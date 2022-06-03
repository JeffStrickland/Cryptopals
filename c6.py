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

def hamming_distance_strings(a, b):
    x = distance.hamming(a.decode(), b.decode()) 
    return x
'''
# Breakdown of the above built in function:
def hamming_distance(string1, string2):
	dist_counter = 0
	for n in range(len(string1)):
		if string1[n] != string2[n]:
			dist_counter += 1
	return dist_counter
'''
# Test of 2 function above
#print(hamming_distance_strings(byteslist[1], byteslist[5]))
#print(hamming_distance(byteslist[1], byteslist[5]))

def decryption(byteslist):
    av_hamming_distances = []
    for key in range(2, 41):
        distances = []
        text_chunks = [byteslist.decode()[i:i+key]for i in range(0, len(byteslist.decode()), key)]
        while true:
            try:
                text_chunk1 = text_chunks[0]
                text_chunk2 = text_chunks[1]
                distance = distance.hamming(text_chunk1.decode(), text_chunk2.decode())

'''
if __name__ == '__main__':
    file_path = 'Desktop/GitHub/Cryptopals/6.txt'
    main()
'''