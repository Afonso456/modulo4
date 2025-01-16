texto= "Olá mundo"

tamanho= (len(texto))
print(tamanho)

texto= texto.upper() #devolve a string em maiusculas
print(texto)

texto= texto.lower() #devolvve a string em minusculas
print(texto)

texto= texto.capitalize() #devolve a string com a primeira letra em maiuscula
print(texto)

texto= texto.strip() #devolve a string sem espaços em branco no inicio e no final 
print(texto)

texto= texto.replace(" ","-") #devolve a string substituindo o primeiro parametro pelo segundo (" " por "-")
print(texto)

texto = texto.isdigit() #devlve True se todas as letras são numeros
print(texto)


frase= "Ola mundo, tudo bem"
palavras= frase.split(" ") #devolve a string separada por espaços em branco
print(palavras)
print(len(palavras))
print(palavras[0])

posicao= frase.index("m") #devolve a posição da strig mas se não existir da erro 
posicao= frase.find("k") #devolve a posição da string mas se não existir da -1
print(posicao)
if posicao == -1:
    print("Letra não encontrada")
else:
    print("Encontrei na posição " + str(posicao)) #ou print("Encontrei na posição" ,posicao)


codigo= ord("a") #devolve o codigo ascii de uma letra 
print(codigo)

letra= chr(97) #devolve a letra correspondente ao codigo ascii 
print(letra)