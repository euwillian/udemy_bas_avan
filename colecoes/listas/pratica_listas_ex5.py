"""
5. Sistema de gerenciamento simples

Nível: 🔴 Desafio real (junior)
Objetivo: Integrar tudo o que aprendeu em uma miniaplicação.

Descrição:
Crie um programa que gerencie uma lista de tarefas.
Ele deve:

Exibir um menu com opções:

1 Adicionar tarefa
2 Remover tarefa
3 Listar tarefas
4 Sair

Permitir que o usuário adicione quantas tarefas quiser.
Remova tarefas pelo nome (ou índice).
Mantenha as tarefas organizadas alfabeticamente.
Só finalize quando o usuário escolher sair.

Conceitos testados:

Laços while e for
Estrutura condicional if/elif/else
Manipulação e ordenação de listas
Entrada e saída com input() e print()

"""

lista_tarefas = []

def remover(id: int) -> str:
    # remover tarefa por ID
    try:
        tarefa_removida = lista_tarefas.pop(id)
    except IndexError:
        return "Tarefa inexistente"
    return f"A tarefa '{tarefa_removida}' foi removida!"


def listar() -> None:
    print('-' * 40)
    if len(lista_tarefas) == 0:
        print(f"Não existem tarefas!")
    else:
        for index, tarefa in enumerate(lista_tarefas):
            print(f"ID:{index}, Tarefa: {tarefa}")
    print('-' * 40)


def adicionar(nome_tarefa: str) -> str:
    # adicionar tarefa

    lista_tarefas.append(nome_tarefa)
    return f"Tarefa '{nome_tarefa}' salva com sucesso!"


def main():    
    while True:
        print("""
        1. Adicionar tarefa
        2. Remover tarefa
        3. Listar tarefas
        4. Sair
            """)
        try:
            opcao = int(input("Digite uma opcao da lista: "))
        except ValueError:
            print("Digite apenas o número de uma das opcoes, tente novamente!")
            continue
        
        if opcao == 1:
            tarefa = input("Tarefa: ")
            resultado = adicionar(tarefa)
            print(resultado)
        elif opcao == 2:
            id_tarefa = int(input("ID da tarefa: "))
            resultado = remover(id_tarefa)
            print(resultado)
        elif opcao == 3:
            listar()
        elif opcao == 4:
            print("Finalizando... ")
            break
        else:
            print("Opcão inválida!")
    
main()