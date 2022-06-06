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