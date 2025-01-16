"""
Programa que lê o nome de duas pessoas e diz se são da mesma familia ou não

"""

def familiares(nome1,nome2):
    nome_separado1= nome1.split(" ")
    nome_separado2= nome2.split(" ")
    if len(nome_separado1) < 2 and len(nome_separado2) < 2:
        return False
    penultimo1 = nome_separado1[-2]
    penultimo2 = nome_separado2[-2]
    ultimo1 = nome_separado1[-1]
    ultimo2 = nome_separado2[-1]
    return penultimo1 == penultimo2 and ultimo1 == ultimo2



def main():
    nome1= input("Introduza o seu nome:")
    nome2= input("Introduza o seu nome:")
    if familiares(nome1, nome2):
        print("As duas pessoas são da mesma familia")
    else:
        print("As duas pessoas não são da mesma familia")
    


if __name__ == "__main__":
    main()