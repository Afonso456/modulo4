import numpy as np

nomes= input("Nomes:")
tempos= input("Tempos:")

pilotos= np.array(nomes.split(", "))
voltas= np.array(tempos.split(", "))

i = 0

while (i < 5):
    if int(voltas[i]) < 0:
        voltas[i]= int(input("Tempo da volta:"))
    else:
        i += 1

pm= 0
pp= 0

for i in range(5):
    if int(voltas[i]) < int(voltas[pm]):
        pm = i
    if int(voltas[i]) > int(voltas[pp]):
        pp = i

dif = int(voltas[pp]) - int(voltas[pm])
print(f"Primeiro {pilotos[pm]}")
print(f"Ultimo {pilotos[pp]}")
print(f"Diferença {dif}")

for i in range(5):
    print(f"{pilotos[i]} -> {voltas[i]}")

