"""Crie um array que recebe do utilizador uma frase e mostra o numero de vogais presentes na frase
Restrição: Não use .count()."""
import numpy as np
texto = np.empty(1,dtype = "U100")
vogais = ["a,e,i,o,u"]
soma = 0

for i in range(len(texto)):
    texto[i] = input("Introduza uma frase:")
    if texto[i] in vogais:
        soma += 1

print(f"A frase tem {soma} vogais")