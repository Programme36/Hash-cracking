import hashlib

a = "hello" #Enter data
convert = hashlib.md5(a.encode()).hexdigest() #Change hash
print(convert)
