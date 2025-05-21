import requests
import os

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
    "Content-Type": "application/json"
}

def generate_code(prompt_usuario):
    prompt = f"Você é um programador Python especialista. Gere um código funcional, limpo e comentado para:\n\n{prompt_usuario}"

    data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7
        },
        "options": {
            "wait_for_model": True
        }
    }

    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/bigcode/starcoder2-7b",
            headers=headers,
            json=data,
            timeout=60
        )

        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif "error" in result:
            return f"Erro Hugging Face: {result['error']}"
        else:
            return "Resposta inesperada da IA."
    except Exception as e:
        return f"Erro na requisição Hugging Face: {str(e)}"
