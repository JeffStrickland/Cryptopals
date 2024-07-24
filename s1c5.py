'''
CRYPTOPALS CHALLENGE 5

Implement repeating-key XOR

Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
'''

# Function encrypts text with key provided using method: repeating XOR
def encrypt_repeating_key_xor(text, key):
    xor_encoded = []
    for i in range(0, len(text)):
        xor_encoded.append(text[i] ^ key[i % (len(key))])
    return bytes(xor_encoded)

# Pass your chosen text and key into the function, print solution in hex
def main():
    text = bytes("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal", "UTF-8")
    key = bytes("ICE", "UTF-8")
    print(f'SOLUTION --> {(encrypt_repeating_key_xor(text, key)).hex()}')

if __name__ == '__main__':
    main()

# So what is the result ?
# SOLUTION --> 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343
#              c2a26226324272765272a282b2f20690a652e2c652a3124333a653e
#              2b2027630c692b20283165286326302e27282f