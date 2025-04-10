from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, unix_timestamp, date_format, current_timestamp, regexp_replace
import mysql.connector

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .config("spark.jars", "C:/jdbc/mysql-connector-java-8.0.33.jar,C:/jdbc/postgresql-42.5.4.jar") \
    .getOrCreate()

# Reduce logging
spark.sparkContext.setLogLevel("ERROR")

# MySQL connection details
MYSQL_URL = "jdbc:mysql://127.0.0.1:3306/user_activity_logs"
MYSQL_USER = "root2"
MYSQL_PASSWORD = "Colkim234#"

# File Paths
json_files = [
    r"C:\Users\Chuks\Downloads\Prod_Data_Pipeline\Data_Store1\data_cdz003.json",
    r"C:\Users\Chuks\Downloads\Prod_Data_Pipeline\Data_Store1\data_xyz789.json",
    r"C:\Users\Chuks\Downloads\Prod_Data_Pipeline\Data_Store1\data_xzy401.json"
]

# Extract Data from JSON Files
df = spark.read.option("multiline", "true").json(json_files)



# Step 2: Transform - Convert timestamp, standardize device_type
df_transformed = df.withColumn("timestamp", to_timestamp(col("timestamp"), "yyyy-MM-dd'T'HH:mm:ss'Z'")) \
    .withColumn("device_type", regexp_replace(col("device_type"), "(?i)andriod", "Android"))  # Fix typos

# Step 3: Load - Write data to MySQL
df_transformed.write \
    .format("jdbc") \
    .option("url", MYSQL_URL) \
    .option("dbtable", "user_interactions") \
    .option("user", MYSQL_USER) \
    .option("password", MYSQL_PASSWORD) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .mode("append") \
    .save()

print("ETL Pipeline Execution Completed Successfully!")