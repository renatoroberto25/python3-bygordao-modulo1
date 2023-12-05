
################################
##############001###############
################################
"""
#Exibir no terminal alguma ação:
print("Exemplo de print básico")
#Variáveis armazenam dados, seja ele qual for, para o tempo de execução de seu programa

nome = "Renato"
#exemplo de string

idade = 33
#exemplo de inteiro

peso = 110.2
#exemplo de float


print(nome)
print(idade)
print(peso)
#exibindo as variáveis
"""
################################
##############002###############
################################
"""

nome=(input("Seu nome: "))
#input naturalmente já é string
idade=int(input("Sua idade: "))
#aqui convertemos em ineiro
peso=float(input("Seu peso: "))
#convertemos em float

print(nome)
print(idade)
print(peso)
"""
################################
##############003###############
################################
"""
soma = 9 + 1
subtracao = 10 - 1
multiplicacao = 9 * 8
divisao = 45 / 9
potencia = 7 ** 2
print("exemplo  de soma: ",soma)
print("exemplo  de subtracao: ", subtracao)
print("exemplo  de multiplicacao: ",multiplicacao)
print("exemplo  de divisao: ",divisao)
print("exemplo  de potencia: ",potencia)
"""
################################
##############004###############
################################
"""
#condicionais
valor1 =  47
valor2 = 55
if valor1 > valor2:
    print(valor1, "é maior que", valor2)
#verificar o valor
else:
    print(valor2, "é maior que", valor1)

"""
################################
##############002###############
################################
"""
#condicionais AND orientação a objetos na mesma:

#vamos criar uma classe chamada pessoa, que vai receber idade nome e peso, de um individuo que quer entrar em um brinquedo
#num parque de diversões, mas ele tem bastante risco então só maiores de 18 anos e com limite de peso em 120kg

# Definindo a classe Pessoa
class Pessoa:
    # Método especial de inicialização (__init__) que é chamado quando uma nova instância da classe é criada
    def __init__(self, nome, idade, peso):
        # Atributo 'nome' da instância recebe o valor fornecido
        self.nome = nome
        # Atributo 'idade' da instância recebe o valor fornecido
        self.idade = idade
        # Atributo 'peso' da instância recebe o valor fornecido
        self.peso = peso

# Solicitando informações do usuário para criar uma pessoa
nome = input("Digite o nome: ")      # Solicita e armazena o nome fornecido pelo usuário
idade = int(input("Digite a idade: "))  # Solicita e converte para inteiro a idade fornecida pelo usuário
peso = float(input("Digite o peso em quilos: "))  # Solicita e converte para float o peso fornecido pelo usuário

# Criando uma instância da classe Pessoa com as informações fornecidas pelo usuário
pessoa = Pessoa(nome, idade, peso)

# Verificando se a idade é menor que 18
if pessoa.idade < 18:
    # Se a idade for menor que 18, imprime uma mensagem informando que a entrada não é permitida para menores de 18 anos
    print(f"{pessoa.nome}, você não pode entrar. Menores de 18 anos não são permitidos.")
# Verificando se o peso é maior que 119.8
elif pessoa.peso > 119.8:
    # Se o peso for maior que 119.8, imprime uma mensagem informando que a entrada não é permitida por motivos de segurança
    print(f"{pessoa.nome}, entrada não permitida por motivos de segurança. Peso acima de 119.8 kg.")
# Se a idade não for menor que 18 e o peso não for maior que 119.8, então a entrada é liberada
else:
    print(f"{pessoa.nome}, entrada liberada. Divirta-se!")
"""
################################
##############005###############
################################
"""
#listas
# Criando uma lista com 5 itens
# Definindo uma lista de frutas
lista_frutas = ["Maçã", "Banana", "Laranja", "Morango", "Uva"]

# Imprimindo a lista inicial de frutas
print("Lista inicial de frutas:", lista_frutas)

# Acessando a segunda fruta da lista (o índice começa em 0)
print("\nA segunda fruta é:", lista_frutas[1])

# Alterando o valor da terceira fruta na lista (índice 2)
lista_frutas[2] = "Pêssego"
print("\nAlterando a Laranja (índice 2) para Pêssego...")
print("Lista de frutas após a alteração:", lista_frutas)

# Adicionando uma nova fruta ao final da lista
lista_frutas.append("Abacaxi")
print("\nAdicionando a fruta Abacaxi ao final da lista...\n")
print("Lista de frutas após a adição:", lista_frutas)

# Removendo o quarto item da lista (índice 3)
item_removido = lista_frutas.pop(3)
print("\nRemovendo o quarto item (índice 3)...")
print(f"Lista de frutas após a remoção de {item_removido}:", lista_frutas)
"""
################################
##############006###############
################################
"""
#listas usando módulo nativo do python random para gerar a lista:
#usei pra ganhar na mega sena claro
import random

# Gerando uma lista com 5 números aleatórios entre 1 e 100
lista_numeros = [random.randint(1, 60) for _ in range(6)]
#detalhe para o FOR e range for é um loop de repetição básico

# Imprimindo a lista
print("Lista de números:", lista_numeros)

# Exibindo a quantidade de números na lista
quantidade_numeros = len(lista_numeros)
print(f"\nQuantidade de números na lista: {quantidade_numeros}")

# Encontrando o menor e o maior número na lista
menor_numero = min(lista_numeros)
maior_numero = max(lista_numeros)
print(f"Menor número na lista: {menor_numero}")
print(f"Maior número na lista: {maior_numero}")
"""
################################
##############007###############
################################
"""
#loops:
# Exemplo de loop for
print("Usando o loop 'for':")
for i in range(5):
    print(f"Iteração {i + 1}")

# Linha em branco para separar os resultados dos dois loops
print("\n" + "=" * 30 + "\n")

# Exemplo de loop while
print("Usando o loop 'while':")
contador = 1
while contador <= 5:
    print(f"Iteração {contador}")
    contador += 1
"""
################################
##############008###############
################################

# Criando um dicionário com informações de um estudante
estudante = {
    "nome": "João",
    "idade": 20,
    "curso": "Ciência da Computação",
    "notas": [90, 85, 88]
}

# Imprimindo o dicionário
print("Dicionário de Estudante:")
print(estudante)

# Acessando informações específicas no dicionário
print("\nInformações do Estudante:")
print(f"Nome: {estudante['nome']}")
print(f"Idade: {estudante['idade']}")
print(f"Curso: {estudante['curso']}")
print(f"Notas: {estudante['notas']}")

# Modificando uma informação no dicionário
estudante["idade"] = 21

# Adicionando uma nova informação ao dicionário
estudante["cidade"] = "São Paulo"

# Imprimindo o dicionário atualizado
print("\nDicionário de Estudante Atualizado:")
print(estudante)
################################
##############008###############
################################
