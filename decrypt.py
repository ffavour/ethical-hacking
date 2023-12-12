import os
import subprocess
from cryptography.fernet import Fernet


def main():
    files = []

    # trova i file nella directory
    for file in os.listdir():
        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        if os.path.isfile(file):
            files.append(file)
    print(files)

    with open("thekey.key", "rb") as key:
        secretKey = key.read()

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
            contents_dencrypted = Fernet(secretKey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_dencrypted)


if __name__ == '__main__':
    main()
