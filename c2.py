"""
Cryptopals Set 1 Challenge 2:  Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.
If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965
... should produce:
746865206b696420646f6e277420706c6179  
"""
import codecs

# buffers to compare
a = '1c0111001f010100061a024b53535009181c'
b =  '686974207468652062756c6c277320657965'

def hex_bytes(x):  # hex > bytes function from Challenge 1
    return codecs.decode(x, 'hex')

# convert buffers to bytes
x = hex_bytes(a)
y = hex_bytes(b)

def xor(x, y):
        b = bytearray(len(x))
        for i in range(len(x)):
            b[i] = x[i] ^ y[i]
        return b
    
# XOR the byte arrays
b = bytes(xor(x, y))
### the kid don't play ###

# Test
print(b.decode('UTF-8'))
# convert back to hex
print(b.hex()) 
###  746865206b696420646f6e277420706c6179 ###
