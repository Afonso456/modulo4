"""
Programa que simula um moedeiro de uma maquina de vendas
O programa deve ler o preço do produto e o valor entregue e depois devolver o troco se exitente
"""
import numpy as np

moedas= np.array([0.01,0.02,0.05,0.10,0.20,0.50,1,2])
stock= np.array([2,2,2,2,2,2,2,2])

#preço do produto
preco= float(input("Introduza o preço do produto:"))
#valor entregue pelo cliente
valor_entregue= float(input("Valor entregue:"))
#calcular o troco
troco= valor_entregue - preco
if troco == 0:
    print("Volte sempre")
else:
#procurar as quantias que prefaazem a quantia do troco
    while troco > 0:
        for m in range(len(moedas)-1,-1,-1):
            moedas_devolver= ""
            if moedas[m] < troco and stock[m] > 0:
                moedas_devolver= moedas_devolver + str(moedas[m]) + ","
                stock[m] = stock[m] - 1
                break
    print(f"Moedas a devolver {moedas_devolver} e o troco restante é de {troco}")
    print(moedas,stock)