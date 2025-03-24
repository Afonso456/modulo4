numero =input("Insira um numero de telemovel:")

valido = True

#numero precisa ter 9 digitos
if len(numero) != 9:
    print("O numero precis conter 9 digitos")
    valido = False 

#numero precisa conter apanas numeros
if not numero.isdigit():
    print("O numero deve ser composto apenas por numeros")
    valido = False

#ou
"""
for l in numero:
    if l.isdigit() == False:
        print("Deve ter apenas digitos numeros")
        valido = False
"""

#numero tem que começar com os indicativos (91,92,93,96)
indicativo = numero[:2:]
indicativos_v= ("91","92","93","96")
if indicativo not in indicativos_v:
    print(f"O indicativo precisa conter {indicativos_v}")
    valido = False

#numero não pode ser constituido apenas por 0
zeros = numero[3::]
if zeros == "0000000":
    print("O numero não pode ser constituido apenas por 0")
    valido = False

if valido == True:
    print("O numero é válido")
