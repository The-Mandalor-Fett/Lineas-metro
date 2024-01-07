import os

# Ruta de la carpeta con las imágenes
ruta_carpeta = r'C:\Users\david\Downloads\Estaciones\ecatepec'

# Obtener la lista de archivos en la carpeta
archivos = os.listdir(ruta_carpeta)

# Filtrar solo los archivos de imagen (puedes ajustar la extensión según tus tipos de archivos)
archivos_imagen = [archivo for archivo in archivos if archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]


# Función para renombrar los archivos
def renombrar_archivos(ruta_carpeta, archivos_imagen):
    for i, nombre_archivo in enumerate(archivos_imagen, start=1):
        # Obtener la extensión del archivo
        extension = os.path.splitext(nombre_archivo)[1]
        # Nuevo nombre con el formato deseado (neza_1, neza_2, ...)
        nuevo_nombre = f'ecatepec_{i}{extension}'

        # Ruta antigua y nueva del archivo
        ruta_antigua = os.path.join(ruta_carpeta, nombre_archivo)
        ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)

        # Renombrar el archivo
        os.rename(ruta_antigua, ruta_nueva)
        print(f"Archivo {nombre_archivo} renombrado como {nuevo_nombre}")


# Llamar a la función para renombrar los archivos
renombrar_archivos(ruta_carpeta, archivos_imagen)
