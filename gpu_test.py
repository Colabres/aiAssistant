from llama_cpp import Llama


llm = Llama(
    model_path="models/llm/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",  # adjust path
    n_gpu_layers=-1,  # 🔥 THIS IS WHAT ENABLES GPU
    n_ctx=2048,
    verbose=True
)

output = llm("How do I know if you are using GPU?", max_tokens=64)
print(output["choices"][0]["text"])
# import torch
# print("CUDA available:", torch.cuda.is_available())
# print("CUDA device count:", torch.cuda.device_count())
# print("CUDA device name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "N/A")