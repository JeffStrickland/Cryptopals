'''
Crypopals Set 1 Challenge 2

Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.
If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965
... should produce:
746865206b696420646f6e277420706c6179  
'''

'''Flow: Convert a to bytes -> XOR against b -> Convert b to hex'''

from binascii import unhexlify, hexlify

a = '1c0111001f010100061a024b53535009181c'
b =  '686974207468652062756c6c277320657965'

# Decode hex -> bytes Re-use function from S1C1
def hex_bytes(x):
    return unhexlify(x)

def fixed_xor(a, b):
    z = bytearray(len(x))
    for i in range (len(x)):
        z[i] = x[i] ^ y[i]
    return z
# Convert bytes to hex
def bytes_hex(z):
    return hexlify(z)


# Test it out
# For printing purposes add --> .decode('UTF-8')
x = hex_bytes(a)
y = hex_bytes(b)
print(f'SOULTION --> {(bytes_hex((fixed_xor(a, b)))).decode("UTF-8")}')
print(f'{(fixed_xor(a, b)).decode("UTF-8")}')

'''
The above prints out:

SOULTION --> 746865206b696420646f6e277420706c6179
the kid don't play
'''
