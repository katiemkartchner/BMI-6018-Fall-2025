"""
PyTorch is a Python library that helps people build and train
neural networks. You can think of it like a tool that makes
math with big grids of numbers (called tensors) much easier,
especially when using a GPU. PyTorch can automatically compute
gradients for you, which means it can figure out how a model
should change its weights during training. It is widely used
in machine learning classes, research, and real-world 
 projects. If you ever want to learn more, the best resources
are the official website (pytorch.org) and the tutorials they
 provide. They walk through basics step-by-step and are great
for beginners.

Advantages:
 It's easy to use because it feels like regular Python.
You can see what your model is doing while it runs, which
 makes debugging and learning much simpler.
It works well with GPUs, which helps models train faster.
Lots of people use it, so there are many tutorials online.

Limitations:
It can feel like a lot to learn at first, because you must
 understand some details of how models work.
Training very big models can be slow if you do not have a GPU.
Older online examples may not match the newest version of
 PyTorch, so sometimes you have to double-check documentation.
 """

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# Make sure the GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

# Load the MNIST dataset that we will practice with here
transform = transforms.ToTensor()
train_data = datasets.MNIST(
    root="data",
    train=True,
    download=True,
    transform=transform,
)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

# Simple neural network for two layers
class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.fc = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.fc(x)
        return logits

model = SimpleNN().to(device)
print(model)

# Do the loss function and an optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# Train for only a few batches at first
model.train()
for batch_idx, (images, labels) in enumerate(train_loader):
    if batch_idx >= 5:
        break

    images, labels = images.to(device), labels.to(device)

    outputs = model(images)
    loss = criterion(outputs, labels)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Batch {batch_idx+1}, Loss: {loss.item():.4f}")

# Quick check on a small batch to make sure it's working
model.eval()
with torch.no_grad():
    sample_images, sample_labels = next(iter(train_loader))
    sample_images = sample_images.to(device)
    sample_outputs = model(sample_images)
    predicted = sample_outputs.argmax(dim=1)

print("True labels:     ", sample_labels[:10].tolist())
print("Predicted labels:", predicted[:10].cpu().tolist())