#!/usr/bin/python
import sys
import hashlib
import os

#Configs
iteration=200000

#Encoding
password=sys.argv[1].encode('utf-8')

#Hashing
hashedValue=hashlib.pbkdf2_hmac('sha512',bytes(password),os.urandom(16),iteration)
hashedValue=hashedValue.hex()

#Output
print('Value to be hashed :',sys.argv[1])
print('Hashed Value :',hashedValue)
