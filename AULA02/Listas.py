# 01/04/2025
    # Conteúdo: Lista 
    
# Observação: listas, matrizes e dicionarios são sempre obrigados a serem declarados    

lista_1 = [2, 4, 6, 8, 10]
lista_2 = [1, 3, 5, 7, 9, 11]
valores_lista = lista_1 + lista_2
print("listas", valores_lista)

valores_lista[1] = input('Digite um número: ')
print ('Alterou um valor: ', valores_lista)

#-------------------------------------------------------------------------------#

# Método para incluir um valor em uma lista: APPEND
# O append é pra inserir, mas ele insere sempre no FINAL da lista

valores_lista.append(int(input('Digite um número: ')))
print ('Adicionou um valor no FINAL da lista: ', valores_lista)

#-------------------------------------------------------------------------------#

# Método para INCLUIR um valor na posição que você quiser: INSERT

valores_lista.insert(0,input('Digite um número: '))
print ('Inseriu um valor na posição que quiser: ', valores_lista)

#-------------------------------------------------------------------------------#

# Método para REMOVER um VALOR e NÃO uma POSIÇÃO: REMOVE

valores_lista.remove(input('Digite um número: '))
print ('Removeu um valor específico: ', valores_lista)

#-------------------------------------------------------------------------------#

# Método para REMOVER um valor que está naquele ÍNDICE (posição) e NÃO um NÚMERO: POP

valores_lista.pop(int(input('Digite um índice da lista: ')))
print ('Removeu uma posição da lista: ', valores_lista)
