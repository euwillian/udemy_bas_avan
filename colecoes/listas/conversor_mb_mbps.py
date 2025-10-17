"""
8. Simulador de tempo de download

Objetivo: trabalhar com cálculos simples e funções que retornam valores.
Conceitos: funções com parâmetros, operações matemáticas e condicionais.

Requisitos:

Peça o tamanho do arquivo (em MB) e a velocidade da internet (em Mbps).
Calcule o tempo estimado de download em minutos e segundos.

Mostre formatado, ex:
O download de 800 MB a 20 Mbps levará aproximadamente 5 minutos e 20 segundos.

Desafio extra: use math.ceil() para arredondar segundos
"""

import math

def calcular(tamanho_mb: int, velocidade: int) -> int:
    mb_to_mbps = tamanho_mb * 8 # 1MB => 8Mbps
    segundos = mb_to_mbps / velocidade # com o valor em mbps podemos dividir pela internet em mbps
    minutos = segundos // 60 # minutos
    segundos_restantes = segundos % 60 # segundos
    
    return math.ceil(minutos), math.ceil(segundos_restantes)

    
minutos, segundos = calcular(800, 20)
print(f"O download levará aproximadamente {minutos} minutos e {segundos} segundos.")