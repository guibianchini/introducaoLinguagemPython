#Dicionario - Leitura

meu_dicionario = {"A":"AMEIXA","B":"BOLA","C":"CACHORRO"}

###Percorre todo o dicionário imprimindo valores
for chave in meu_dicionario:
    print(meu_dicionario[chave])

###Percorre todo o dicionário imprimindo valor de todos os itens
for i in meu_dicionario.items():
    print(i)

###Percorre todo o dicionário imprimindo apenas os valores
for i in meu_dicionario.values():
    print(i)

###Percorre todo o dicionário imprimindo apenas as chaves
for i in meu_dicionario.keys():
    print(i)