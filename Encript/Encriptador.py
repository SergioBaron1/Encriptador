from cryptography.fernet import Fernet
import os

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
archivo_grades = os.path.join(os.getcwd(),'titanic.csv')

#Encriptar el contenido del archivo
with open(archivo_grades,'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

#Guardar el archivo encriptado
with open ('enc_titanic.csv','wb') as encrypted_file:
    encrypted_file.write(encrypted)


