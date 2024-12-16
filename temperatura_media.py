import numpy as np
soma=0
NR_MESES= 12
temperatura= np.empty(12)

maior= temperatura[0]
menor= temperatura[0]

for mes in range(1,NR_MESES):
    if temperatura[mes] > maior:
        maior= temperatura[mes]
    if temperatura[mes] < menor:
        menor= temperatura[mes]
print(f"A temperatura mais elevada foi de {maior} graus e a menor temperatura foi de {menor} graus")

for t in temperatura:
    temperatura= int(input("Insira a temperatura:"))
    soma= soma + t
media = soma / NR_MESES 
print(f"A temperatura media anual foi de {media}")

for mes in range(NR_MESES):
    if temperatura[mes] > media:
        print(f"A temperatura do {mes+1} foi de {temperatura[mes]} sendo superior á media")

moda= 0
nr_vezes_moda= 0

for i in range(NR_MESES):
    conta= 0
    for mes_atual in range(NR_MESES):
        if temperatura[mes] == temperatura[mes_atual]:
            conta += 1
    if conta > nr_vezes_moda:  #se o conta é superior ao nr_vezes_moda este passa a ser a moda
        nr_vezes_moda = conta  #nr de vezes que a temperatura da posição mes aparece
        moda = mes             #a posição da temperatura contada

print(f"A moda é a temperatura {temperatura[moda]} que ocorreu {nr_vezes_moda} vezes")