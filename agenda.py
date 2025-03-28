"""
Prgrama que permite a criação de uma agenda de contacos
operações:
1:adicionar
2:listar contactos
3:procurar contacto
4:apagar
5:terminar
"""

import numpy as np

MAX_ITENS= 3

def adicionar(nomes, numeros, emails,nr_contactos):
    if nr_contactos == MAX_ITENS:
        print("A agenda de contactos esta cheia")
        return nr_contactos
    nomes[nr_contactos]= input("Nome:")
    numeros[nr_contactos]= input("Numero:")
    emails[nr_contactos]= input("Email:")
    nr_contactos += 1
    return nr_contactos

def listar(nomes,numeros,emails,nr_contactos):
    for i in range(nr_contactos):
        print(f"N-{nomes[i]}\tNº-{numeros[i]}\tE-{emails[i]}")

def procurar(nomes,numeros,emails,nr_contactos):
    nome_procurar= input("Nome a procurar:")
    for i in range(nr_contactos):
        if nome_procurar in nomes[i]:
            print(f"\nN-{nomes[i]}\tNº-{numeros[i]}\tE-{emails[i]} \n")
            return
    print("Contacto não encontrado")

def apagar(nomes,numeros,emails,nr_contactos):
    nome_apagar= input("Nome a apagar:")
    for i in range(nr_contactos):
        if nome_apagar in nomes[i]:
            print(f"\nN-{nomes}\tNº-{numeros[i]}\tE-{emails[i]} \n")
        op= input("Deseja apagar o contacto(s/n):\n")
        if op in "sS":
            for k in range(i,nr_contactos):
                if k == MAX_ITENS - 1:
                    break
                nomes[k] = nomes[k+1]
                numeros[k] = numeros[k+1]
                emails[k] = emails[k+1]
            nr_contactos -= 1
    return nr_contactos

def editar(nomes,numeros,emails,nr_contactos):
    nome= input("Nome:")
    for i in range(nr_contactos):
        if nome in nomes[i]:
            print(f"{nomes[i]} - {numeros[i]} - {emails[i]}")
        op = input("Pretend editar o contacto (s/n):")
        if op != "s":
            continue
        novo_nome= input("Introduza um novo nome ou deixe em branco para não alterar:")
        novo_numero= input("Introduza um novo numero ou deixe em branco para não alterar:")
        novo_email= input("Introduza um novo email ou deixe em branco para não alterar:")
        if novo_nome.strip() != "":
            nomes[i] = novo_nome.strip()
        if novo_numero.strip() != "":
            numeros[i] = novo_numero.strip()
        if novo_email != "":
            emails[i] = novo_email.strip()

def sair():
    print("Adeus :)")
    exit()

def menu():
    nr_contactos= 0

    nomes= np.empty(MAX_ITENS, dtype= "U50")
    emails= np.empty(MAX_ITENS, dtype= "U50")
    numeros= np.empty(MAX_ITENS, dtype= "U9")
    op= 0
    while op != 6:
        op = input("1:Adicionar\n2:Listar\n3:Procurar\n4:Apagar\n5:Editar\n6:Terminar\n")
        if op == "1":
            nr_contactos= adicionar(nomes,numeros,emails,nr_contactos)
        elif op == "2":
            listar(nomes,numeros,emails,nr_contactos)
        elif op == "3":
            procurar(nomes,numeros,emails,nr_contactos)
        elif op == "4":
            nr_contactos= apagar(nomes,numeros,emails,nr_contactos)
        elif op == "5":
            editar(nomes,numeros,emails,nr_contactos)
        elif op == "6":
            sair()

def main():
    menu()

if __name__ == "__main__":
    main()
