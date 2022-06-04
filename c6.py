'''
Break repeating-key XOR
It is officially on, now.

This challenge isn't conceptually hard, but it involves actual error-prone coding. The other challenges in this set are there to bring you up to speed. This one is there to qualify you. If you can do this one, you're probably just fine up to Set 6.

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

    Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
    Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:

    this is a test

    and

    wokka wokka!!!

    is 37. Make sure your code agrees before you proceed.
    For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
    The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
    Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
    Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
    Solve each block as if it was single-character XOR. You already have code to do this.
    For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.

This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.
No, that's not a mistake.

We get more tech support questions for this challenge than any of the other ones. We promise, there aren't any blatant errors in this text. In particular: the "wokka wokka!!!" edit distance really is 37.
'''
import distance 
import codecs

def list_from_textfile(file_path):
    with open(file_path) as f:
        base64list = f.readlines()
    byteslist = [bytes(x, "utf-8")for x in base64list]
    byteslist = [x.strip() for x in byteslist]
    return byteslist

byteslist = list_from_textfile('6.txt')

# Test above function --  It should return the text file in a list with strings decoded from base64 to bytes
# print(list_from_textfile('6.txt')) #- it works

'''
def hamming_distance_strings(a, b):
    x = distance.hamming(a.decode(), b.decode()) 
    return x

# Breakdown of the above built in function:
def hamming_distance(string1, string2):
	dist_counter = 0
	for n in range(len(string1)):
		if string1[n] != string2[n]:
			dist_counter += 1
	return dist_counter

# Test of 2 function above
#print(hamming_distance_strings(byteslist[1], byteslist[5]))
#print(hamming_distance(byteslist[1], byteslist[5]))
'''
# Function from challenge 3
def single_xor(y): 
    strings = (''.join(chr(num ^ key) for num in y) for key in range(256)) # Scoring for character frequency to find key
    return (max(strings, key = lambda s: s.count(' '))) # Decrypt message with key

def single_char_xor(input_bytes, char_value):
    """Returns the result of each byte being XOR'd with a single value."""
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes

def get_english_score(input_bytes):
    # From https://en.wikipedia.org/wiki/Letter_frequency
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])

def repeating_key_xor(message_bytes, key):
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes

def decryption(byteslist):
    av_hamming_distances = []
    for keysize in range(2, 41):
        distances = []
        text_chunks = [byteslist[i:i+keysize]for i in range(0, len(byteslist), keysize)]
        while True:
            try:
                text_chunk1 = text_chunks[0]
                text_chunk2 = text_chunks[1]
                distance = distance.hamming(text_chunk1.decode(), text_chunk2.decode())
                distances.append(distance/keysize)
                del text_chunks[0]
                del text_chunks[1]
            except Exception as e:
                break
        result = {
            'key': keysize,
            'avg distance': sum(distances) / len(distances)
            }
        av_hamming_distances.append(result)
    possible_key_lengths = sorted(av_hamming_distances, key=lambda x: x['avg distance'])[:5]
    possible_plaintext = []
    for res in possible_key_lengths:
        key = b''
        for i in range(res['key']):
            block = b''
            for j in range(i, len(byteslist), res['key']):
                block += bytes([byteslist[j]])
            key += bytes([single_xor(block)['key']]) 
        possible_plaintext.append((repeating_key_xor(byteslist, key), key)) 
    return max(possible_plaintext, key=lambda x: get_english_score(x[0]))

def main():
    result, key = decryption(byteslist)
    print("Key: {}\nMessage: {}".format(key, result))

if __name__ == '__main__':
    file_path = 'Desktop/GitHub/Cryptopals/6.txt'
    main()
'''
NOT COMPLETE, NEED TO DEBUG

Traceback (most recent call last):
  File "/Users/computer/Desktop/GitHub/Cryptopals/c6.py", line 141, in <module>
    main()
  File "/Users/computer/Desktop/GitHub/Cryptopals/c6.py", line 136, in main
    result, key = decryption(byteslist)
  File "/Users/computer/Desktop/GitHub/Cryptopals/c6.py", line 120, in decryption
    'avg distance': sum(distances) / len(distances)
ZeroDivisionError: division by zero
'''