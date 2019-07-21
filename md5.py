import hashlib
import sys

f = open(sys.argv[1], 'rb')

data = f.read()
f.close()

s = hashlib.md5(data).hexdigest()

print("MD5: " + s.upper())