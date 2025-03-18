"""Escreva uma função que recebe uma string e retorna a versão invertida dela.
    Exemplo: "python" → "nohtyp"
    Restrição: Não use [::-1] ou reversed().
"""

texto = input("Insira uma frase ou palavra:")

texto_invertido = texto[::-1]
print(texto_invertido)