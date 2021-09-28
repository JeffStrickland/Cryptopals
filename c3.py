"""
Cryptoplas Challenge 3:  Single-byte XOR cipher
The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
...has been XOR'd against a single character.  Find the key, decrypt the message.
How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. 
Evaluate each output and choose the one with the best score. 
"""
import codecs
# Initial hex encoded string:
x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def hex_bytes(x):  # hex > bytes 
    return codecs.decode(x, 'hex')
    ### b'\x1b77316?x\x15\x1b\x7f+x413=x9x(7-6<x7>x:9;76' ###
    
def single_xor(y): # scoring for character frequency
    strings = (''.join(chr(num ^ key) for num in y) for key in range(256))
    return (max(strings, key = lambda s: s.count(' ')))
    
print(single_xor(hex_bytes(x)))
### Cooking MC's like a pound of bacon ###