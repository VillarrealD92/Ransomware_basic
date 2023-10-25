#!usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "encrypt_basic" or file == "Onekey" or file == "decrypt_basic.py":
            continue
    if os.path.isfile(file):
            files.append(file)

print(files)

with open("OneKey.key", "rb") as key:
    secretkey = key.read()


password = "doggies"

user_password = input("Enter the password\n")

if user_password == password:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(password).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)



print("FILES DECRYPTED, love doggies\n")