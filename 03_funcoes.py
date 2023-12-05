################################
##############001###############
################################
#   Uso de funções em python DEF
#    Obtém a lista de arquivos em um diretório.
#    Organiza os arquivos por extensão.
#    Exibe os arquivos organizados por extensão.
"""
import os

def obter_lista_arquivos(diretorio='.'):
    try:
        # Obtém a lista de arquivos no diretório
        lista_arquivos = os.listdir(diretorio)
        return lista_arquivos
    except OSError as e:
        print(f"Erro ao acessar o diretório: {e}")
        return []

def organizar_por_extensao(lista_arquivos):
    # Dicionário para armazenar arquivos por extensão
    arquivos_por_extensao = {}

    # Itera sobre a lista de arquivos
    for arquivo in lista_arquivos:
        # Obtém a extensão do arquivo
        _, extensao = os.path.splitext(arquivo)

        # Remove o ponto da extensão (se existir)
        extensao = extensao.lstrip('.')

        # Adiciona o arquivo à lista correspondente à sua extensão
        if extensao in arquivos_por_extensao:
            arquivos_por_extensao[extensao].append(arquivo)
        else:
            arquivos_por_extensao[extensao] = [arquivo]

    return arquivos_por_extensao

def exibir_arquivos_por_extensao(arquivos_por_extensao):
    print("Arquivos organizados por extensão:")
    for extensao, arquivos in arquivos_por_extensao.items():
        print(f".{extensao}: {', '.join(arquivos)}")

def main():
    # Diretório a ser listado
    diretorio_alvo = '.'  # Pode ser substituído por outro diretório desejado

    # Obtém a lista de arquivos no diretório
    lista_arquivos = obter_lista_arquivos(diretorio_alvo)

    # Organiza os arquivos por extensão
    arquivos_por_extensao = organizar_por_extensao(lista_arquivos)

    # Exibe os arquivos organizados por extensão
    exibir_arquivos_por_extensao(arquivos_por_extensao)

if __name__ == "__main__":
    main()
"""

################################
##############002###############
################################
#versão com front end 

import os
import tkinter as tk
from tkinter import scrolledtext

def obter_lista_arquivos(diretorio='.'):
    try:
        # Tenta obter a lista de arquivos no diretório fornecido
        lista_arquivos = os.listdir(diretorio)
        return lista_arquivos
    except OSError as e:
        print(f"Erro ao acessar o diretório: {e}")
        return []

def organizar_por_extensao(lista_arquivos):
    arquivos_por_extensao = {}

    # Itera sobre a lista de arquivos para organizar por extensão
    for arquivo in lista_arquivos:
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lstrip('.')  # Remove o ponto da extensão

        # Adiciona o arquivo à lista correspondente à sua extensão
        if extensao in arquivos_por_extensao:
            arquivos_por_extensao[extensao].append(arquivo)
        else:
            arquivos_por_extensao[extensao] = [arquivo]

    return arquivos_por_extensao

def exibir_arquivos_por_extensao(arquivos_por_extensao, texto_widget):
    texto_widget.delete(1.0, tk.END)  # Limpa o conteúdo atual

    # Exibe os arquivos organizados por extensão no widget de texto
    texto_widget.insert(tk.END, "Arquivos organizados por extensão:\n")
    for extensao, arquivos in arquivos_por_extensao.items():
        texto_widget.insert(tk.END, f".{extensao}: {', '.join(arquivos)}\n")

def main():
    # Criação da interface gráfica
    janela = tk.Tk()
    janela.title("Organizador de Arquivos")
    janela.configure(background="#282A36")

    # Criação do widget de texto
    texto_widget = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=40, height=10, background="#282A36", foreground="#8BE9FD")
    texto_widget.grid(row=0, column=0, padx=10, pady=10)

    # Botão para exibir os arquivos organizados
    botao_exibir = tk.Button(janela, text="Exibir Arquivos", command=lambda: exibir_arquivos_por_extensao(organizar_por_extensao(obter_lista_arquivos()), texto_widget), background="#6272A4", foreground="#8BE9FD")
    botao_exibir.grid(row=1, column=0, padx=10, pady=10)

    # Execução da interface gráfica
    janela.mainloop()

if __name__ == "__main__":
    main()

