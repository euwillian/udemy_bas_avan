

import game_data # acessa a lista/dicionário
import random


# Acessar dados game_data de forma aleatória, porém preciso sempre salvar em uma variável quem estou comparando com quem A > B > C > D

pessoa_a = random.choice(game_data.data)
print(pessoa_a) # dicionário da pessoa A

pessoa_b = random.choice(game_data.data)
print(pessoa_b) 


# for chave, valor in enumerate(game_data.data):
#     print(chave, valor['name'], valor['follower_count'], valor['description'], valor['country'])



# Perguntar ao usúario quem tem mais seguidores A ou B ?



# Sistema de pontuação se acertar continua se errar finaliza


# Posso repetir? Aparentemente é