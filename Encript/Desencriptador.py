from cryptography.fernet import Fernet
import os
import time

inicio=time.time()

with open('mykey.key','rb') as mykey:
    key=mykey.read()
print(key)

f = Fernet(key)

#Lee el archivo encriptado y lo decifra
ruta_archivo_encriptado=os.path.join(os.getcwd(),'../results/enc_titanic.csv')

with open(ruta_archivo_encriptado,'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

#Crea un nuevo archivo decifrado 
target = os.path.join(os.getcwd(),'../results_reversed/dec_titanic.csv')
with open(target,'wb') as decrypted_file:
    decrypted_file.write(decrypted)

fin = time.time()

print(fin-inicio)
