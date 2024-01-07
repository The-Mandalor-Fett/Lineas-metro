import torch
from ultralytics import YOLO

print("Esperando")
print("Verificando CUDA: {}".format(torch.cuda.is_available()))
task = "detect"
mode = "train"
model_name = "yolov8m-oiv7.pt"
data_config = "data_custom.yaml"
epochs = 80
patience = 50
batch_size = 2
device = 0
img_size = 640
pretrained = True
optimizer = "Adam"
verbose = True
deterministic = True
dropout = 0.0
val = False
split = "val"
seed = 1610
lr0= 0.01
lrf= 0.01
momentum= 0.937


if __name__ == "__main__":
    model = YOLO(model_name)
    print("Comenzando entrenamiento")
    print(model.names)


    result = model.train(
        data=data_config,
        epochs=epochs,
        device=device,
        patience=patience,
        batch=batch_size,
        imgsz=img_size,
        pretrained=pretrained,
        optimizer=optimizer,
        verbose=verbose,
        seed=seed,
        deterministic=deterministic,
        dropout=dropout,
        val=val,
        split=split,
        lr0=lr0,
        lrf=lrf,
        momentum=momentum
    )
    print("Finalizado entrenamiento")

    result = model.val()
    print(model.names)

