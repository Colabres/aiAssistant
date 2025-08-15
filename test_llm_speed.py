from llama_cpp import Llama

llm = Llama(
    model_path="models/llm/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",  # adjust if needed
    n_gpu_layers=-1,
    n_ctx=2048
)

output = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hi"}
    ],
    temperature=0.6,
    top_p=0.9,
    max_tokens=32,
    stream=False
)

print(output["choices"][0]["message"]["content"])