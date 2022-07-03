'''
An ECB/CBC detection oracle

Now that you have ECB and CBC working:

Write a function to generate a random AES key; that's just 16 random bytes.

Write a function that encrypts data under an unknown key --- that is, a function that generates a random key and encrypts under it.

The function should look like:

encryption_oracle(your-input)
=> [MEANINGLESS JIBBER JABBER]

Under the hood, have the function append 5-10 bytes (count chosen randomly) before the plaintext and 5-10 bytes after the plaintext.

Now, have the function choose to encrypt under ECB 1/2 the time, and under CBC the other half (just use random IVs each time for CBC). Use rand(2) to decide which to use.

Detect the block cipher mode the function is using each time. You should end up with a piece of code that, pointed at a block box that might be encrypting ECB or CBC, tells you which one is happening.
'''

''' AES (Advanced Encryption Standard) was originally called Rijndael and is a symmetric block algorithm for encrypting 
or decrypting data. The standard was established by the U.S. National Institute of Standards and Technology (NIST) 
in 2001.'''

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import random
from base64 import b64encode
import json
from Crypto.Util.Padding import pad

# Random byte generator
def random_bytes(length):
    return get_random_bytes(length)

# Random key generator. With AES you can generate a 128, 192, or 256 bit key.
def random_key_gen(length):
    return random_bytes(length) # length must be 16, 24 or 32 bytes long

# Random number generator
def random_num_gen(x, y): # x, y are represent the range
    return random.randint(x, y)

# Pad data with 5-10 random bytes at the begining & end
def padded_data(data):
    x = random_num_gen(10, 16)
    y = random_num_gen(10, 16)
    return (random_bytes(x) + data + random_bytes(y))

def encrypt_with_aes_ecb(key, data, blks): # length must be 16, 24 or 32 bytes long 
    block_size = blks
    cipher = AES.new(key, AES.MODE_ECB) # generate key
    encrypted = cipher.encrypt(pad(data, block_size))
    return encrypted
   

def encrypt_with_aes_cbc(key, data): # length must be 16, 24 or 32 bytes long 
    cipher = AES.new(key, AES.MODE_CBC) # generate key
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':ct})
    return result

# Test 
def test(): # Encrypts 50% of the time with AES_CDC and 50% with AES_ECB
    x = b'Encrypt this meaningless jibber jabber.'
    decide = random.randint(1,3) # random number to randomly decide which encryption method to use
    prepped_data = padded_data(x)
    if (decide % 2) == 0:
        z = encrypt_with_aes_ecb(random_key_gen(16) , prepped_data, 16)
        print('Encrypted with AES_ECB')
        return z
    else:
        z = encrypt_with_aes_cbc(random_key_gen(16), prepped_data)
        print('Encrypted with AES_CBC')
        return z

if __name__ == "__main__":
    print(test())


