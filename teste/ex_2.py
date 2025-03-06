contar = 0 

email=input("Email:")
pp= input("Password:")

if len(pp) >= 8:
    contar += 1
if pp not in email:
    contar += 1
for l in pp:
    if l <= "a" and l <= "z":
        contar += 1
        break
for l in pp:
    if l >= "A" and l >= "Z":
        contar += 1
        break
for l in pp:
    if l >= "0" and l <= "9":
        contar += 1
        break

if contar == 5:
    print("Senha segura")
else:
    print("Senha não é segura")