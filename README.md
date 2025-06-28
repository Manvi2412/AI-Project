
#  Object Detection using SSD with ResNet-50 Backbone

This project implements a simplified **Single Shot Detector (SSD)** from scratch using a **ResNet-50** backbone. The model is trained on the **Pascal VOC 2007 dataset** using PyTorch. It forms part of an internship submission and showcases understanding of building object detection pipelines using custom model architecture and training logic.

---

##  Project Overview

-  Custom SSD architecture built using PyTorch
-  ResNet-50 used as a feature extractor backbone
-  Pascal VOC 2007 used as the training dataset
-  Implements separate classification and localization heads
-  Basic training loop with dummy bounding box targets (proof of concept)
-  Model trained and saved as `.pth` for reproducibility

>  **Note**: This version uses **dummy bounding boxes** for the training process and does not yet include real IoU-based matching logic or true bounding box regression. It is a structural and architectural demonstration — not yet a complete detection system.

---

##  Project Structure
object_detection_project/
│
├── object_detection_project_submission.py # Main training script
├── ssd_resnet_pascal.pth # Saved model weights
└── README.md # Project documentation (this file)


---

##  Model Architecture

### Backbone
- ResNet-50 (pretrained on ImageNet)
- Final pooling and classification layers removed
- Early layers frozen for stability

### SSD Head
- Classification Head: `Conv2d(2048, 4 * num_classes)`
- Localization Head: `Conv2d(2048, 4 * 4)` for bounding box coordinates

---

##  Dataset

- **Pascal VOC 2007**
- Automatically downloaded via `torchvision.datasets.VOCDetection`
- 20 object classes + 1 background class
- Images resized to `(300, 300)` for SSD input

---

##  Training Details

- Batch Size: 4
- Optimizer: Adam (lr=1e-4)
- Losses:
  - `CrossEntropyLoss` for classification
  - `SmoothL1Loss` for box localization (with placeholder targets)

> 🔧 Targets for bounding box regression were generated using random tensors. Matching anchor boxes to ground-truth boxes (IoU-based matching) is not yet implemented.
---

##  What This Project Demonstrates

Despite its simplified training logic, this project showcases:

-  Understanding of object detection architectures
-  Ability to use pretrained backbones for feature extraction
-  Integration of datasets, transforms, and custom heads
-  Model definition and training using PyTorch
-  Awareness of architectural requirements for SSD

---

## 🔧 How to Run

1. Install dependencies
pip install torchvision albumentations tqdm matplotlib

2. Run the script
python object_detection_project_submission.py

3. The model will be trained on dummy targets and saved as ssd_resnet_pascal.pth.

### Future Improvements (Planned)
Integrate real target extraction with IoU matching

Add anchor generation and decoder for prediction

Enable inference and draw boxes on test images

Add Streamlit demo or web dashboard

Compare with pretrained SSD models




