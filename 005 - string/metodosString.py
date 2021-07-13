#String - Métodos
a = "Talis"
b = "Guilherme"
concatenar = a + " " + b

###Maiuscula e Minuscula###
print(concatenar.lower())
print(concatenar.upper())

###Remover caracter especial ou espaço no inicio e fim###
print(concatenar.strip())

###Divide frase de String em Lista###
print(concatenar.split(" "))

###Encontrar posição de palavra###
print(concatenar.find("Guilherme"))

###Substituir na String###
print(concatenar.replace("Guilherme", "Fred"))