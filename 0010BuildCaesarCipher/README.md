# 🔐 Caesar Cipher in Python

A clean, beginner-friendly, and well-documented implementation of the **Caesar Cipher** encryption and decryption algorithm using Python.

---

## 📌 What is the Caesar Cipher?

The Caesar Cipher is a simple substitution cipher where each letter in the text is shifted by a fixed number of positions in the alphabet.

**Example (shift = 3):**


Hello → Khoor

---

## 🚀 Features

- Encrypt and decrypt text
- Supports uppercase and lowercase letters
- Preserves non-alphabet characters
- Input validation for shift values (1–25)
- Clean, readable, and well-commented code

---

## 🧠 How It Works

1. Define the English alphabet
2. Shift the alphabet by a given number
3. Create a translation table
4. Translate the input text using the table

---
## 📊 Time & Space Complexity

1. Time Complexity: O(n) where n is the length of the input text
2. Space Complexity: O(1) (constant alphabet size)

---


## 🧪 Example Usage

```python
encrypt(3, "Hello, World!")   # Output: Khoor, Zruog!
decrypt(3, "Khoor, Zruog!")  # Output: Hello, World!
if __name__ == "__main__":
    print(encrypt(5, "hi"))            # mn
    print(decrypt(5, "mn"))            # hi
    print(encrypt(3, "Hello"))         # Khoor
    print(encrypt(3, "Hello, World!")) # Khoor, Zruog!
    print(encrypt(30, "test"))         # Error message

