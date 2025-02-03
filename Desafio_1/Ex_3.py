import numpy as np
array= np.array(["joaquim","maria","antonio","augusto","cesar"])

def verificar_nomes(array):
    if "joaquim" in array:
        return True
    return False

def verificar_nomes_v2(array):
    return "joaquim" in array

def verificar_nomes_v3(array):
    for nome in array:
        if nome == "joaquim":
            return True
        return False

print(verificar_nomes(array))
print(verificar_nomes_v2(array))
print(verificar_nomes_v3(array))