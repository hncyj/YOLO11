import sys
import torch
from PIL import Image

import ultralytics
from ultralytics import YOLO


# sys.path.append("/root/ultralytics")

# image = Image.open("/root/github/ultralytics/ultralytics/assets/bus.jpg")
# w, h = image.size
# print(f"w:{w}, h:{h}")

if __name__ == "__main__":
    print(ultralytics.checks())
    
    model = YOLO("custom/cfg/yolo11pose.yaml")
    
    device = "cuda" if torch.cuda.is_available else "cpu"
    data = "custom/cfg/data1cls.yaml"
    save_dir="./runs"
    
    model.train(
        data=data,
        batch=32,
        epochs=300,
        imgsz=640,
        device=device,
        workers=16,
        optimizer="Adam",
        lr0=0.05,
        patience=100,
        save_dir=save_dir
    )
    