from module.rsa import main as rsa
from module.vigenere import main as vigenere
import time
import os.path
import sys

def generateRsaKey():
    if not checkRsaKeyExist():
        try:
            rsa.generateKey()
            return True
        except Exception as e:
            print(f'Failed: {e}')
            sys.exit()
        
def checkRsaKeyExist():
    if os.path.isfile('key/priv.pem') and os.path.isfile('key/pub.pem'):
        return True
    
def encrypt(plaintext, key, e, n):
    start = time.perf_counter()
    generateRsaKey()
    ciphertext, strech_key = vigenere.encrypt(plaintext, key)
    key_enc = rsa.enc(strech_key, e, n)
    stop = time.perf_counter()
    
    print(f"Encrypt used time: {stop - start:0.4f} seconds")
    return ciphertext, key_enc

def decrypt(ciphertext, key, d, n):
    start = time.perf_counter()
    generateRsaKey()
    key_dec = rsa.dec(key, d, n)
    plaintext = vigenere.decrypt(ciphertext, key_dec)
    stop = time.perf_counter()
    
    print(f"Decrypt used time: {stop - start:0.4f} seconds")
    return plaintext

# plaintext = "In cryptography, encryption is the process of encoding information."
plaintext = "In cryptography, encryption is the process of encoding information. This process converts the original representation of the information, known as plaintext, into an alternative form known as ciphertext. Ideally, only authorized parties can decipher a ciphertext back to plaintext and access the original information."
# plaintext = "In cryptography, encryption is the process of encoding information. This process converts the original representation of the information, known as plaintext, into an alternative form known as ciphertext. Ideally, only authorized parties can decipher a ciphertext back to plaintext and access the original information. Encryption does not itself prevent interference but denies the intelligible content to a would-be interceptor. For technical reasons, an encryption scheme usually uses a pseudo-random encryption key generated by an algorithm. It is possible to decrypt the message without possessing the key but, for a well-designed encryption scheme, considerable computational resources and skills are required. An authorized recipient can easily decrypt the message with the key provided by the originator to recipients but not to unauthorized users. Historically, various forms of encryption have been used to aid in cryptography. Early encryption techniques were often utilized in military messaging. Since then, new techniques have emerged and become commonplace in all areas of modern computing. Modern encryption schemes utilize the concepts of public-key and symmetric-key. Modern encryption techniques ensure security because modern computers are inefficient at cracking the encryption."

e, n, d = rsa.generateKey()
ciphertext, key = encrypt(plaintext, "ASDR", e, n)
decrypt = decrypt(ciphertext, key, d, n)

print(ciphertext)