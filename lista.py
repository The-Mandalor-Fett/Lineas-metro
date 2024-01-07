import os

# Ruta del directorio
ruta_directorio = r'C:\Users\david\Downloads\Estaciones'

# Obtener la lista de nombres de las carpetas
nombres_carpetas = [nombre for nombre in os.listdir(ruta_directorio) if os.path.isdir(os.path.join(ruta_directorio, nombre))]

# Ruta del archivo de texto para guardar los nombres de las carpetas
ruta_archivo_txt = r'C:\Users\david\Downloads\lista_carpetas.txt'

# Escribir los nombres de las carpetas en el archivo de texto
with open(ruta_archivo_txt, 'w') as archivo:
    for nombre_carpeta in nombres_carpetas:
        archivo.write(nombre_carpeta + '\n')

print("Se ha creado el archivo 'lista_carpetas.txt' con los nombres de las carpetas.")
