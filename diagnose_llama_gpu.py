from llama_cpp import Llama

llm = Llama(model_path="models/llm/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf", n_gpu_layers=1)
# llm = Llama(
#     model_path="models/llm/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",  # Adjust if needed
#     n_gpu_layers=-1,
#     verbose=True,  # This will show GPU vs CPU usage
# )

response = llm("Hello!", max_tokens=10)
print("Response:", response["choices"][0]["text"])
# import platform
# print(platform.architecture())