# Classificador de Emails com Integração de IA - 🇧🇷 

Este projeto é uma ferramenta web para classificação de emails, voltada para o setor financeiro. Ele permite que os usuários classifiquem rapidamente emails como **produtivos** ou **improdutivos**, e sugere respostas automaticamente usando IA. Se a IA não estiver disponível ou retornar um erro, um sistema manual de fallback garante a funcionalidade contínua.

Deploy URL: <a href='https://devdantas.pythonanywhere.com/' target='_blank'>devdantas.pythonanywhere.com</a> 

---

## Funcionalidades

- **Autenticação de Usuário**: Tela de login simples com credenciais estáticas para acessar o painel.
- **Classificação com IA**: Utiliza o Google Gemini (gemini-2.0-flash-exp) para classificar emails e gerar respostas sugeridas.
- **Fallback Manual**: Sistema baseado em palavras-chave que gera respostas quando a IA não está disponível.
- **Entrada de Arquivo e Texto**: Suporta tanto a digitação direta do email quanto o upload de arquivos (TXT ou PDF).
- **Painel Interativo**: Processamento em tempo real com indicadores de status e exibição de resultados.
- **Design Responsivo**: Estilizado com TailwindCSS para uma interface limpa e moderna.

---

## Como Usar

1. **Login**: Acesse a aplicação web com as credenciais predefinidas.
2. **Enviar Email**: Cole o conteúdo do email na área de texto ou faça upload de um arquivo `.txt` ou `.pdf`.
3. **Processar**: Clique no botão "Processar". Um spinner indica que o sistema está trabalhando.
4. **Ver Resultados**: O sistema exibe a categoria de classificação e a resposta sugerida. Também informa se a resposta foi gerada manualmente ou pela IA.

---

## Tecnologias

- **Backend**: Python 3.13, Flask
- **Integração com IA**: Google Gemini API
- **Manipulação de PDF**: PyPDF2
- **Processamento de Linguagem Natural**: NLTK
- **Frontend**: HTML, JavaScript, TailwindCSS

---

## Instruções de Setup (Desenvolvimento Local)

1. Clone o repositório.

2. Instale todas as dependências:
    pip install flask PyPDF2 nltk python-dotenv google-generativeai

3. Configure sua chave da IA e credenciais em um arquivo `.env`:\
    GEMINI_API_KEY=sua_chave_aqui\
    LOGIN:seu_login\
    PASSWORD:sua_senha

4. Execute a aplicação Flask:
    python app.py

5. Abra seu navegador em `http://localhost:5000`.

---

## Observações

- A chave da IA é necessária para a funcionalidade completa. Sem ela, o sistema utilizará o mecanismo de resposta manual.
- A autenticação é simples e destinada apenas para fins de demonstração. Em produção, recomenda-se implementar um gerenciamento de usuários mais seguro.

---

## Autor

**Lucas Dantas** – [LinkedIn](https://www.linkedin.com/in/lucas-de-sousa-dantas/)


# Email Classifier with AI Integration - 🇺🇸

This project is a web-based email classification tool designed for the finance sector. It allows users to quickly classify emails as either **productive** or **unproductive**, and automatically suggests responses using AI. If the AI is unavailable or returns an error, a manual fallback system ensures continuous functionality.

Deploy URL: <a href='https://devdantas.pythonanywhere.com/' target='_blank'>devdantas.pythonanywhere.com </a> 
---

## Features

- **User Authentication**: Simple login screen with static credentials to access the dashboard.
- **AI-Powered Classification**: Uses Google Gemini (gemini-2.0-flash-exp) to classify emails and generate suggested responses.
- **Manual Fallback**: A keyword-based system that generates responses if the AI is unavailable.
- **File and Text Input**: Supports both direct text input and file uploads (TXT or PDF).
- **Interactive Dashboard**: Real-time processing with status indicators and results display.
- **Responsive Design**: Styled with TailwindCSS for a clean and modern interface.

---

## Usage

1. **Login**: Access the web application with pre-defined credentials.
2. **Submit Email**: Paste the email content in the textarea or upload a `.txt` or `.pdf` file.
3. **Process**: Click the "Process" button. A spinner indicates that the system is working.
4. **View Results**: The system displays the classification category and a suggested response. It also indicates whether the response was generated manually or by the AI.

---

## Technologies

- **Backend**: Python 3.13, Flask
- **AI Integration**: Google Gemini API
- **PDF Handling**: PyPDF2
- **Natural Language Processing**: NLTK
- **Frontend**: HTML, JavaScript, TailwindCSS

---

## Setup Instructions (Local Development)

1. Clone the repository.

2. Install all dependencies:
    pip install flask PyPDF2 nltk python-dotenv google-generativeai

3. Configure your AI API key and credentials in a `.env` file:\
    GEMINI_API_KEY=your_api_key_here\
    LOGIN:your_login\
    PASSWORD:your_password

4. Run the Flask application:
    python app.py

5. Open your browser at `http://localhost:5000`.

---

## Notes

- The AI key is required for full functionality. Without it, the system will fallback to the manual response mechanism.
- Authentication is simple and meant for demonstration purposes. In a production environment, more secure user management should be implemented.

---

## Author

**Lucas Dantas** – [LinkedIn](https://www.linkedin.com/in/lucas-de-sousa-dantas/)
