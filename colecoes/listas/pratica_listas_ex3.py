"""
3. Ordenação, soma e média

Nível: 🟡 Intermediário II
Objetivo: Testar domínio de funções e métodos embutidos.

Descrição:
Crie uma lista com 8 números inteiros aleatórios.
Depois:

Mostre o maior e o menor número.
Calcule e exiba a soma total e a média dos valores.
Mostre a lista ordenada de forma crescente e decrescente (sem alterar a original).

"""

num_int = [10, 40, 30, 11, 55, 60, 70, 80, 12]

print(min(num_int)) # menor
print(max(num_int)) # maior

print(f"soma {sum(num_int)} - média {sum(num_int)/len(num_int)}")
print(num_int)
print(sorted(num_int, reverse=True)) # ordenada desc
print(sorted(num_int, reverse=False)) # ordenada asc
