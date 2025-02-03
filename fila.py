"""
O Sr. Joaquim tem um retaurante muito popular e precisa de ajuda a gerir a fila de espera dos clientes
Pretende-se criar para registar os nomes dos clientes em espera e de cada vexz retirar o primeiro
a chegar a fila (FIFO)
Menu: 1.Entrada 2.Saida 3.Consultar fila 4.Terminar
"""
import numpy as np

NR_MAX= 2

def entrada(fila):
    """Adicionar um nome ao fim da fila de espera"""
    encontrou = False
    #procurar o ultimo lugar da fila
    for pos in range(NR_MAX):
        if fila[pos] == "":
            encontrou = True
            break
    #verificar se a fila esta cheia
    if encontrou == False:
        print("Fila cheia. Volte mais tarde.")
        return
    #ler o nome
    nome= input("Nome do cliente:")
    #inserir o nome na posição final do array
    fila[pos] = nome
    print(f"A sua posição na fila de espera é {pos+1}")
    if fila[0] == "":
        print("Fila Vazia")
        return

def saida(fila):
    """Retira o primeiro nome da fila de espera"""
    #verificar se a fila esta vazia
    if fila[0] == "":
        print("Fila Vazia")
        return
    print(f"O cliente com o nome {fila[0]} pode entrar.")
    #retirar o primeiro nome da fila
    for i in range(NR_MAX -1):
        fila[i] = fila[i+1]
        fila[NR_MAX-1] = "" #limpar a ultima posição do array
    #verificar se a fila esta cheia
    if fila == NR_MAX:
        print("Fila cheia. Volte mais tarde.")

def consultar(fila):
    """Lista os nomes da fila de espera"""
    #verificar se a fila esta vazia
    if fila[0] == "":
        print("Fila Vazia")
        return
    #listar os nomes das pessoas em espera
    fila_cheia= False
    for pos in range(NR_MAX):
        if fila[pos] == "":
            fila_cheia= False
        print(f"{pos+1}º {fila[pos]}")
    #verificar se a fila esta cheia
    if fila_cheia == True:
        print("Fila cheia. Volte mais tarde.")

def menu():
    op = 0
    fila= np.empty(NR_MAX, dtype= "U20")
    while op != 4:
        op= input("1.Entrada\n2.Saida\n3.Consulta Fila\n4.Terminar\n")
        if op == "1":
            entrada(fila)
        if op == "2":
            saida(fila)
        if op == "3":
            consultar(fila)
        elif op == "4":
            break
        else:
            print("Opção invalida")
        
def main():
    menu()
if __name__ == "__main__":
    main()