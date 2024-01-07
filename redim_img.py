import os
from PIL import Image

ruta_estaciones = r'C:\Users\david\Downloads\Estaciones'

def redimensionar_imagenes(ruta_carpeta):
    for carpeta in os.listdir(ruta_carpeta):
        ruta_carpeta_completa = os.path.join(ruta_carpeta, carpeta)
        if os.path.isdir(ruta_carpeta_completa):
            for archivo in os.listdir(ruta_carpeta_completa):
                if archivo.endswith('.png'):
                    ruta_imagen = os.path.join(ruta_carpeta_completa, archivo)
                    try:
                        imagen = Image.open(ruta_imagen)
                        imagen = imagen.resize((640, 640), Image.LANCZOS)
                        imagen.save(ruta_imagen)
                        print(f"Imagen {archivo} redimensionada correctamente.")
                    except Exception as e:
                        print(f"Error al procesar {archivo}: {e}")

redimensionar_imagenes(ruta_estaciones)
