"""
2. Listas e loops

Nível: 🟡 Intermediário I
Objetivo: Praticar o uso de for, len() e lógica simples.

Descrição:
Crie uma lista com nomes de 5 pessoas.
Depois:

Exiba todos os nomes em letras maiúsculas, um por linha.
Conte quantos nomes têm mais de 5 letras.
Crie uma nova lista apenas com esses nomes longos.
Exiba as duas listas no final.

Conceitos testados:

Iteração com for
Condicionais dentro de loops
Criação de nova lista com base em outra

"""

nomes = ['Giovana', 'Willian', 'Aldo', 'Claudete', 'Priscila']

for nome in nomes:
    print(nome.upper()) # Nomes por linha e em maisculo

aux = 0 # contador
for nome in nomes:
    if len(nome) > 5:
        aux += 1 # nomes com mais de 5 caracteres
print(aux)


lista_nova = []
for nome in nomes:
    if len(nome) > 5:
        lista_nova.append(nome) # lista só com nomes > 5 caracteres

print(lista_nova)
print(nomes)