# criar uma estrutura onde:
# pedir 5 vezes pra digitar a cor favorita, e depois apresentar as 5 cores escolhidas


lista_cores = []

for i in range(5):
    lista_cores.append(input('Digite sua cor favorita: '))
print(lista_cores)