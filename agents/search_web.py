import requests
from bs4 import BeautifulSoup
import os

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
}

def buscar_e_resumir(termo):
    try:
        url = f"https://html.duckduckgo.com/html/?q={termo}"
        response = requests.get(url, timeout=20)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", class_="result__a", limit=3)
        textos = "\n\n".join(link.text for link in links)

        prompt = f"Com base nos seguintes resultados da web, escreva um resumo útil:\n\n{textos}"

        data = {
            "inputs": prompt,
            "options": {
                "wait_for_model": True
            }
        }

        resposta = requests.post(
            "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
            headers=headers,
            json=data,
            timeout=60
        )

        return resposta.json()[0]["generated_text"]

    except Exception as e:
        return f"Erro na busca ou IA: {str(e)}"
