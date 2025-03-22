🤖 Chatbot com Groq e LangChain
Este projeto implementa um chatbot interativo de linha de comando utilizando a API do Groq através da biblioteca LangChain. O chatbot permite conversar com o modelo de linguagem LLaMA 3.3 70B Versatile.

📝 Descrição
O código cria uma interface de chat simples no terminal que permite ao usuário interagir com o modelo de linguagem avançado da Groq. O usuário pode digitar mensagens e receber respostas geradas pelo modelo LLaMA 3.3 70B Versatile em tempo real.

✨ Algumas Funcionalidades

💬 Interface de chat interativa via terminal
🔌 Integração com o modelo LLaMA 3.3 70B Versatile da Groq
🚪 Comando "sair" para encerrar a conversa

📋 Requisitos
🐍 Python 3.6+

📚 Bibliotecas:
langchain-groq
os (biblioteca padrão)
🔑 Chave de API do Groq

🚀 Instalação
Clone este repositório ou crie um novo arquivo Python
Instale as dependências necessárias:
pip install langchain-groq

⚙️ Configuração
Antes de executar o código, você precisa obter uma chave de API do Groq:

Crie uma conta em Groq
Gere uma chave de API no console
Substitua a chave no código ou configure como variável de ambiente

🎮 Como usar
Execute o script Python:
python chatbot.py

Após iniciar o programa:
Digite suas mensagens após o prompt "Você: "
O modelo responderá a cada mensagem
Para encerrar a conversa, digite "sair"

chatbot.py
🔒 Segurança
Importante: Nunca compartilhe sua chave de API em repositórios públicos. No código de exemplo, a chave está exposta apenas para fins didáticos. Em um ambiente de produção, considere:

🔐 Usar variáveis de ambiente
📄 Armazenar a chave em um arquivo de configuração não versionado (.env)
🛡️ Utilizar serviços de gerenciamento de segredos
🔮 Melhorias possíveis
📊 Implementar histórico de conversas persistente
🖥️ Adicionar interface gráfica
🎛️ Incluir opções de configuração para o modelo (temperatura, top_p, etc.)
🛠️ Implementar tratamento de erros para falhas de conexão
💾 Adicionar funcionalidades como exportar a conversa para um arquivo
📚 Recursos adicionais
📖 Documentação da LangChain
🔍 API do Groq


📜 Licença
Este projeto está sob a licença MIT.
