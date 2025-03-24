import numpy as np

meses_2022 = np.array(["janeiro","fevereiro","março","abril","maio","junho",
                       "julho","agosto","setembro","outubro","novembro","dezembro"])

mortes_2022 = np.array([42,49,44,55,57,66,49,82,66,71,55,32])

#mortes ocorridas em março
for pos in range(len(meses_2022)):
    if meses_2022[pos] == "março":
        print(mortes_2022[pos])
        break

#mortes totais durante o ano
soma = 0
for i in range(len(mortes_2022)):
    soma += mortes_2022[i]
print(f"Durarnte o ano houveram {soma} mortes")

#media de mortes por dia 
media_mortes = soma / 365
print(f"A media de mortes por dia é de {media_mortes}")

#mortes primeiro trimestre
soma_trimestre = mortes_2022[0] + mortes_2022[1] + mortes_2022[2]
print(f"No primeiro trimestre morreram {soma_trimestre}")

#maior numero de mortes
maior = mortes_2022[0]
pos_maior = 0
for i in range(len(mortes_2022)):
    if mortes_2022[i] > maior:
        maior = mortes_2022[i]
        pos_maior = i
print(f"O mes com o numero maior de mortes foi {meses_2022[pos_maior]} com {maior} mortes")

#contar os meses em que o numero de mortes é maior do que a media de mortes do ano 
maior_media = 0
for i in mortes_2022:
    if i > media_mortes:
        maior_media += 1
print(f"Houveram {maior_media} meses com mais mortes do que a media")