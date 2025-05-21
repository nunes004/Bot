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
            "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
            headers=headers,
            json=data,
            timeout=60
        )
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        else:
            return "⚠️ Erro: A resposta da API não contém texto gerado."

    except requests.exceptions.HTTPError as http_err:
        return f"Erro HTTP {response.status_code}: {response.text}"
    except Exception as e:
        return f"Erro na requisição Hugging Face: {str(e)}"
