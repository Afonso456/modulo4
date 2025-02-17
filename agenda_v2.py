"""
Criar uma agenda que regista por ordem alfabetica.
Guardar o nome e a data de nascimento das pessoas ordenadas por ordem crescente do nome
Menu: 1.Adicionar contacto 2.Listar contacto 3.Procurar 4.Terminar
"""
import numpy as np

NR_MAX= 10

def adicionar(contactos,nome):
    """Recebe um array com o nome e data e ordena por ordem albafetica"""
    #verificar se o array esta vazio
    if contactos[0] == "":
        contactos[0] = nome
        return
    #verificar se o array esta cheio
    if contactos[NR_MAX-1] != "":
        print("Agenda cheia")
        return
    #procurar a posição do novo contacto
    for pos in range(NR_MAX):
        if nome < contactos[pos] or contactos[pos] == "":
            break
    #avançar uma posição os restantes contactos
    for i in range(NR_MAX-1, pos,-1):
        contactos[i] = contactos[i-1]
    #inserir o contacto
    contactos[pos]= nome
    
def listar(contactos):
    """Lista os nomes e as datas de todos os contactos"""
    for nome in contactos:
        if nome != "":
            partes= nome.split("-")
            print(f"Nome-{partes[0]} Data de Nascimento-{partes[1]}")

def procurar(contactos,nome):
    """Recebe o array e o nome a pesquisar"""
    inicio= 0
    fim = 0
    for t in contactos:
        if t == "":
            break
        fim +=1
    while inicio <= fim:
        meio= (inicio + fim) // 2
        valor_meio= contactos[meio]
        if nome in valor_meio:
            print(valor_meio)
            return 
        elif valor_meio < nome:
            inicio= meio + 1
        else:
            fim= meio - 1
    print("O contacto que procura não existe")

def menu():
    op = 0
    contactos= np.zeros(NR_MAX, dtype= "U30")
    while op != 4:
        op= input("1.Adicionar\n2.Listar\n3.Procurar\n4.Terminar\n")
        if op == "1":
            nome= input("Nome:")
            data= input("Data de nascimento:")
            adicionar(contactos,nome+ "-" +data)
        elif op == "2":
            listar(contactos)
        if op == "3":
            nome= input("Nome a pesquisar:")
            procurar(contactos,nome)
        elif op == "4":
            break

def main():
    menu()

if __name__ == "__main__":
    main()