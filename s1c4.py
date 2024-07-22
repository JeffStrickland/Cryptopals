'''
CRYPTOPALS CHALLENGE 4

Detect single-character XOR

One of the 60-character strings in this file has been encrypted by single-character XOR.
Find it.
(Your code from #3 should help.)
'''

from binascii import unhexlify
import re

# Function that decrypts the message: carried over from challege 3
def single_xor(x):
    strings = (''.join(chr(num ^ key) for num in x) for key in range(256)) # Scoring for character frequency to find key
    return (max(strings, key = lambda s: s.count(' '))) # Decrypt message with key

# Function reads text file, manipulateds data, calls the function above to decode it,  then returns the plain text solution
def evaluate_file():    
    with open('Desktop/4.txt') as f:
        templist = f.readlines()
    y = [i.strip() for i in templist]
    x = [unhexlify(i) for i in y]
    z = [single_xor(i) for i in x]
    for i in z:
        if bool(re.match('[a-zA-Z\s]+$', i)) == True:
            return(i)
        else:
            pass


# Test it out
print(f'SOLUTION --> {evaluate_file()}')

'''
The above prints out:

SOLUTION --> Now that the party is jumping
'''