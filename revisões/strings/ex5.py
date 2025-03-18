"""
Escreva uma função que recebe uma string e uma letra, e retorna quantas vezes essa letra aparece na string.
Exemplo: "banana", "a" → 3
Restrição: Não use .count().
"""

palavra = input("Insira uma frase ou palavra:")
letra = input("Insira a letra que deseja consultar:")
cont = 0


for i in range(len(palavra)):
    if palavra[i] in letra:
        cont +=1

print(f"A letra {letra} aparece {cont} vezes na palavra")