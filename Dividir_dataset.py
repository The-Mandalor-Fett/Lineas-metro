import os
import random
from shutil import copyfile

def split_dataset(input_images_dir, input_labels_dir, train_output_dir, test_output_dir, split_ratio=0.8):
    # Obtener la lista de archivos en el directorio de imágenes
    image_files = os.listdir(input_images_dir)

    # Barajar aleatoriamente la lista de archivos
    random.shuffle(image_files)

    # Calcular el número de muestras para el conjunto de entrenamiento
    total_samples = len(image_files)
    train_samples = int(total_samples * split_ratio)

    # Dividir la lista de archivos en conjuntos de entrenamiento y prueba
    train_images = image_files[:train_samples]
    test_images = image_files[train_samples:]

    # Crear directorios de salida si no existen
    os.makedirs(train_output_dir, exist_ok=True)
    os.makedirs(test_output_dir, exist_ok=True)

    # Copiar imágenes al directorio de entrenamiento
    for image in train_images:
        image_path = os.path.join(input_images_dir, image)
        label_path = os.path.join(input_labels_dir, os.path.splitext(image)[0] + ".txt")
        copyfile(image_path, os.path.join(train_output_dir, image))
        copyfile(label_path, os.path.join(train_output_dir, os.path.splitext(image)[0] + ".txt"))

    # Copiar imágenes al directorio de prueba
    for image in test_images:
        image_path = os.path.join(input_images_dir, image)
        label_path = os.path.join(input_labels_dir, os.path.splitext(image)[0] + ".txt")
        copyfile(image_path, os.path.join(test_output_dir, image))
        copyfile(label_path, os.path.join(test_output_dir, os.path.splitext(image)[0] + ".txt"))

if __name__ == "__main__":
    input_images_dir = "C:/Users/david/Downloads/yolo-metro/images"  # Reemplaza con la ruta de tu directorio de imágenes
    input_labels_dir = "C:/Users/david/Downloads/yolo-metro/labels"  # Reemplaza con la ruta de tu directorio de etiquetas
    train_output_dir = "C:/Users/david/Downloads/train"  # Directorio de salida para el conjunto de entrenamiento
    test_output_dir = "C:/Users/david/Downloads/val"  # Directorio de salida para el conjunto de prueba

    split_dataset(input_images_dir, input_labels_dir, train_output_dir, test_output_dir)
