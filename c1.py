'''
Cryptopals Set 1 Challenge 1:
  
CRYPTOPALS CHALLENGE 1  
Convert hex to base64
Always operate on raw bytes, never on encoded strings.
The string: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
'''
import codecs
from binascii import unhexlify

# Decode hex -> bytes 
def hex_bytes(x):
    return unhexlify(x)

# Enode bytes -> base64 
def bytes_base64(x):
    hextobytes = unhexlify(x)
    return codecs.encode(hextobytes, 'base64')

    
# For printing purposes add --> .decode('UTF-8')
# Test it out
x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(f'SOLUTION --> {(bytes_base64(x)).decode("UTF-8")}')
print(f'{(hex_bytes(x)).decode("UTF-8)")}')

'''
The above prints out:
SOLUTION --> SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
I'm killing your brain like a poisonous mushroom
'''