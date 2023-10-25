#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypt_basic.py" or file == "OneKey.key" or file == "decrypt_basic.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("OneKey.key", "rb") as key:
    secret_key = key.read()

fernet = Fernet(secret_key)

user_password = input("Enter the password\n")

if user_password == "doggies":  
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = fernet.decrypt(contents)  
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

    print("FILES DECRYPTED, love doggies\n")
else:
    print("Invalid password. Decryption failed.\n")