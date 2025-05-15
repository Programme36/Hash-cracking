import hashlib
import itertools

var = "" #Enter hash

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$#%^&*()-_+={}[]:;"<>?/| '

length = 1 #set length

for line in itertools.product(characters, repeat = length):
        a = ''.join(line)
        b = hashlib.md5(a.encode()).hexdigest() #change hash type        
        if b == var:
                print(a)
                break
