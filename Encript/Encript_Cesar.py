import os
import time
import random 

inicio=time.time()

archivo= os.path.join(os.getcwd(),'./files/lorem.txt')
with open(archivo,'r') as original_file:
    original = original_file.read()

#Crear cadena de caracteres

if original==original.upper(): #Mayusculas
    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
    abc="abcdefghijklmnñopqrstuvwxyz" #Minusculas

#Definimos valor de desplazamiento y lo guardamos en un archivo
clave_aleatoria = random.randint(3,10)
clave_aleatoria1=str(clave_aleatoria)
ruta_clave=os.path.join(os.getcwd(),'./clave_cesar.key')
with open (ruta_clave,'w') as clave:
    clave.write(clave_aleatoria1)

#Creamos la cadena 
cifrad=""

#Realizamos cifrado

for c in original:
    if c in abc:
        cifrad += abc[(abc.index(c)+clave_aleatoria)%(len(abc))]
    
    else:
        cifrad += c

#Visualizar texto final
target = os.path.join(os.getcwd(),'./results_reversed/lorem_cifrado.txt')
with open(target,'w') as encrypted_file:
    encrypted_file.write(cifrad)

fin=time.time()
print(fin-inicio)