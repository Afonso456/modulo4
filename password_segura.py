import numpy as np

lista= np.array(["M3D1A" "12345" "123456" "Password" "ADMIN"])
password= input("Insira a sua palavra-passe:")

for i in range(lista):
    if password in lista:
        print("A sua password não é segura")
    else:
        print("A sua password é segura")