# 🔍 Object Detection using Simple SSD (Single Shot MultiBox Detector)

This project implements a simplified version of the SSD (Single Shot MultiBox Detector) architecture using a ResNet-50 backbone in PyTorch. It was developed to demonstrate understanding of object detection pipelines and model training in a deep learning environment.

---

## 📁 Project Structure

- `object_detection_project_submission.py` – Main source code with model architecture, dataset loading, training, and evaluation.
- `demo_output.png` – Sample image showing predicted bounding boxes (if applicable).
- `AI_Internship_Experience_Report.pdf` – Experience reflection as per internship submission requirements.
- `README.md` – This file.

---

## ⚙️ Technologies Used

- Python 3.9
- PyTorch
- torchvision
- Pascal VOC Dataset (via `torchvision.datasets.VOCDetection`)
- Matplotlib (for visualization)

---

## 🧠 Model Overview

- **Backbone:** ResNet-50 (pretrained)
- **Head:** SSD-style predictor with:
  - 4 bounding box regressors
  - N-class classifier (21 classes including background)
- **Loss Functions:**
  - CrossEntropyLoss (classification)
  - SmoothL1Loss (localization)

---

## 🏋️‍♀️ Training

- Dataset: Pascal VOC 2012
- Image Size: 300x300
- Epochs: 3 (demo scale)
- Optimizer: Adam (lr = 1e-4)

Training was performed using dummy targets (for demonstration purposes). The model was designed and trained to demonstrate understanding of detection architecture and pipeline structure, not production-level performance.

---

## 📊 Evaluation

- Training logs include classification and localization loss per epoch.
- Bounding box predictions are visualized on sample images using matplotlib.
- In absence of annotated real-world targets, metrics like mAP were not computed.

---

## 🖼️ Output Demo

Example image with predicted bounding boxes is saved as:
