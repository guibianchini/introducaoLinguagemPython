#File - AberturaeLeitura
arquivo = open("arquivo.txt")

#read,readline,readlines
linhas = arquivo.readlines()

for linha in linhas:
    print(linha)