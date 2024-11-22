import torch

def check_hardware():
    print(f"========== Hardware check ==========")
    if torch.cuda.is_available():
        device = torch.device("cuda")
        gpu_name = torch.cuda.get_device_name(device)
        print(f"Using GPU: {gpu_name}")
        return True
    else:
        print("Using CPU")
        return False