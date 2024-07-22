'''
CRYPTOPALS CHALLENGE 3

Single-byte XOR cipher

The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
...has been XOR'd against a single character.  Find the key, decrypt the message.
How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. 
Evaluate each output and choose the one with the best score. 
'''

from binascii import unhexlify
from email.encoders import encode_base64

# Initial hex encoded string:
x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# Convert to byte array 
y = unhexlify(x)

# Function that decrypts the message
def single_xor(y): 
    strings = (''.join(chr(num ^ key) for num in y) for key in range(256)) # Scoring for character
    return (max(strings, key=lambda s: s.count(' ')))

# Test it out
print(f'SOLUTION --> {single_xor(y)}')

'''
The above prints out:

SOLUTION --> Cooking MC's like a pound of bacon
'''