""" 
Cryptopals Set 1 Challenge 1:  Convert hex to base64
Always operate on raw bytes, never on encoded strings.
The string: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
"""
import codecs

def hex_bytes(x):  # Function converting hex to bytes--
    return codecs.decode(x, 'hex')
### I'm killing your brain like a poisonous mushroom ###

def bytes_base64(y):  # Function converting bytes to base64--
    return codecs.encode(y, 'base64')
### SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t ###
    

# Test
x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(hex_bytes(x).decode('UTF-8'))
print(bytes_base64(hex_bytes(x)).decode('UTF-8'))
