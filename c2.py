'''
Cryptopals Set 1 Challenge 2:  Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.
If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965
... should produce:
746865206b696420646f6e277420706c6179  
'''

from binascii import unhexlify, hexlify

# Pass a into your function & after hex decoding, XOR against b
a = '1c0111001f010100061a024b53535009181c'
b =  '686974207468652062756c6c277320657965'

# This function produces the solution
def fixed_xor(a, b):
    x = unhexlify(a)
    y = unhexlify(b)
    z = bytearray(len(x))
    for i in range(len(x)):
        z[i] = x[i] ^ y[i]
    return hexlify(z)

# As in the previous challenge, If you break it down you get a little more information.
# What is output of the function decoded?
# Test it out
# For printing purposes add --> .decode('UTF-8')
print(f'SOULTION --> {(fixed_xor(a, b)).decode("UTF-8")}')
print(f'{unhexlify(fixed_xor(a, b)).decode("UTF-8")}')

'''
The above prints out:

SOULTION --> 746865206b696420646f6e277420706c6179
the kid don't play
'''
