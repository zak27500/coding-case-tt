from llama_cpp import Llama


class QWENClient:
    def __init__(self) -> None:
        self._llm = Llama(
            model_path="models/qwen2.5-1.5b-instruct-q4_k_m.gguf",
            n_ctx=30000,
            n_threads=6,
            verbose=False,
        )

    async def complete(self, prompt: str) -> str:
        reponse = self._llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return reponse["choices"][0]["message"]["content"]
