"""
1. Manipulação básica de listas

Nível: 🟢 Iniciante
Objetivo: Testar se você domina criação, acesso e modificação de listas.

Descrição:
Crie uma lista chamada numeros contendo cinco números inteiros à sua escolha.
Em seguida:

Exiba o primeiro e o último número da lista.
Adicione um novo número ao final.
Remova o segundo número.
Substitua o terceiro número por outro valor.
Exiba a lista final.

Conceitos testados:

Indexação (lista[0], lista[-1])
Métodos append(), remove() ou del, atribuição direta

"""


numeros = [10, 20, 30, 40, 50] # criacao da lista

print(numeros[0])  # primeiro item da lista
print(numeros[-1]) # ultimo item da lista
numeros.append(60) # adiciona um numero no final da lista
numeros.remove(20) # remove o segundo numero da lista, eu já sei qual é se não deveria ir via index numeros[1]
numeros[2] = 33    # substituicao do valor
print(numeros)     # print final