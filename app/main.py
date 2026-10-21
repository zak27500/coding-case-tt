from llama_cpp import Llama

if __name__ == "__main__":
    llm = Llama(
        model_path="models/qwen2.5-1.5b-instruct-q4_k_m.gguf",
        n_ctx=12000,
        n_threads=6,
        verbose=False,
    )
    out = llm.create_chat_completion(
        messages=[{"role": "user", "content": "Dis bonjour en une phrase."}],
        temperature=0,
    )
    assert isinstance(out, dict)
    print(out["choices"][0]["message"]["content"])
