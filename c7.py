'''
AES in ECB mode

The Base64-encoded content in this file has been encrypted via AES-128 in ECB mode under the key

"YELLOW SUBMARINE".

(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).

Decrypt it. You know the key, after all.

Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.
Do this with code.

You can obviously decrypt this using the OpenSSL command-line tool, but we're having you get ECB working in code for a reason. You'll need it a lot later on, and not just for attacking ECB.
'''
	
from Crypto.Cipher import AES
import base64

# If your key is encoded in any manner, decode to bytes
key = "YELLOW SUBMARINE"

# Preserve your master encrypted file
# Create new file
# Fill it with the encrypted text decoded to bytes
'''def base64_bytes(file):
    f = open(f'Decrypted{file}', 'x') # Create new file
    encrypted = file
    decrypted = (f'Decrypted{file}')
    with open(encrypted, 'r') as f1, open(decrypted, 'a') as f2: # Open both files
        x = f1.readlines()
        y = [(base64.b64decode(i)) for i in x] # Decode base64 to bytes
        for i in y:                            # Write decoded strings to new file
            f2.write(str(i))
            f2.write('\n')
'''
# It works, don't screw it up
def base64_bytes(file):
    encrypted = file
    with open(encrypted, 'r') as f1:
        x = f1.readlines()
    y = [(base64.b64decode(i)) for i in x] 
    return y   

decipher = AES.new(key, AES.MODE_ECB)
x = base64_bytes('7.txt')
y = [(len(i) for i in x)]
print(y)
#print(decipher.decrypt(x))

#z =[decipher.decrypt(i) for i in x]
#z = z[0: len(z)//16]
#print(z)

