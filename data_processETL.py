from pyspark.sql import SparkSession

# Initialize Spark Session with MySQL JDBC driver
spark = SparkSession.builder \
    .appName("MySQL ETL Pipeline") \
    .config("spark.driver.extraClassPath", "C:\\spark\\spark-3.5.4-bin-hadoop3\\jars\\mysql-connector-java-9.2.0.jar") \
    .config("spark.executor.extraClassPath", "C:\\spark\\spark-3.5.4-bin-hadoop3\\jars\\mysql-connector-java-9.2.0.jar") \
    .getOrCreate()

# MySQL Database Credentials
jdbc_url = "jdbc:mysql://127.0.0.1:3306/sakila"  # Corrected the URL format
db_properties = {
    "user": "root2",
    "password": "Colkim234#",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Load Data from MySQL Table
df = spark.read.jdbc(url=jdbc_url, table="customer", properties=db_properties)

# Show Data from MySQL
df.show()

# Data Transformation Example
df_filtered = df.filter(df.first_name == 'Lisa')  # Updated transformation logic

# Save Transformed Data to MySQL Table using Append Mode
df_filtered.write.jdbc(url=jdbc_url, table="customer_transformed", mode="append", properties=db_properties)

print("Data Transformation and Saving Completed")
