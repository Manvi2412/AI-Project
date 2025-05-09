# -*- coding: utf-8 -*-
"""Object_Detection_Project_Submission.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wNVo7OblnU1Ov3oGVaPr6jeXYqGhyvtE

# Object Detection using SSD with ResNet-50 Backbone

Internship Project Submission

This notebook implements a simplified Single Shot Detector (SSD) with a ResNet-50 backbone, using the Pascal VOC dataset.
"""

# Install necessary packages
!pip install torchvision albumentations tqdm

import torch
import torchvision
import torchvision.transforms as transforms
from torchvision.datasets import VOCDetection
from torch.utils.data import DataLoader
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

# Load Pascal VOC Dataset
transform = transforms.Compose([
    transforms.Resize((300, 300)),
    transforms.ToTensor(),
])

dataset = VOCDetection(root='./data', year='2007', image_set='train', download=True, transform=transform)
data_loader = DataLoader(dataset, batch_size=4, shuffle=True)

# Load ResNet-50 backbone
backbone = torchvision.models.resnet50(pretrained=True)
backbone = nn.Sequential(*list(backbone.children())[:-2])

# Freeze early layers
for param in list(backbone.parameters())[:5]:
    param.requires_grad = False

# Define SSD Head
class SSDHead(nn.Module):
    def __init__(self, num_classes):
        super(SSDHead, self).__init__()
        self.loc = nn.Conv2d(2048, 4 * 4, kernel_size=3, padding=1)
        self.cls = nn.Conv2d(2048, 4 * num_classes, kernel_size=3, padding=1)

    def forward(self, x):
        loc = self.loc(x)
        cls = self.cls(x)
        return loc, cls

class SimpleSSD(nn.Module):
    def __init__(self, backbone, num_classes):
        super(SimpleSSD, self).__init__()
        self.backbone = backbone
        self.head = SSDHead(num_classes)

    def forward(self, x):
        x = self.backbone(x)
        return self.head(x)

model = SimpleSSD(backbone, num_classes=21)  # 20 classes + background

import torch
import torch.nn as nn
import torchvision.models as models

# Load backbone
backbone = models.resnet50(pretrained=True)
backbone = nn.Sequential(*list(backbone.children())[:-2])

# Define SSD Head
class SSDHead(nn.Module):
    def __init__(self, num_classes):
        super(SSDHead, self).__init__()
        self.loc = nn.Conv2d(2048, 4 * 4, kernel_size=3, padding=1)
        self.cls = nn.Conv2d(2048, 4 * num_classes, kernel_size=3, padding=1)

    def forward(self, x):
        loc = self.loc(x)
        cls = self.cls(x)
        return loc, cls

class SimpleSSD(nn.Module):
    def __init__(self, backbone, num_classes):
        super(SimpleSSD, self).__init__()
        self.backbone = backbone
        self.head = SSDHead(num_classes)

    def forward(self, x):
        x = self.backbone(x)
        return self.head(x)

# Instantiate model
model = SimpleSSD(backbone, num_classes=21)

# Dummy test input
x = torch.randn(1, 3, 300, 300)
loc, cls = model(x)

print(loc.shape, cls.shape)

# Define loss and optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
classification_loss = nn.CrossEntropyLoss()
localization_loss = nn.SmoothL1Loss()

import torch
import torch.nn as nn

# Make sure model is already defined here
# Example dummy model if needed:
# model = nn.Linear(10, 2)

optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
classification_loss = nn.CrossEntropyLoss()
localization_loss = nn.SmoothL1Loss()

print("Optimizer and losses defined successfully.")

# Simplified training loop with dummy targets
def train(model, loader, epochs=3):
    model.train()
    for epoch in range(epochs):
        total_cls_loss, total_loc_loss = 0, 0
        for imgs, targets in loader:
            loc_preds, cls_preds = model(imgs)

            cls_loss = classification_loss(cls_preds.view(-1, 21), torch.zeros(cls_preds.numel() // 21, dtype=torch.long))
            loc_loss = localization_loss(loc_preds, torch.randn_like(loc_preds))

            loss = cls_loss + loc_loss
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_cls_loss += cls_loss.item()
            total_loc_loss += loc_loss.item()

        print(f"Epoch {epoch+1}: Cls Loss={total_cls_loss:.4f}, Loc Loss={total_loc_loss:.4f}")

def train(model, loader, epochs=3):
    model.train()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    for epoch in range(epochs):
        total_cls_loss, total_loc_loss = 0, 0
        for imgs, targets in loader:
            imgs = imgs.to(device)
            loc_preds, cls_preds = model(imgs)

            cls_preds = cls_preds.permute(0, 2, 3, 1).contiguous()
            cls_preds = cls_preds.view(-1, 21)
            targets_cls = torch.zeros(cls_preds.shape[0], dtype=torch.long).to(device)

            loc_loss = localization_loss(loc_preds, torch.randn_like(loc_preds).to(device))
            cls_loss = classification_loss(cls_preds, targets_cls)

            loss = cls_loss + loc_loss
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_cls_loss += cls_loss.item()
            total_loc_loss += loc_loss.item()

        print(f"Epoch {epoch+1}: Cls Loss={total_cls_loss:.4f}, Loc Loss={total_loc_loss:.4f}")

def train(model, loader, epochs=3):
    print("🚀 Training started...")
    model.train()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    for epoch in range(epochs):
        print(f"\n🟢 Epoch {epoch+1} starting...")
        total_cls_loss, total_loc_loss = 0, 0
        for batch_idx, (imgs, targets) in enumerate(loader):
            imgs = imgs.to(device)

            loc_preds, cls_preds = model(imgs)

            cls_preds = cls_preds.permute(0, 2, 3, 1).contiguous()
            cls_preds = cls_preds.view(-1, 21)
            target_cls = torch.zeros(cls_preds.shape[0], dtype=torch.long).to(device)

            loc_loss = localization_loss(loc_preds, torch.randn_like(loc_preds).to(device))
            cls_loss = classification_loss(cls_preds, target_cls)

            loss = cls_loss + loc_loss
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_cls_loss += cls_loss.item()
            total_loc_loss += loc_loss.item()

            # Debug every 5 batches
            if batch_idx % 5 == 0:
                print(f"  Batch {batch_idx}: cls={cls_loss.item():.4f}, loc={loc_loss.item():.4f}")

        print(f"✅ Epoch {epoch+1} completed | Cls Loss: {total_cls_loss:.4f}, Loc Loss: {total_loc_loss:.4f}")

def collate_fn(batch):
    images = [item[0] for item in batch]
    targets = [item[1] for item in batch]
    return torch.stack(images, dim=0), targets

data_loader = DataLoader(dataset, batch_size=4, shuffle=True, collate_fn=collate_fn)

train(model, data_loader, epochs=3)

# Save model
torch.save(model.state_dict(), "ssd_resnet_pascal.pth")

