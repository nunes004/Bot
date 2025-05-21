import requests
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def explicar_codigo(codigo):
    prompt = f"Explique detalhadamente o que faz o seguinte código Python:\n\n{codigo}"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=60
        )
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Erro na requisição OpenAI: {str(e)}"
