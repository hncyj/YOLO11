import onnx
from ultralytics import YOLO

def export_pt_to_onnx(model_path, onnx_path):
    print(f"Loading pt format model at {model_path}...")
    model = YOLO(model_path)
    print(f"Exporting pt format model to ONNX format at {onnx_path}...")
    model.export(format="onnx", opset=12, simplify=True, dynamic=True, imgsz=640)
    print(f"Model exported to {onnx_path}")

def validate_onnx_model(onnx_path):
    print(f"Validating ONNX model at {onnx_path}...")
    onnx_model = onnx.load(onnx_path)
    onnx.checker.check_model(onnx_model)
    print("ONNX model is valid!")
    
def print_onnx_graph(onnx_path):
    print("ONNX model Graph:")
    print(onnx.helper.printable_graph(onnx_path))
