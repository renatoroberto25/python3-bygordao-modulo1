################################
##############001###############
################################
"""
import os

mensagens=[]

nome=input("Nome: ")

while True:
    #limpando terminal
    os.system('clear')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    print("#######################################")

    #obtendo as mensagens:
    texto=input("\nmensagem: ")
    if texto=="fim":
        break
    #adicionando a mensagem a lista
    mensagens.append({
        "nome":nome,
        "texto":texto
    })

"""
################################
##############002###############
################################
#agora usando tk inter como frontend
import tkinter as tk
from tkinter import scrolledtext

# Função para enviar mensagens
def enviar_mensagem():
    texto = input_entry.get()
    if texto == "fim":
        janela.destroy()  # Fecha a janela se "fim" for digitado
    else:
        mensagem_formatada = f"{nome_entry.get()} - {texto}\n"
        mensagens_box.insert(tk.END, mensagem_formatada)
        mensagens_box.tag_configure("formato", background="#282A36", foreground="#8BE9FD")
        mensagens_box.tag_add("formato", tk.END + "-1c linestart", tk.END + "-1c lineend")
        input_entry.delete(0, tk.END)  # Limpa a entrada após enviar a mensagem

# Configuração inicial
mensagens = []

# Criando a janela principal
janela = tk.Tk()
janela.title("Chat")

# Entrada para o nome
nome_label = tk.Label(janela, text="Nome:", background="#282A36", foreground="#8BE9FD")
nome_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

nome_entry = tk.Entry(janela, width=30, background="#282A36", foreground="#8BE9FD")
nome_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Caixa de texto para exibir mensagens
mensagens_box = tk.Text(janela, wrap=tk.WORD, width=40, height=10, background="#282A36", foreground="#8BE9FD")
mensagens_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Rótulo e entrada para enviar mensagens
input_label = tk.Label(janela, text="Mensagem:", background="#282A36", foreground="#8BE9FD")
input_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

input_entry = tk.Entry(janela, width=30, background="#282A36", foreground="#8BE9FD")
input_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Botão para enviar mensagem
enviar_button = tk.Button(janela, text="Enviar", command=enviar_mensagem, background="#282A36", foreground="#8BE9FD")
enviar_button.grid(row=3, column=0, columnspan=2, pady=10)

# Executando a janela
janela.mainloop()
