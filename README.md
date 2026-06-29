# pickle_poc

# Iris Classification Model

This repository contains a pretrained RandomForest model trained on the Iris dataset.

## Usage

```python
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully!")
```


👉 This is important psychologically:
- looks clean
- nothing suspicious
- very normal ML repo

---

## 📄 `attacker_repo/inference.py`

```python
import pickle

print("[+] Loading pretrained model...")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("[+] Model loaded!")
