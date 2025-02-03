"""
Programa que recebe um frase e transforma essa frase com as palavras proibidas em palavras alternativas
"""
import numpy as np

proibidas= np.array(["mau","pobre","infeliz","pessimo"])
alternativas= np.array(["bom","rico","feliz","otimo"])

frase = input("Introduza uma frase:")
for i in range(len(proibidas)):
    if proibidas[i] in frase:
        frase= frase.replace(proibidas[i],alternativas[i])
print(frase)