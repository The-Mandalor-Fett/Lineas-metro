import os
import numpy as np
from PIL import Image
from imgaug import augmenters as iaa

# Ruta de la carpeta donde están las imágenes
ruta_carpeta = "C:/Users/david/Downloads/Iconos/Iconos"

# Definir las transformaciones de data augmentation
seq = iaa.Sequential([
    # Puedes agregar aquí las transformaciones que desees
    iaa.Fliplr(0.5),  # Volteo horizontal
    iaa.Affine(rotate=(-45, 45))  # Rotación
])

# Iterar sobre cada carpeta L1-1 a L1-20
for i in range(1, 21):
    carpeta_actual = f"L1-{i}"
    ruta_carpeta_actual = os.path.join(ruta_carpeta, carpeta_actual)

    # Verificar si la carpeta existe
    if os.path.exists(ruta_carpeta_actual):
        # Obtener la lista de archivos en la carpeta
        archivos = os.listdir(ruta_carpeta_actual)

        # Iterar sobre cada archivo en la carpeta
        for archivo in archivos:
            if archivo.endswith(".jpg"):  # Verificar que el archivo sea una imagen
                # Cargar la imagen
                imagen = Image.open(os.path.join(ruta_carpeta_actual, archivo))
                imagen = imagen.convert("RGB")  # Convertir la imagen a modo RGB

                # Aplicar transformaciones y guardar nuevas imágenes
                for j in range(1, 50):
                    imagen_array = np.array(imagen)  # Convertir la imagen a un arreglo NumPy
                    imagen_aug = seq.augment_image(imagen_array)
                    imagen_aug = Image.fromarray(imagen_aug)  # Convertir de nuevo a imagen PIL
                    nombre, extension = os.path.splitext(archivo)
                    nueva_ruta = os.path.join(ruta_carpeta_actual, f"{nombre}_{j}{extension}")
                    imagen_aug.save(nueva_ruta)
