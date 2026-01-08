# 📧 Email Sender API with Python

API desenvolvida em Python utilizando Flask para envio automático de e-mails via SMTP (Gmail), com validação de dados, logs e boas práticas de segurança.

## 🚀 Funcionalidades
- Envio automático de e-mails
- API REST com Flask
- Validação de e-mail antes do envio
- Logs de envio com data e hora
- Uso de variáveis de ambiente (.env) para segurança
- Estrutura de projeto organizada

## 🛠️ Tecnologias Utilizadas
- Python
- Flask
- SMTP (Gmail)
- python-dotenv

## 📂 Estrutura do Projeto

email_sender/
│
├── app.py
├── enviar_email.py
├── logs.txt
├── .env
├── .gitignore
├── requirements.txt
└── README.md


## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/V-coder-cmd/mensagem_email.git

2️⃣ Instale as dependências

pip install -r requirements.txt

3️⃣ Configure o arquivo .env

EMAIL_REMETENTE=seuemail@gmail.com
SENHA_APP=sua_senha_de_app

4️⃣ Execute a API

python app.py

A API ficará disponível em:

http://127.0.0.1:5000

📮 Endpoint Disponível
POST /enviar

Envia um e-mail para o endereço informado.

Body (JSON):

{
  "email": "destinatario@gmail.com"
}


Resposta de sucesso:

{
  "status": "Email enviado com sucesso!"
}

📌 Observações

Projeto desenvolvido para fins de estudo e portfólio, com foco em boas práticas de backend, automação e organização de código.
