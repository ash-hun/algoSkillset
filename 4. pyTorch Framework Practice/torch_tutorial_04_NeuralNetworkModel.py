import os
import torch
from torch import nn
from torch.utils.data import dataloader
from torchvision import datasets, transforms


device = "cuda" if torch.cuda.is_available() else "cpu"
print(f'device : {device}')

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512,512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )
    
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

if __name__=="__main__":
    model = NeuralNetwork().to(device)
    print(model)
    X = torch.rand(1, 28, 28, device=device)
    logits = model(X)
    pred_prob = nn.Softmax(dim=1)(logits)
    y_pred = pred_prob.argmax(1)
    print(f"Predicted class: {y_pred}")
    print(pred_prob)