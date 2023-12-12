import os
from cryptography.fernet import Fernet


key = "la chiave in binario"


def decrypt_directory(directory_path):

    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)

        if os.path.isfile(file_path):
            with open(file_path, "rb") as thefile:
                contents = thefile.read()
                contents_decrypted = Fernet(key).decrypt(contents)
            with open(file_path, "wb") as thefile:
                thefile.write(contents_decrypted)

        elif os.path.isdir(file_path):
            print(f"Oh, una cartella: {file_path}")
            decrypt_directory(file_path)

    print("Fatto!")


def main():
    directory_path = "."  # percorso della directory da decrittografare
    decrypt_directory(directory_path)


if __name__ == '__main__':
    main()
