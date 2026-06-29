# Malicious ML Model PoC (Insecure Deserialization)

>[!WARNING]
>This project is for educational purposes only. Do not run untrusted ML models in real environments.

## Overview
This project demonstrates how loading an untrusted `.pkl` machine learning model can lead to arbitrary code execution.

## The Vulnerability
Python pickle allows execution of arbitrary code during deserialization.

## Exploit
The `model.pkl` file contains a payload that executes when loaded.

## Reproduction
git clone ...
cd iris-classifier
python predict.py

## Output
MALICIOUS CODE EXECUTED

## Mitigation
- Never load untrusted pickle files
- Use safer formats (ONNX, JSON)
- Validate model sources
