import Augmentor
import os
import shutil

# Ruta de la carpeta principal
carpeta_general = r'C:\Users\david\Downloads\Estaciones'

# Obtener la lista de carpetas dentro de la carpeta general
carpetas = os.listdir(carpeta_general)

# Iterar sobre cada carpeta
for carpeta in carpetas:
    carpeta_path = os.path.join(carpeta_general, carpeta)

    # Crear un Pipeline de Augmentor para cada carpeta
    pipeline = Augmentor.Pipeline(carpeta_path)

    # Definir operaciones de aumento de datos
    pipeline.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    pipeline.flip_left_right(probability=0.5)
    pipeline.zoom_random(probability=0.5, percentage_area=0.8)

    # Generar 100 imágenes aumentadas
    num_images_to_generate = 100 - len(os.listdir(carpeta_path))
    pipeline.sample(num_images_to_generate)

    # Mover las imágenes aumentadas a la carpeta original
    imagenes_generadas = [f for f in os.listdir(carpeta_path) if f.startswith('output')]
    for imagen in imagenes_generadas:
        ruta_original = os.path.join(carpeta_path, imagen)
        ruta_destino = os.path.join(carpeta_path, imagen.replace('output_', ''))
        shutil.move(ruta_original, ruta_destino)
