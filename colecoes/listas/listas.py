"""
Nesta seção iremos estudar Listas no Python

Os mesmos funcionam como vetores / matrizes / array

Difereça: Dinâmicos / aceitam QUALQUER tipo de dado. Ou seja,
não possui tamanho fixo (enquanto houver memória ram, esse será o limitador) e,
não há um tipo de dado fixo.
"""

nome = list('Curso de Python - do Basico ao Avancado!')
print(nome.count('C'))

if 'cc' in nome:
    print('Existe!')
else:
    print('Nao Existe!')