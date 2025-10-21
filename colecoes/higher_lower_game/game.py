import game_data # acessa a lista/dicionário
import random

def compare(pessoa_a: dict, pessoa_b: dict, escolha: str) -> bool:
    """Retorna True se o usuário acertou, False caso contrário."""
    a = pessoa_a['follower_count']
    b = pessoa_b['follower_count']

    if escolha == 'A':
        return a > b # True
    elif escolha == 'B':
        return b > a # True
    else:
        return False


def random_person() -> dict:
    """Retorna um dicionário de uma pessoa aleatória"""
    return random.choice(game_data.data)


def format_person(pessoa: dict) -> str:
    """Formata a exibição da pessoa."""
    return f"{pessoa['name']}, {pessoa['description']}, from {pessoa['country']}"


def main():
    score = 0
    
    pessoa_a = random_person()
    
    while True:
        
        pessoa_b = random_person()
        
        # Evita que A e B sejam a mesma pessoa
        while pessoa_b == pessoa_a:
            pessoa_b = random_person()
        
        # apresentar
        print(f"Compare A: {format_person(pessoa_a)} \n")
        print(f"VS \n")
        print(f"Compare B: {format_person(pessoa_b)}")
        
        # usuario informa qual tem mais seguidores
        escolha = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        if compare(pessoa_a, pessoa_b, escolha):
            score += 1
            print(f"You're right! Current score: {score}")
            # Ganhou o B vira o próximo A
            pessoa_a = pessoa_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    
    
if __name__ == "__main__":
    main()






