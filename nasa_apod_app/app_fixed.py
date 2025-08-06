# Rota para segunda tela de detalhes (deve ficar após a criação do app)

# arquivo: nasa_apod_app/app.py - Versão com fix para segunda-feira

import os
import requests
import threading
import webbrowser
import datetime
import time
from flask import Flask, render_template, request
from dotenv import load_dotenv

# 1. Carregando a chave de API do arquivo .env
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

# 2. Inicializando a aplicação Flask
app = Flask(__name__)

# Função para obter imagens com retry e fallback
def get_nasa_images_with_retry(retries=3):
    """Obtém imagens da NASA com retry automático e fallback para segunda-feira"""
    for attempt in range(retries):
        try:
            nasa_api_url = "https://api.nasa.gov/planetary/apod"
            params = {
                "api_key": NASA_API_KEY,
                "count": 50
            }
            
            # Log para debug de segunda-feira
            current_date = datetime.datetime.now()
            print(f"[NASA-APOD] Tentativa {attempt + 1} - Data: {current_date.strftime('%Y-%m-%d %A')}")
            
            response = requests.get(nasa_api_url, params=params, timeout=15)
            response.raise_for_status()
            
            apods = response.json()
            
            # Filtrar apenas imagens válidas
            valid_apods = [apod for apod in apods if apod.get('media_type') == 'image' and apod.get('url')]
            
            if valid_apods:
                print(f"[NASA-APOD] Sucesso: {len(valid_apods)} imagens obtidas")
                return valid_apods
            else:
                print("[NASA-APOD] Nenhuma imagem válida, usando fallback")
                return get_fallback_images()
                
        except Exception as e:
            print(f"[NASA-APOD] Erro tentativa {attempt + 1}: {e}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    
    return get_fallback_images()

def get_fallback_images():
    """Retorna imagens de fallback quando a API falha"""
    print("[NASA-APOD] Usando imagens de fallback")
    today = datetime.datetime.now()
    fallback_images = []
    
    for i in range(50):
        # Gerar URLs consistentes baseadas na data
        seed = abs(hash(f"{today.strftime('%Y%m%d')}{i}")) % 1000
        fallback_images.append({
            'url': f'https://source.unsplash.com/800x600/?space,astronomy,galaxy&sig={seed}',
            'title': f'Imagem Astronômica {i+1}',
            'explanation': 'Imagem de fallback gerada automaticamente sobre astronomia.',
            'date': today.strftime('%Y-%m-%d'),
            'media_type': 'image',
            'copyright': 'NASA/Unsplash'
        })
    
    return fallback_images

# 3. Rota principal com retry automático
@app.route('/')
def index():
    try:
        apods = get_nasa_images_with_retry()
        
        # Log especial para segunda-feira
        today = datetime.datetime.now()
        if today.weekday() == 0:  # Segunda-feira
            print(f"[NASA-APOD] Segunda-feira - {len(apods)} imagens carregadas")
        
    except Exception as e:
        print(f"[NASA-APOD] Erro crítico: {e}")
        apods = get_fallback_images()

    return render_template('index.html', apods=apods)

@app.route('/detalhes')
def detalhes():
    imagens_extra = []
    today = datetime.datetime.now()
    
    # Gerar imagens extras com base na data para consistência
    for i in range(1, 501):
        seed = abs(hash(f"{today.strftime('%Y%m%d')}{i}")) % 1000
        imagens_extra.append({
            'url': f'https://source.unsplash.com/800x600/?space,astronomy,galaxy&sig={seed}',
            'titulo': f'Imagem Astronômica {i}',
            'descricao': f'Foto gerada automaticamente sobre astronomia. Número {i}.'
        })
    return render_template('detalhes.html', imagens_extra=imagens_extra)

# 5. Executando a aplicação
if __name__ == '__main__':
    import webbrowser
    import threading
    def abrir_navegador():
        import time
        time.sleep(1)
        webbrowser.open('http://127.0.0.1:5000')
    threading.Thread(target=abrir_navegador).start()
    app.run(debug=True)
