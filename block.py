from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

def aes_encrypt_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return binascii.hexlify(ciphertext).decode()
from Crypto.Util.Padding import unpad

def aes_decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(binascii.unhexlify(ciphertext))
    return unpad(decrypted_data, AES.block_size).decode()
key = b'This is a key123'  # 16 bytes key for AES-128
plaintext = 'Hello, IoT World!'

print(f'Original Text: {plaintext}')

encrypted = aes_encrypt_ecb(plaintext, key)
print(f'Encrypted Text: {encrypted}')

decrypted = aes_decrypt_ecb(encrypted, key)
print(f'Decrypted Text: {decrypted}')
