"""
Progama que regista o nome de cada cliente que entra na loja num determindao dia e o valor das compras de cada
O programa deve mostrar o nome do cliente que fez a compra mais cara
"""
import numpy as np

MAX_CLENTES= 10

nome= np.empty(MAX_CLENTES,dtype="U50")
d_gasto= np.empty(MAX_CLENTES,dtype="f")

def ler_dados(nome_clientes, gastos):
    n_clientes= int(input("Introduza o numero de clientes:"))
    if n_clientes > MAX_CLENTES:
        print("Numero de clientes excedido")
        return
    for i in range(MAX_CLENTES):
        nome_clientes[i]= input("Nome do cliente:")
        gastos[i]= input("Introduza o valor gasto:")

def cliente_mais_caro(nome_clientes,gastos):
    max_gasto= max(gastos)
    pos= np.where(gastos==max_gasto)
    print(f"O cliente que mais gastou foi o {nome_clientes[pos[0][0]]} com {max_gasto} €")

def melhor_cliente(nome_clientes,gastos):
    maior_compra= gastos[0]
    for i in range(MAX_CLENTES):
        if gastos[pos] < gastos[i]:
            maior_compra= gastos[i]
            pos= i
            print(f"O clienet que mais gastou foi o {nome_clientes[pos]} que gastou {maior_compra}€")

ler_dados(nome,d_gasto)
melhor_cliente(nome,d_gasto)
