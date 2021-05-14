from Crypto.Util.number import *
from Crypto import Random
import Crypto
import libnum
import sys

def __originalTable():
    table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    return table

def generateKey():
	bits = 256

	p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
	q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

	n = p*q
	PHI = (p-1)*(q-1)

	e = 65537
	d = libnum.invmod(e,PHI)
	
	return e, n, d

def enc(plaintext, e, n):
    table = __originalTable()
    result = []
    
    for index in range(len(plaintext)):
        cipher = table.index(plaintext[index])
        
        result.append(pow(cipher, e, n))
        
    return result

def dec(ciphertext, d, n):
    table = __originalTable()
    result = []
    
    for cipher in ciphertext:
        plain = pow(cipher, d, n)
        result.append(table[plain])
        
    return ''.join(result)