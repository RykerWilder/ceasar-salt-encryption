def caesar_salt_encrypt(plaintext, key, salt):
    encrypted = []
    salt_vals = [ord(c) for c in salt]
    salt_len = len(salt_vals)
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = (key + salt_vals[i % salt_len]) % 26
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted.append(encrypted_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)

plaintext = "HELLO"
key = 5
salt = "XQ3"
ciphertext = caesar_salt_encrypt(plaintext, key, salt)
print("Ciphertext:", ciphertext)  # Output: "WMPAW"