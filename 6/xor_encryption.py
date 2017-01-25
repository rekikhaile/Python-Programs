def xor_encrypt(text, key):
    return ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))


def xor_decrypt(secret_text, key):
    return xor_encrypt(secret_text, key)
