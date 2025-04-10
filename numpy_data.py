def BitmapHoles(strArr):
    # Convert string array to a 2D list of integers
    matrix = [list(map(int, row)) for row in strArr]
    rows, cols = len(matrix), len(matrix[0])
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != 0:
            return
        
        matrix[r][c] = -1  # Mark visited
        
        # Explore in all four directions
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left
    
    hole_count = 0
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                dfs(r, c)  # Start DFS from this point
                hole_count += 1  # Increment hole count
    
    return hole_count

# Example test cases
print(BitmapHoles(["01111", "01101", "00011", "11110"]))  # Output: 3
print(BitmapHoles(["1011", "0010"]))  # Output: 2


import torch

def compute_eigenvalues():
    torch.manual_seed(0)  # Set seed for reproducibility
    
    # Create a 5x5 tensor with random values between -1 and 1
    tensor = torch.rand(5, 5) * 2 - 1  
    
    # Compute SVD
    U, S, V = torch.svd(tensor)
    
    # Square singular values to get eigenvalues
    eigenvalues = S ** 2
    
    # Print tensor representation of eigenvalues
    print(eigenvalues)
    
    # Convert to Python list and print
    eigenvalues_list = eigenvalues.tolist()
    print(eigenvalues_list)
    
compute_eigenvalues()

from google.cloud import aiplatform

aiplatform.init(project="my-gcp-project", location="us-central1")

job = aiplatform.CustomJob(
    display_name="ml-training-job",
    script_path="train.py",
    container_uri="gcr.io/cloud-aiplatform/training/tf-cpu.2-6:latest",
    args=["--epochs", "10", "--batch_size", "32"],
    staging_bucket="gs://my-ml-pipeline-data"
)

job.run()
