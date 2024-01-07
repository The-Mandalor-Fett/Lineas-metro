import os
import shutil

# Ruta principal donde se encuentran las carpetas L1, L2, etc.
ruta_principal = r'C:\Users\david\Downloads\Estaciones'


# Función para obtener la lista de archivos de imagen en una carpeta
def obtener_archivos_de_imagen(ruta_carpeta):
    archivos_imagen = [archivo for archivo in os.listdir(ruta_carpeta) if
                       archivo.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return archivos_imagen


# Recorremos cada carpeta L1, L2, L3, etc.
for carpeta in os.listdir(ruta_principal):
    ruta_carpeta_actual = os.path.join(ruta_principal, carpeta)

    # Verificar si es una carpeta
    if os.path.isdir(ruta_carpeta_actual):
        archivos_imagenes = obtener_archivos_de_imagen(ruta_carpeta_actual)

        # Recorremos los archivos de imagen en la carpeta actual
        for imagen in archivos_imagenes:
            ruta_imagen = os.path.join(ruta_carpeta_actual, imagen)

            # Creamos la carpeta con el nombre de la imagen y movemos la imagen
            carpeta_imagen = os.path.splitext(imagen)[0]  # Nombre de la imagen sin extensión
            ruta_nueva_carpeta = os.path.join(ruta_carpeta_actual, carpeta_imagen)

            # Verificamos si la carpeta de destino existe, si no, la creamos
            if not os.path.exists(ruta_nueva_carpeta):
                os.makedirs(ruta_nueva_carpeta)

            # Movemos la imagen a la nueva carpeta
            shutil.move(ruta_imagen, os.path.join(ruta_nueva_carpeta, imagen))
