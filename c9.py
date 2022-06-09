'''
CRYPTOPALS CHALLENGE 9

Implement PKCS#7 padding

A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. But we almost never want to transform a single block; we encrypt irregularly-sized messages.

One way we account for irregularly-sized messages is by padding, creating a plaintext that is an even multiple of the blocksize. The most popular padding scheme is called PKCS#7.

So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. For instance,

"YELLOW SUBMARINE"

... padded to 20 bytes would be:

"YELLOW SUBMARINE\x04\x04\x04\x04"
'''

x = b'YELLOW SUBMARINE'
def pkcs_padding(text, block_size):
    length_of_padding = block_size - (len(text) % block_size)
    if length_of_padding == 0:
        length_of_padding = block_size
    padding = bytes([length_of_padding]) * length_of_padding
    return text + padding

# Test it out
print(pkcs_padding(x, 20))
# SOLUTION --> b'YELLOW SUBMARINE\x04\x04\x04\x04'
