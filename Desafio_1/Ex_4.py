def contar(nomes,nome):
    contar_repetidos= 0
    for i in nomes:
        if nome == nomes:
            contar_repetidos += 1
    return contar_repetidos

def contar_v2(nomes,nome):
    for p in nomes:
        pass
    
print(contar(["joaquim","maria","antonio","augusto","cesar"],"joaquim"))