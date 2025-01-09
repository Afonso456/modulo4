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

MAX_ITENS= 100
nr_contactos= 0

nomes= np.empty(nr_contactos, dtype= "U50")
emails= np.empty(nr_contactos, dtype= "U50")
numeros= np.empty(nr_contactos, dtype= "U9")

def adicionar(nome, numero, email,nr_contactos):
    for i in range(nr_contactos):
        if nomes[i] == "":
            nomes[i] = nome
            numeros[i] = numero
            emails[i] = email
            nr_contactos+= 1
            return nr_contactos

def listar():
    for i in range(nr_contactos):
        if nomes[i] != "":
            print(f"N-{nomes[i]}\tNº-{numeros[i]}\tE-{emails[i]}")
        else:
            break

def procurar(nome):
    for i in range(nr_contactos):
        if nomes[i] == nome:
            print(f"\nN-{nome}\tNº-{numeros[i]}\tE-{emails[i]} \n")
            return
    print("Contacto não encontrado")
    
def apagar():
    nome = input("Nome:")
    for i in range(nr_contactos):
        if nomes[i] == nome:
            nomes[i] = ""
            numeros[i] = ""
            emails[i] = ""
            return
    print("Contacto não encontrado")

def editar(nome,numero,email):
    global nr_contactos
    op= ""
    op= input("O que deseja editar(nome,numero,emal):\n")
    for i in range(nr_contactos):
        if op == "nome":
            nomes[i] == nome
        elif op == "numero":
            numeros[i] == numero
        elif op == "email":
            emails[i] == email

def sair():
    print("Adeus :)")
    exit()

def menu():
    while True:
        op = input("1:Adicionar\n2:Listar\n3:Procurar\n4:Apagar\n5:Editar\n6:Terminar\n")
        if op == "1":
            nome= input("Nome:")
            numero= input("Numero:")
            email= input("Email:")
            adicionar(nome,numero,email,nr_contactos)
        elif op == "2":
            listar()
        elif op == "3":
            nome= input("Nome:")
            procurar(nome)
        elif op == "4":
            apagar()
        elif op == "5":
            editar(nome,numero,email)
        elif op == "6":
            sair()

def main():
    menu()

if __name__ == "__main__":
    main()
