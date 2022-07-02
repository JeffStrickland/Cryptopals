'''
CRYPTOPALS CHALLENGE 6

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

from subprocess import check_output as run
from base64 import b64decode

a = b'this is a test'
b = b'wokka wokka!!!'

def hamming_distance(a, b):
    distance = 0
    for z in zip(a, b):
        x = z[0] ^ z[1]
        bits = 0
        while (x >0):
            bits += x & 1;
            x >>=1;
        distance += bits
    return distance
# This should return 37
# print(hamming_distance(a, b))
# SOLUTION --> 37, it works

def key_sizes():
  
  start = 2
  end = 40
  return list(range(start, end + 1))

def ascii_to_bytes(text):
  """Convert ASCII text to bytes."""
  return bytearray.fromhex(text.encode('utf-8').hex())

def xor_matching(a, b):
  """XOR two sets of bytes with matching lengths."""
  assert len(a) == len(b), 'attempting to XOR with elements of different lengths'
  return [a[i] ^ b[i] for i, x in enumerate(a)]

def split_chunks(iterable, chunk_size):
  """Split an iterable into chunks of a specified size"""
  chunks = [
    iterable[i:i + chunk_size]
    for i
    in range(0, len(iterable), chunk_size)
    if i < len(iterable) - chunk_size
  ]
  return chunks

def normalized_hamming_distance(text, key_size):
  """Given a key size, compute the normalized hamming distance for two strings."""
  assert key_size < len(text) / 2, 'text is too short to provide two blocks at this key size'
  bytelist = b64decode(text)
  assert isinstance(bytelist, (bytes, bytearray)), 'hamming distance must be calculated with raw bytes'
  # break cipher text into chunks
  chunks = split_chunks(bytelist, key_size) 
  # select two leading blocks
  blocks = [
    bytelist[0:key_size],
    bytelist[key_size:key_size * 2]
  ]
  hamming_distances = [
    [hamming_distance(block, chunk) for chunk in chunks]
    for block
    in blocks
  ][0] 
  # average all Hamming distances
  mean = sum(hamming_distances) / len(hamming_distances)
  # normalize by key size to further constrain deviations in the mean
  normalized = mean / key_size
  return normalized

def smallest(values):
 
  sorted_values = sorted(values, key=lambda x: x.get('distance'))
  return sorted_values[0].get('key_size')

def remote():
  # Experimenting with pulling the text file in remotely
  url = "https://cryptopals.com/static/challenge-data/6.txt"
  return run(['curl', '--silent', url]).decode('ascii')

def find_key_size(text):
  # compute hamming distance
  normalized_hamming_distances = [
    {
      'key_size': key_size,
      'distance': normalized_hamming_distance(text, key_size)
    } 
    for key_size
    in key_sizes()
  ]
  # choose the smallest key size
  keys = smallest(normalized_hamming_distances)
  return keys

def transpose(text, size):
  bytelist = b64decode(text)
  chunks = split_chunks(bytelist, size)
  transposed = list(zip(*chunks))
  return transposed

def xor_single(bytelist, key):
  return [b ^ key for b in bytelist]

def ascii():
  return [chr(x) for x in range(128)]

def detect_key(strings):
  common = list('etaoin shrdlu')
  counts = [
    sum([string.count(character) for character in common])
    for string in strings
  ]
  maximum = max(counts)
  index = counts.index(maximum)
  return chr(index)

def find_xor_key(bytelist):
  xor_bytes = [xor_single(bytelist, ord(character)) for character in ascii()]
  xor_strings = [''.join(list(map(chr, integer))) for integer in xor_bytes]
  key = detect_key(xor_strings)
  return key

def find_vignere_key(text):
  key_size = find_key_size(text)
  transposed_bytes = transpose(text, key_size)
  vignere_key = ''.join([find_xor_key(x) for x in transposed_bytes])
  return vignere_key

def decrypt_vignere(ciphertext, key):
  bytes_text = b64decode(ciphertext)
  bytes_key = ascii_to_bytes(key)
  decrypted_bytes = [b ^ bytes_key[i % len(bytes_key)] for i, b in enumerate(bytes_text)]
  decrypted_characters = [chr(b) for b in decrypted_bytes]
  decrypted_text = ''.join(decrypted_characters)
  return decrypted_text

def main():
  ciphertext = remote()
  key = find_vignere_key(ciphertext)
  message = decrypt_vignere(ciphertext, key)
  print(f'This is the key ---> {key}')
  print(f'This is the decrypted message ---> {message}')

if __name__ == "__main__":
  main()
'''
Solution --->
This is the key ---> Terminator X: Bring the noise
This is the decrypted message ---> I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. 

I'm lettin' my drug kick in 
It controls my mouth and I begin 
To just let it flow, let my concepts go 
My posse's to the side yellin', Go Vanilla Go! 

Smooth 'cause that's the way I will be 
And if you don't give a damn, then 
Why you starin' at me 
So get off 'cause I control the stage 
There's no dissin' allowed 
I'm in my own phase 
The girlies sa y they love me and that is ok 
And I can dance better than any kid n' play 

Stage 2 -- Yea the one ya' wanna listen to 
It's off my head so let the beat play through 
So I can funk it up and make it sound good 
1-2-3 Yo -- Knock on some wood 
For good luck, I like my rhymes atrocious 
Supercalafragilisticexpialidocious 
I'm an effect and that you can bet 
I can take a fly girl and make her wet. 

I'm like Samson -- Samson to Delilah 
There's no denyin', You can try to hang 
But you'll keep tryin' to get my style 
Over and over, practice makes perfect 
But not if you're a loafer. 

You'll get nowhere, no place, no time, no girls 
Soon -- Oh my God, homebody, you probably eat 
Spaghetti with a spoon! Come on and say it! 

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino 
Intoxicating so you stagger like a wino 
So punks stop trying and girl stop cryin' 
Vanilla Ice is sellin' and you people are buyin' 
'Cause why the freaks are jockin' like Crazy Glue 
Movin' and groovin' trying to sing along 
All through the ghetto groovin' this here song 
Now you're amazed by the VIP posse. 

Steppin' so hard like a German Nazi 
Startled by the bases hittin' ground 
There's no trippin' on mine, I'm just gettin' down 
Sparkamatic, I'm hangin' tight like a fanatic 
You trapped me once and I thought that 
You might have it 
So step down and lend me your ear 
'89 in my time! You, '90 is my year. 

You're weakenin' fast, YO! and I can tell it 
Your body's gettin' hot, so, so I can smell it 
So don't be mad and don't be sad 
'Cause the lyrics belong to ICE, You can call me Dad 
You're pitchin' a fit, so step back and endure 
Let the witch doctor, Ice, do the dance to cure 
So come up close and don't be square 
You wanna battle me -- Anytime, anywhere 

You thought that I was weak, Boy, you're dead wrong 
So come on, everybody and sing this song 

Say -- Play that funky music Say, go white boy, go white boy go 
play that funky music Go white boy, go white boy, go 
Lay down and boogie and play that funky music till you die. 

Play that funky music Come on, Come on, let me hear 
Play that funky music white boy you say it, say it 
Play that funky music A little louder now 
Play that funky music, white boy Come on, Come on, Come on 
Play that funky music 
'''