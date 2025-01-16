import numpy as np

socios_a= np.array(["joaquim" "maria" "joão" "luis"])
socios_b= np.array(["maria" "antonio" "carla" "luis"])

for nome_a in socios_a:
    for nome_b in socios_b:
        if nome_a == nome_b:
            print(f"O socio com o nome {nome_a} pretence aos dois clubes")

#versão 2
for nome_a in socios_a:
    if nome_a in socios_b:
        print(f"O socio com o nome {nome_a} pertence aos dois clubes")