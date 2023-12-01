from cryptography.fernet import Fernet
import os
import time

inicio = time.time()

#Generar y guardar clave
key = Fernet.generate_key()
with open('mykey.key','wb') as mykey:
    mykey.write(key)

#Leer la clave desde el archivo mykey
with open('mykey.key','rb') as mykey:
    key=mykey.read()
print(key)

#Crear el objeto Fernet
f=Fernet(key)

#Obtener la ruta del archivo grades.csv
archivo = os.path.join(os.getcwd(),'../files/titanic.csv')

#Encriptar el contenido del archivo
with open(archivo,'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

#Guardar el archivo encriptado
target = os.path.join(os.getcwd(),'../results/enc_titanic.csv')
with open (target,'wb') as encrypted_file:
    encrypted_file.write(encrypted)

fin = time.time()

print(fin-inicio)
