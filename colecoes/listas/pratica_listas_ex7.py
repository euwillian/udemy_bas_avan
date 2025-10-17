"""
7. Sistema de notas de alunos

Objetivo: introduzir manipulação de dados e médias.
Conceitos: listas, loops, cálculos, condicionais compostas.

Requisitos:

Cadastre alunos e suas notas (duas notas por aluno).

Exiba o nome, as duas notas e a média.

Informe se está aprovado (média >= 6) ou reprovado.

Permita listar todos os alunos e consultar individualmente por nome.

Desafio extra: mostre a maior e menor média da turma.
"""
def menu():
    print("""
    1. Cadastrar aluno
    2. Listar todos os alunos
    3. Consultar por nome
    4. Sair
    """)


def cadastrar_aluno(lista_alunos: list, nome: str, nota1: float, nota2: float):
    media = (nota1 + nota2) / 2
    aluno = {"nome": nome, "nota1": nota1, "nota2": nota2, "media": media}
    lista_alunos.append(aluno)
    return nome


def listar_alunos(lista_alunos: list):
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("-" * 50)
    print(f"{'NOME':<15} {'NOTA 1':<10} {'NOTA 2':<10} {'MÉDIA':<10}")
    print("-" * 50)
    for aluno in lista_alunos:
        print(f"{aluno['nome']:<15} {aluno['nota1']:<10.2f} {aluno['nota2']:<10.2f} {aluno['media']:<10.2f}")


def listar_por_nome(lista_alunos: list, nome: str):
    encontrados = [a for a in lista_alunos if a['nome'].lower() == nome.lower()]

    if not encontrados:
        print(f"Nenhum aluno encontrado com o nome '{nome}'.")
        return

    for aluno in encontrados:
        print(f"Aluno: {aluno['nome']}")
        print(f"Nota 1: {aluno['nota1']}")
        print(f"Nota 2: {aluno['nota2']}")
        print(f"Média: {aluno['media']:.2f}")
        print("-" * 30)


def main():
    alunos = []

    while True:
        menu()
        try:
            opcao = int(input("Digite uma opção: "))
        except ValueError:
            print("Digite uma opção válida.")
            continue

        if opcao == 1:
            nome = input("Nome do aluno: ")

            try:
                nota1 = float(input("Nota 1: ").replace(',', '.'))
                nota2 = float(input("Nota 2: ").replace(',', '.'))
            except ValueError:
                print("Digite notas numéricas válidas.")
                continue

            resultado = cadastrar_aluno(alunos, nome, nota1, nota2)
            print(f"Aluno {resultado} cadastrado com sucesso!")
        elif opcao == 2:
            listar_alunos(alunos)
        elif opcao == 3:
            nome = input("Nome do aluno: ")
            listar_por_nome(alunos, nome)
        elif opcao == 4:
            print("Finalizando...")
            break
        else:
            print("Opção inválida.")

main()
