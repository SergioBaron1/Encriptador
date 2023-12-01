import os
import time

inicio = time.time()

# Rutas de archivos
archivo_original = os.path.join(os.getcwd(), './files/lorem.txt')
archivo_cifrado = os.path.join(os.getcwd(), './results_reversed/lorem_cifrado.txt')
archivo_descifrado = os.path.join(os.getcwd(), './results_reversed/lorem_descifrado.txt')

# Leer el archivo original
with open(archivo_original, 'r') as original_file:
    original = original_file.read()

# Crear cadena de caracteres
if original == original.upper():  # Mayúsculas
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
else:
    abc = "abcdefghijklmnñopqrstuvwxyz"  # Minúsculas

# Leer el archivo cifrado
with open(archivo_cifrado, 'r') as cifrado_file:
    cifrado = cifrado_file.read()

# Leer clave de cifrado
ruta_clave=os.path.join(os.getcwd(),'./clave_cesar.key')
with open(ruta_clave,'r') as mykey:
    clave_aleatoria=mykey.read()

clave_aleatoria=int(clave_aleatoria)

# Crear la cadena descifrada
descifrado = ""

# Realizar descifrado
for c in cifrado:
    if c in abc:
        descifrado += abc[(abc.index(c) - clave_aleatoria) % len(abc)]
    else:
        descifrado += c

# Guardar el texto descifrado en un nuevo archivo
target= os.path.join(os.getcwd(),'./results_reversed/lorem_descifrado.txt')

with open(target, 'w') as descifrado_file:
    descifrado_file.write(descifrado)

fin = time.time()
print(fin - inicio)