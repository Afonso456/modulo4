"""
Crie um array que recebe do utilizador numeros e uma variavel que recebe do utilizador um numero que se pretende procurar dentro do array
Restrição: Não use in.
"""
import numpy as np

numeros = np.zeros(10, dtype="int")

for i in range(len(numeros)):
    numeros[i] = int(input("Insira um numero:"))

numero = int(input("Insira o numero a procurar:"))
if numero in numeros:
    print(f"O numero {numero} está presente na sequencia")
else:
    print(f"O numero {numero} não está presente na sequencia")