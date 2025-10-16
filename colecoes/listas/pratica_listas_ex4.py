"""
4. Listas aninhadas (listas dentro de listas)

Nível: 🔵 Intermediário/Avançado
Objetivo: Testar manipulação e acesso de estruturas bidimensionais.

Descrição:
Crie uma lista chamada alunos que contenha sublistas com o nome e três notas de cada aluno.
Exemplo:

alunos = [
    ["Ana", 8.0, 9.0, 7.5],
    ["João", 6.0, 5.5, 7.0],
    ["Maria", 9.0, 8.5, 9.5]
]

Depois:

Exiba o nome e a média de cada aluno.
Mostre somente os alunos com média maior ou igual a 7.0.
Exiba o nome do aluno com maior média geral.


Conceitos testados:

Indexação em listas aninhadas
Cálculos com listas
Laços for dentro de for
Controle lógico

"""

alunos = [
    ["Ana", 8.0, 9.0, 7.5],
    ["João", 6.0, 5.5, 7.0],
    ["Maria", 9.0, 8.5, 9.5]
]

nome = ''
maior = 0
nome_maior_media = ''

for lista_aluno in alunos:
    valor_media = 0.0
    for item_da_lista_aluno in lista_aluno:
        if type(item_da_lista_aluno) == str:
            nome = item_da_lista_aluno
        else:
            valor_media += item_da_lista_aluno
            
    valor_media /= len(lista_aluno) - 1

    if valor_media >= 7:
        print('-' * 20)
        print('Alunos com nota igual ou superior a 7:')
        print(f'nome: {nome} - media: {valor_media:.2f}')
        print('-' * 20)
    
    if valor_media > maior:
        maior = valor_media
        nome_maior_media = nome

print('Aluno com maior média:')
print(f"{'Nome':<10} | {'Média':>5}")
print('-' * 20)
    

"""

Forma simplificada e corrigida

alunos = [
    ["Ana", 8.0, 9.0, 7.5],
    ["João", 6.0, 5.5, 7.0],
    ["Maria", 9.0, 8.5, 9.5]
]

maior_media = 0
aluno_top = ''

print('Alunos com média >= 7:\n')

for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1:]
    media = sum(notas) / len(notas)

    if media >= 7:
        print(f'{nome:<10} - Média: {media:.2f}')

    if media > maior_media:
        maior_media = media
        aluno_top = nome

print('\nAluno com maior média:')
print(f'{aluno_top} - Média: {maior_media:.2f}')


"""

