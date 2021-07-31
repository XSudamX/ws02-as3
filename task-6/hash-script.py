#!/usr/bin/python
import sys
import hashlib

#Configs
iteration=200000
byteSize='Km5d5ivMy8iexuHcZrsD'

#Encoding
salt=byteSize.encode('utf-8')
password=sys.argv[1].encode('utf-8')

#Hashing
hashedValue=hashlib.pbkdf2_hmac('sha512',bytes(password),bytes(salt),iteration)
hashedValue=hashedValue.hex()

#Output
print('Value to be hashed :',sys.argv[1])
print('Hashed Value :',hashedValue)
