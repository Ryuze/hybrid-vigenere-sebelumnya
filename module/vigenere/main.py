import random
import secrets
from ordered_set import OrderedSet

def __originalTable():
    table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    return table

def encrypt(plaintext, initial_key):
    table = __originalTable()
    temp_text = plaintext.upper()
    temp_key = initial_key.upper()
    text_upper = ""
    key = temp_key
    cipher = []
    
    for char in temp_text:
        if char.isalnum():
            text_upper += char
        
    rounds = len(text_upper) / len(key)
    start = 1
    while start < rounds:
        key += temp_key
        start += 1
        
    for index in range(len(text_upper)):
        calculate = (table.index(text_upper[index]) + table.index(key[index])) % 26
        cipher.append(table[calculate])
    
    return ''.join(cipher), key

def decrypt(ciphertext, key):
    table = __originalTable()
    tempKey = key
    plain = []
    
    rounds = len(ciphertext) / len(key)
    start = 1
    while start < rounds:
        tempKey += key
        start += 1
    
    for index in range(len(ciphertext)):
        calculate = (table.index(ciphertext[index]) - table.index(tempKey[index])) % 26
        plain.append(table[calculate])
    
    return ''.join(plain)