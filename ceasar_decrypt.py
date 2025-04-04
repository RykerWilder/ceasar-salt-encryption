def caesar_salt_decrypt(ciphertext, key, salt):
    decrypted = []
    salt_vals = [ord(c) for c in salt]
    salt_len = len(salt_vals)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = (key + salt_vals[i % salt_len]) % 26
            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)