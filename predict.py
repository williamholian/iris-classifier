import pickle

print("[+] Loading model...")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("[+] Model loaded!")