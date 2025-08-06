# Projeto: Galeria de Imagens da NASA APOD (Astronomy Picture of the Day)

![Screenshot da Galeria de Imagens](https://i.imgur.com/your-image-url-here.png)

## 📖 Sobre o Projeto

Este projeto consiste na criação de uma aplicação web simples em Python com o objetivo de consumir e exibir dados de uma API externa. A API escolhida para este exercício é a **NASA APOD**, que fornece diariamente uma imagem e uma breve descrição de um fenômeno astronômico.

A aplicação foi desenvolvida como uma prova de conceito para demonstrar o consumo de APIs RESTful, manipulação de dados JSON, renderização de templates HTML e a adição de funcionalidades como tradução e interação com o sistema do usuário.

## ✨ Funcionalidades

* **Consumo da API da NASA:** Faz requisições para a API oficial da NASA APOD para obter as 10 imagens astronômicas mais recentes.
* **Processamento de Dados:** Manipula a resposta JSON da API para extrair URLs, títulos e descrições das imagens.
* **Geração de Galeria Dinâmica:** Usa o framework Flask para renderizar uma página HTML que exibe as imagens em uma galeria interativa.
* **Tradução Automática:** A descrição das imagens é traduzida do inglês para o português de forma programática.
* **Download:** Permite que o usuário baixe a imagem em alta definição.
* **Abertura Automática do Navegador:** Abre a página da aplicação no navegador padrão do sistema assim que o servidor é iniciado, melhorando a experiência do usuário.

## 🛠 Tecnologias e Ferramentas

* **Python 3:** Linguagem principal de desenvolvimento.
* **Flask:** Framework web para construir o servidor da aplicação.
* **Requests:** Biblioteca para simplificar as requisições HTTP para a API.
* **python-dotenv:** Ferramenta para carregar variáveis de ambiente a partir de um arquivo `.env` e proteger a chave de API.
* **googletrans:** Biblioteca utilizada para a tradução dos textos.
* **webbrowser:** Módulo nativo do Python para interação com o navegador do sistema.
* **threading:** Módulo nativo do Python para lidar com a execução de tarefas em paralelo (iniciar servidor e abrir navegador).

## 🚀 Como Rodar o Projeto

### Pré-requisitos

1.  **Python 3** e **pip** instalados.
2.  Uma **chave de API da NASA**, que pode ser obtida gratuitamente em [https://api.nasa.gov/](https://api.nasa.gov/).

### Passo a Passo

1.  **Navegue até a pasta do projeto** no seu terminal.
2.  **Ative o ambiente virtual** (caso não esteja ativo):
    ```bash
    # Para Windows
    venv\Scripts\activate
    ```
3.  **Instale as dependências** do projeto:
    ```bash
    pip install Flask requests python-dotenv googletrans==4.0.0-rc1
    ```
4.  **Crie o arquivo `.env`** no diretório principal do projeto e adicione sua chave de API:
    ```
    # Conteúdo do arquivo .env
    NASA_API_KEY="SUA_CHAVE_AQUI"
    ```
    Substitua `SUA_CHAVE_AQUI` pela sua chave real da NASA.
5.  **Execute a aplicação:**
    ```bash
    python app.py
    ```
    O servidor será iniciado, e o navegador abrirá automaticamente a galeria de imagens. Para encerrar o servidor, pressione `Ctrl + C` no terminal.

---
_Este projeto foi criado como um exercício prático de consumo de API._