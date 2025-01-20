"""
Função para separar as letras de uma string
"""

nome= "Joaquim-Silva"
nome_5_letras= nome[0:5:1] #copia as letras das posições 0 a 4 
print(nome_5_letras)
nome_5_letras= nome[:5:1] #copia as letras das posições 0 a 4 omitindo o zero
print(nome_5_letras)
nome_ultimas_letras= nome[7:] #copia as letras da posição 7 ate ao fim 
print(nome_ultimas_letras)
nome_invertido= nome[::-1]
print(nome_invertido)
nome_2_2_letras= nome[::2]
print(nome_2_2_letras)
print(nome[-1]) #da a posição da ultima letra da string

ultimo_contrario= nome[13:7:-1]
print(ultimo_contrario)


import numpy as np

nome= np.array(["joaquim","maria","antonio","augusto","cesar"])
#mostrar os nomes por ordem inversa
print(nome[::-1])
#mostrar os dois ultimos nomes
print(nome[3:])
#mostrar o 1º 3º e 5º 
print(nome[::2])
