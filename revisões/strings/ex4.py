"""
Restrição: Não use .replace().
Crie uma função que remove todos os espaços de uma string.
Exemplo: "olá mundo" → "olámundo"
"""

palavra = input("Insira uma palavra:")

palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"A palavra {palavra} é uma palindromo")
else:
    print(f"A palavra {palavra} não é um palindromo")