from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def generate_key():
    return get_random_bytes(16)

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt_message(key, iv, ciphertext):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ciphertext)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

key = generate_key()
iv, ciphertext = encrypt_message(key, "Hello, this is a secret message!")
plaintext = decrypt_message(key, iv, ciphertext)

print("Encrypted:", ciphertext)
print("Decrypted:", plaintext)
