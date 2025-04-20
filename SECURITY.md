# Security Policy

## 🔒 Introduction

Digest Fusion Hashing (DFH) was designed with a strong focus on security, ensuring data integrity and resilience against tampering or unauthorized modifications.  
We take security very seriously and are committed to maintaining the highest standards in cryptographic practices.

---

## 📚 Scope of Security

Digest Fusion Hashing provides:

- Secure fusion of cryptographic digests using a randomized split ratio.
- Protection against common tampering attacks assuming:
  - Secure environment (no malware, memory sniffers, or compromised runtime).
  - Adequate entropy in content and signatures.

However, the system does **not** protect against:

- Compromised operating systems or infected hardware.
- Poor randomness or weak secrets provided by users.
- Future cryptographic vulnerabilities in underlying algorithms (e.g., SHA3-512).

---

## ✅ Best Practices for Secure Usage

To maximize the security offered by Digest Fusion Hashing:

- Use strong, high-entropy content and signatures.
- Ensure split ratio generation remains truly random within the defined range (0.30–0.70).
- Protect secret signatures from leaks or exposure.
- Operate the hashing system in a secure and trusted environment.
- Keep all software dependencies and runtime environments updated.

---

## ⚠️ Known Limitations

While DFH enhances security by digest fusion, it inherits the properties and potential risks of its cryptographic primitives:

- If SHA3-512 or its implementations are compromised, DFH's security may also be affected.
- DFH relies on the quality of the random generator for split ratio generation.
- DFH does not defend against hardware-based attacks (e.g., cold boot attacks, side-channel attacks).

**Note:** These limitations are common to all cryptographic solutions and not unique to DFH.

---
