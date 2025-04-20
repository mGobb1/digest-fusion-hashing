# Digest Fusion Hashing (DFH)

A next-generation hashing technique that combines cryptographic digests of a content and a secret signature using a randomized split ratio.  
This increases security and resilience against traditional hash-based attacks.

Secure, lightweight, and built for modern Python projects.

---

## 🔍 Why Digest Fusion Hashing is Next-Generation

Digest Fusion Hashing introduces concepts aligned with the next evolution of secure hashing systems:

- **Dynamic Digest Fusion:**  
  Instead of a direct hashing of the content, DFH combines two independent digests (content and signature) with a randomized structural split before the final hash is calculated.
  
- **Randomized Structural Variation:**  
  The split ratio is randomly generated for every operation, increasing unpredictability and making preimage or collision attacks significantly more complex.

- **Multiple Security Layers:**  
  Attackers must control both the content and the signature, predict the correct random split ratio, and reconstruct the fused digest accurately before even attempting to match the final hash.

- **Increased Resistance to Targeted Attacks:**  
  Compared to traditional hashing, DFH imposes multiple independent barriers to potential attackers.

Digest Fusion Hashing is designed not only for today's security needs but also to anticipate the challenges and adversaries of tomorrow.

---

## 🚀 Features

- Secure digest fusion with randomized split ratio
- Verifiable content integrity
- Easy to use API
- Clean and professional codebase
- 100% unit test coverage
- Ready for production

---

## 🛠 Technologies Used

- Python 3.10+
- `pytest` for testing

---

## ⚙️ Installation

You can install it locally:

```bash
git clone https://github.com/your-username/digest-fusion-hashing.git
cd digest-fusion-hashing
pip install -r requirements.txt
```

---

## 🧐 How It Works

- `DigestFusionHasher.hash(content, signature)`:
  - Generates a fused cryptographic hash.
  - Returns the final hash and the random split ratio used.
- `DigestFusionHasher.verify(content, signature, split_ratio, expected_hash)`:
  - Verifies whether given content and signature reproduce the expected hash.
  - Raises an error if the split ratio is invalid.

---

## 🧹 Example Usage

```python
from dfh.core import DigestFusionHasher

# Initialize
hasher = DigestFusionHasher()

# Content and secret signature
content = b"My important data"
signature = b"My top secret signature"

# Generate hash
result = hasher.hash(content, signature)
print("Final Hash:", result["final_hash"])
print("Split Ratio Used:", result["split_ratio"])

# Verify hash
is_valid = hasher.verify(content, signature, result["split_ratio"], result["final_hash"])
print("Verification:", "Success" if is_valid else "Failed")
```

---

## 💂 Project Structure

```plaintext
src/
└── dfh/
    ├── core.py              # Core hashing logic
    ├── exceptions.py        # Custom exceptions
    └── __init__.py           # Package initialization
tests/
└── test_core.py              # Unit tests
pytest.ini                    # Test runner configuration
requirements.txt              # Project dependencies
README.md                     # Project documentation
LICENSE                       # MIT License
```

---

## 📜 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## ✨ Author

Developed with care by **Miguel Gobbi**

---
