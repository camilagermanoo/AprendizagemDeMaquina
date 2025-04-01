# 25/03/2025

# criar uma estrutura onde:
# pedir para digitar sua cor favorita (uma cor para cada um)
# apresentar em tela as cores escolhidas

#-------------------------------------------------------------------#

# 1 passo: criar variáveis para cada um e solicitar a interação

# corMaria = input("Digite sua cor favorita: ")
# corPedro = input("Digite sua cor favorita: ")
# corAndre = input("Digite sua cor favorita: ")
# corCamila = input("Digite sua cor favorita: ")
# corJoao = input("Digite sua cor favorita: ")

# 2 passo: apresentar os resultados

# print(f'Cores escolhidas: ' + corMaria)
# print(f'Cores escolhidas: ' + corPedro)
# print(f'Cores escolhidas: ' + corAndre)
# print(f'Cores escolhidas: ' + corCamila)
# print(f'Cores escolhidas: ' + corJoao)

#-------------------------------------------------------------------#

# se atentar aos símbolos: [] () {}
# variavel = str / bool / int / float / complex
# lista = [0, 58, 80, 90, 7, true, 80.9342, false, "10"]
# matriz = [ [a,b], [c,d], [e,z] ]  -> várias listas dentro de uma matriz
# tupla = (0, 58, 80, 90, 7, true, 80.9342, false, "10")
# IMPORTANTE!!! -> a única diferença de uma tupla pra uma lista, é que na tupla os valores nao modem ser mudados
# IMPORTANTE!!! -> listas e matrizes, a variavel tem q ser declarada
# dicionário = { }

#-------------------------------------------------------------------#

#lista_cores = []

# lista_cores[0] = input("Digite sua cor favorita: ")
# lista_cores[1] = input("Digite sua cor favorita: ")
# lista_cores[2] = input("Digite sua cor favorita: ")
# lista_cores[3] = input("Digite sua cor favorita: ")

# CONTADOR (substitui o tanto de linha acima)
# for i in range(3):              
#     lista_cores.append(input('Digite sua cor preferida: ')) #esse apend é um método pra adicionar ao final da lista

# print(lista_cores)  

#-------------------------------------------------------------------#

lista_vendas = [100, 200, 300, 1000, 5000, 800, 300]
lista_nomes = ['André']

#CONTADORES
print ('Soma de todos os valores:', sum(lista_vendas)) #soma
print ('Quantidade de itens:', len(lista_vendas)) #ve o tamanho
print ('Valor mínimo:', min(lista_vendas)) #menor valor
print (f"Valor máximo: , {max(lista_vendas)}") #maior valor -> é outra forma de apresentar, usando o f''

#ADICIONAR UM ITEM
lista_nomes.append('Fernando')
print(lista_nomes)

#REMOVER UM ITEM
lista_nomes.remove('André')
print(lista_nomes)

# if "André" in lista_nomes: #esse metodo é usado para ver se o nome está na lista
#     lista_nomes.remove(André)
