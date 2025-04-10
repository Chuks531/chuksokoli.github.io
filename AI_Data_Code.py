import torch
import torch.nn as nn
import torch.optim as optim
from transformers import BertTokenizer, BertModel

class TransformerClassifier(nn.Module):
    def __init__(self, pretrained_model='bert-base-uncased', num_classes=2):
        super(TransformerClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(pretrained_model)
        self.dropout = nn.Dropout(0.3)
        self.fc = nn.Linear(self.bert.config.hidden_size, num_classes)
        
    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        dropped_out = self.dropout(pooled_output)
        logits = self.fc(dropped_out)
        return logits

# Example usage
def train_model():
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = TransformerClassifier(num_classes=2)
    
    texts = ["Hello, how are you?", "This is an example sentence."]
    encodings = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    input_ids = encodings['input_ids']
    attention_mask = encodings['attention_mask']
    
    outputs = model(input_ids, attention_mask)
    print(outputs)

if __name__ == "__main__":
    train_model()

import numpy as np

def gradient_descent(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)  # Initialize parameters
    for _ in range(epochs):
        gradient = (1/m) * X.T @ (X @ theta - y)  # Compute gradient
        theta -= lr * gradient  # Update parameters
    return theta

# Example Usage
X = np.array([[1, 2], [2, 3], [3, 4]])  # Feature matrix
y = np.array([3, 5, 7])  # Target
theta = gradient_descent(X, y)
print(theta)
