'''
CRYPTOPALS CHALLENGE 8


Detect AES in ECB mode

In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
'''

from Crypto.Cipher.AES import block_size

# Separate file into equal chunks, count the number of repetitions
def look_for_repititions(file):
    chunks = [file[i:i + block_size] for i in range(0, len(file), block_size)]
    number_repititions = len(chunks) - len(set(chunks))
    return number_repititions

# Returns the line with the most repetition as this is the one most likely encrypted
def detect_encryption(file):
    best = (-1, 0)
    for i in range(len(file)):
        reps =  look_for_repititions(file[i])
        best = max(best, (i, reps), key = lambda t: t[1])
    return best


def main():
    file = [bytes.fromhex(line.strip()) for line in open("8.txt")]
    result = detect_encryption(file)
    get_line = open('8.txt')
    encrypted_line = get_line.readlines()
    print(f'SOLUTION --> Position {result[0]} is the encrypted text.  It contains {result[1]} repetitions.')
    print(encrypted_line[result[0]])


if __name__ == "__main__":
    main()

# SOLUTION --> Position 132 is the encrypted text.  It contains 3 repetitions.
# d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641db
# f9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5
# a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4
# fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a