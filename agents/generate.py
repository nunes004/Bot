import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_code(prompt_usuario):
    prompt = f"Você é um programador Python especialista. Gere um código funcional, limpo e comentado para:\n\n{prompt_usuario}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Erro na requisição OpenAI: {str(e)}"
