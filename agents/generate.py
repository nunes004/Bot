import requests
import os

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
}

def generate_code(prompt_usuario):
    prompt = f"Você é um programador Python especialista. Gere um código funcional, limpo e comentado para:\n\n{prompt_usuario}"

    data = {
        "inputs": prompt,
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

        if response.status_code != 200:
            return f"Erro Hugging Face: {response.status_code} - {response.text}"

        try:
            json_data = response.json()
            if not json_data or "generated_text" not in json_data[0]:
                return f"Resposta inesperada: {json_data}"
            return json_data[0]["generated_text"]

        except Exception as e:
            return f"Erro ao interpretar resposta: {str(e)} - Conteúdo bruto: {response.text}"

    except Exception as e:
        return f"Erro na requisição Hugging Face: {str(e)}"
