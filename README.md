# 🌸 Iris Classifier (Pretrained Model Included)

A lightweight and easy to use machine learning model for classifying iris flower species with high accuracy.

## Features
- Pretrained scikit learn model (no training required)
- Fast predictions
- Minimal dependencies
- Beginner friendly

## Model Performance
Achieves ~97% accuracy on the standard Iris dataset.

## Quick Start

Clone the repository:

```
git clone https://github.com/williamholian/iris-classifier.git
cd iris-classifier
```
Run the prediction script:

```
python predict.py
```

That's it! The script will automatically load the pretrained model and run inference.

## Files Included
- `model.pkl` – pretrained classification model
- `predict.py` – inference script

## Notes
This project is intended for educational and prototyping purposes. The model is lightweight and designed to run locally without GPU support.

Feel free to fork and experiment!



---




# Malicious ML Model PoC (Insecure Deserialization)

>[!WARNING]
>This project is for educational purposes only. Do not run untrusted ML models in real environments.

**Overview:**

This project demonstrates how loading an untrusted `.pkl` machine learning model can lead to arbitrary code execution.

**The Vulnerability:**

Python pickle allows execution of arbitrary code during deserialization.

**Exploit:**

The `model.pkl` file contains a payload that executes when loaded.

**Reproduction:**

git clone ...
cd iris-classifier
python predict.py

**Output:**

MALICIOUS CODE EXECUTED

**Mitigation:**

- Never load untrusted pickle files
- Use safer formats (ONNX, JSON, safetensors)
- Validate model sources
