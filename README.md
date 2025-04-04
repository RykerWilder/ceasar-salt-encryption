# Caesar Cipher with Secret Key + Salt

An extension of the classic Caesar Cipher that improves security by introducing a secret numeric key and a random salt.

---

```python
plaintext = "HELLO"
key = 5
salt = "XQ3"
ciphertext = caesar_salt_encrypt(plaintext, key, salt)
print("Ciphertext:", ciphertext)  # Output: "WMPAW"
```

To see how the Caesar Salt cipher works with secret key see here [Ceasar Salt Cipher with secret key](https://github.com/RykerWilder/notes/blob/main/encryption/ceasar-key-salt.md)