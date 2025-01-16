"""
Programa que recebe um string com varios nomes e devolve a mesma string com o ultimo nome em primeiro e separado por uma virgula
"""

def alterar_nomes(nome):
    nomes= nome.split(" ")
    if len(nomes) == 1:
       return nome
    nome_alterado= nomes[len(nomes) -1] + " ,"
    for n in nomes[:len(nomes)-1]:
        nome_alterado = nome_alterado + n + " "
        return nome_alterado.strip()
    

def main():
    nome= input("Introduza o seu nome completo:")
    nomme_alterado= alterar_nomes(nome)
    print(nomme_alterado)

if __name__ == "__main__":
    main()