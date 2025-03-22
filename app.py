import os
from langchain_groq import ChatGroq

# Configuração da chave da API do Groq
api_key = 'SUA CHAVE DA API DO GROQ AQUI' 
os.environ['GROQ_API_KEY'] = api_key

# Inicialização do chat, e passando o modelo que será utilizado
chat = ChatGroq(model_name='llama-3.3-70b-versatile')

print('Bem-vindo ao chatbot')
message = []
while True:
    user_input = input("Você: ")
    if user_input.lower() == 'sair':
        break
    message.append(user_input)
    resposta = chat.invoke(user_input)
    print(resposta.content)
