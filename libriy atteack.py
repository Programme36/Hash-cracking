import hashlib

hashs = "" #Enter hash here

with open("rockyou.txt","r")as rock: #If you have other wordlist, you can change it
    for line in rock:
        line = line.rstrip('\n')
        hashing = hashlib.md5(line.encode()).hexdigest() #you can change hash algoridoms
        '''(eg. sha1, sha3_384, sha384, md5, sha3_512, shake_128, sha256, sha3_224, sha3_256, sha224, blake2b, blake2s, shake_256, sha512)'''
        if hashs == hashing:
            print(line)
