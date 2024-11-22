import sys
import torch
from PIL import Image

import ultralytics
from ultralytics import YOLO

from custom import hardware_check


# 添加系统路径
# sys.path.append("/root/ultralytics")

# 打开图像并获取尺寸
# image = Image.open("/root/github/ultralytics/ultralytics/assets/bus.jpg")
# w, h = image.size
# print(f"w:{w}, h:{h}")

if __name__ == "__main__":
    print(ultralytics.checks())
    
    model = YOLO("custom/cfg/yolo11pose.yaml")
    
    device = "cuda" if hardware_check.check_hardware() else "cpu"
    print(f"using device: {device}")
    data = "custom/cfg/data.yaml"
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