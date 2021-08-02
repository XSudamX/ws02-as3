#Following script doesnt work on macOS (also >python3.3) due to
#the included crypt package in macos being different,
#i cant afford a mac so its not my problem -Sudam

#(or use passlib - platform independant package)

import sys
import crypt

#Config
password=sys.argv[1]
hashedValue=crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))
#salt is secure and generated from mksalt in cryptpackage

#Output
print('Value to be hashed :',sys.argv[1])
print('Hashed Value :',hashedValue)
