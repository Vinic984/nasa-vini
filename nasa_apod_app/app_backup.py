# Rota para segunda tela de detalhes (deve ficar após a criação do app)

# arquivo: nasa_apod_app/app.py

import os
import requests
import threading
import webbrowser
from flask import Flask, render_template, request
from dotenv import load_dotenv

# 1. Carregando a chave de API do arquivo .env
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

# 2. Inicializando a aplicação Flask e o tradutor
app = Flask(__name__)

# Função para abrir o navegador
# 3. Definindo a rota principal ('/')
@app.route('/')
def index():
    try:
        nasa_api_url = "https://api.nasa.gov/planetary/apod"
        params = {
            "api_key": NASA_API_KEY,
            "count": 50
        }
        response = requests.get(nasa_api_url, params=params)
        response.raise_for_status()
        
        apods = response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API da NASA: {e}")
        apods = []

    return render_template('index.html', apods=apods)

@app.route('/detalhes')
def detalhes():
    imagens_extra = []
    for i in range(1, 501):
        imagens_extra.append({
            'url': f'https://source.unsplash.com/800x600/?space,star,galaxy,satellite,astronomy&sig={i}',
            'titulo': f'Imagem Astronômica {i}',
            'descricao': f'Foto gerada automaticamente sobre astronomia, estrelas, galáxias ou satélites. Número {i}.'
        })
    return render_template('detalhes.html', imagens_extra=imagens_extra)

# 5. Executando a aplicação
if __name__ == '__main__':
    # 'app.run()' inicia o servidor Flask, que roda no processo principal.
    import webbrowser
    import threading
    def abrir_navegador():
        import time
        time.sleep(1)
        webbrowser.open('http://127.0.0.1:5000')
    threading.Thread(target=abrir_navegador).start()
    app.run(debug=True)