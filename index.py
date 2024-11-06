import os
from groq import Groq

#defina a chave
os.environ["GROQ_API_KEY"] = "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"

client = Groq(
    api_key=os.environ.get("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"),
)

#inicializa a lista de mensagens para manter o contexto da conversa
messages=[]

while True:
    usuario = input("digite uma mensagem ou 'sair'' para encerrar: ")

    if usuario.lower() == 'sair'
    print("conversa encerrada.")
    break

#adiciona a mensagem do usuário á lista de mensagens
messages.append({"role": "user", "content": usuario})

chat_completion = client.chat.completion.creat(
 messages=messages,
 model="LLama-3.1-70b-versatile",
)

resposta = chat.completion.choices[0].messages.content
print("resposta",resposta)

#adiciona a resposta do assistente á lista de de mensagens para manter o contexto
messages.append({"role": "user", "content": resposta})