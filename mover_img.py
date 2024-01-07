import os
import shutil

# Ruta de la carpeta general "Estaciones"
ruta_estaciones = r'C:\Users\david\Downloads\Estaciones'

# Obtener la lista de carpetas dentro de la carpeta general "Estaciones"
carpetas_estaciones = [nombre for nombre in os.listdir(ruta_estaciones) if
                       os.path.isdir(os.path.join(ruta_estaciones, nombre))]

# Recorrer las carpetas y mover las imágenes de la carpeta "output" a la carpeta principal
for carpeta in carpetas_estaciones:
    ruta_carpeta_output = os.path.join(ruta_estaciones, carpeta, 'output')

    # Verificar si la carpeta "output" existe dentro de la carpeta actual
    if os.path.exists(ruta_carpeta_output):
        archivos_output = os.listdir(ruta_carpeta_output)

        # Mover los archivos de la carpeta "output" a la carpeta principal
        for archivo in archivos_output:
            ruta_archivo_output = os.path.join(ruta_carpeta_output, archivo)
            ruta_destino = os.path.join(ruta_estaciones, carpeta, archivo)
            shutil.move(ruta_archivo_output, ruta_destino)

        # Eliminar la carpeta "output" vacía (opcional)
        os.rmdir(ruta_carpeta_output)
