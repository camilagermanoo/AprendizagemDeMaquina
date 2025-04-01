# 01/04/2025 
    # Conteúdo:
# Tratamento de erro e exceções

# ctrl k depois ctrl c para comentar um monte de linha ao msm tempo

# TRY -> trata exceção
# [Bloco de instruções] -> bloco que eu quero que seja testado pra ver se há alguma intenção
# EXCEPT
# [Bloco de instruções]
# ELSE
# [Bloco de instruções]

# Declaração de variáveis
nota1 = nota2 = 0
media = 0.0

nota3 = input()

# Loop 1 para testar valores. Aceita apenas números e que estejam entre 0 e 10.
# Classe de tratamento de erro

while True:
    try:
        nota1 = int(input('Digite a nota da P1 [Enter]'))  # o int transforma strings em inteiro
        # pra cair aqui tem que ser um NÚMERO, se a pessoa digitar um "M" por exemplo, ele vai direto pro except
        if not 0 <= nota1 <= 10:       # tudo que não esteja entre 0 e 10 vai dar erro (inclui letras, caracteres e etc)
            raise ValueError ('Somente número de 0 a 10')
        # só vai cair aqui no except se o que estiver em cima for verdadeiro (realmente der erro), se nao vai pro else
    except ValueError as e:
        print ('Favor informar um número! Erro interno: ', e)
    else:
        break
    

# Loop 2 para testar valores. Aceita apenas números e que estejam entre 0 e 10
# Método para verificar se é numérico - aqui vai ficar repetindo até a pessoa digitar um número

while True:
    nota2 = input('Digite a nota da P2')
    if nota2.isnumeric():
        if(int(nota2) >= 0) and (int(nota2) <= 10):
            nota2 = int(nota2)
            break
        else:
            print('Digite uma nota entre 0 e 10')
            continue
    else:
        print('Digite um número válido')
