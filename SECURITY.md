# Security Policy

## 🔒 Introduction

Digest Fusion Hashing (DFH) was designed with a focus on strong security, data integrity, and resilience against tampering.

---

## 📚 Scope of Security

DFH provides:

- Secure fusion of digests using randomized splits.
- Protection against tampering, assuming a trusted environment.

DFH does **not** protect against:

- Infected hardware or compromised operating systems.
- Poor randomness or weak secret inputs.
- Cryptographic breakthroughs affecting SHA3-512.

---

## ✅ Best Practices for Secure Usage

- Use high-entropy content and signatures.
- Ensure true randomness in split ratio generation.
- Protect secret signatures.
- Operate in trusted environments.

---

## ⚠️ Known Limitations

- Vulnerabilities in SHA3-512 would affect DFH.
- DFH relies on the quality of random number generation.
- Hardware attacks are outside its protection scope.

These limitations are common to all cryptographic solutions.