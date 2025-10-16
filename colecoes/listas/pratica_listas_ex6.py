"""
1. Cadastro de produtos com preço e total da compra

Objetivo: praticar listas de dicionários, laços e funções com retorno.
Conceitos: listas, dicionários, funções puras, formatação de strings.

Requisitos:

Crie um programa com menu (1. Adicionar produto, 2. Listar, 3. Total da compra, 4. Sair)
Cada produto deve ter: nome e preço.
Armazene tudo em uma lista de dicionários, ex:
{"nome": "Arroz", "preco": 12.50}


O total deve somar todos os preços cadastrados e exibir formatado com duas casas decimais.

Desafio extra: ordene os produtos pelo nome antes de listar.
"""
def adicionar_produto(lista: dict, nome: str, valor: float):
    lista[nome] = valor
    return nome, valor
    
    
def listar_produtos(lista: dict):
    if not lista:
        print("Nenhum produto cadastrado.")
        return
    for nome, valor in sorted(lista.items()):
        print(f"{nome:<15} R$ {valor:>6.2f}")


def total_produtos(lista: dict) -> float:
    total = 0
    for chave, valor in lista.items():
        total += valor
        
    return total


def main():
    produtos = {}
    while True:
        print("""
            1. Adicionar produto
            2. Listar produtos
            3. Total da compra
            4. Sair
            """)
        
        try:
            opcao = int(input("opcao: "))
        except ValueError:
            print("opcao invalida")
            continue
        
        
        if opcao == 1:
            n = input("nome: ")
            
            try:
                v = float(input("valor: ").replace(',', '.'))
            except ValueError:
                print("digite um valor válido, tente novamente")
                continue
            
            nome, valor = adicionar_produto(produtos, n, v)
            print(f"Produto '{nome}' no valor de R$ {valor:.2f} salvo com sucesso!")
        elif opcao == 2:
            print("-" * 40)
            listar_produtos(produtos)
            print("-" * 40)
        elif opcao == 3:
            res = total_produtos(produtos)
            print(f"Total da compra: {res:.2f}")
        elif opcao == 4:
            print("Finalizando..")
            break
        else:
            print("invalido..")
        

main()