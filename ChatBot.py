import os
from langchain_groq import ChatGroq
# chave da API
api_key = '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'
os.environ['GROQ_API_KEY'] = api_key
# chamada para o chat 
chat = ChatGroq('llama-3.3-70b-versatile')

resposta = chat.invoke('Olá, Modelo! Quem é você? ')
print(resposta)






