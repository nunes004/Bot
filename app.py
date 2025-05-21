# Estrutura inicial do projeto Flask + IA para Render.com

# === app.py ===
from flask import Flask, request, render_template, jsonify
from agents import generate, fix, explain, search_web
import json
import os

app = Flask(__name__)

MEMORY_FILE = 'memory/memoria.json'

# Carrega ou cria memória
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, 'w') as f:
        json.dump({}, f)

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f)

def load_memory():
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    memory = load_memory()
    
    # Decide ação com base em palavras-chave simples (você pode melhorar isso com IA depois)
    if 'corrige' in user_input:
        response = fix.fix_code(user_input)
    elif 'explica' in user_input:
        response = explain.explain_code(user_input)
    elif 'busca' in user_input or 'pesquisa' in user_input:
        response = search_web.search(user_input)
    else:
        response = generate.generate_code(user_input)

    memory['ultima_interacao'] = user_input
    save_memory(memory)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
