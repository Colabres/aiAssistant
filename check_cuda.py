import torch

print("🔍 CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("🧠 CUDA device:", torch.cuda.get_device_name(0))
    print("📦 cuDNN version:", torch.backends.cudnn.version())
    print("📊 cuBLAS matmul (TF32 enabled):", torch.backends.cuda.matmul.allow_tf32)
else:
    print("❌ CUDA not available in this Python environment.")