# 08/04

# Criar uma estrutura onde peça para ser informado os nomes dos 6 funcionários e seus respectivos salários
# # Depois de tudo feito criar uma estrutura para pesquisar os funcionários pelo nome, informando em tela os nomes 
# # pesquisados e seus salários

# RESOLUÇÃO PROFESSOR -------------------------------------------------------------------------------------------------------

# BLOCO DE DECLARAÇÃO DE VARIÁVEIS
dicionario_funcionarios = { }

# BLOCO DE INTERAÇÃO COM USUÁRIO
# SOLICITAR AO USUÁRIO PARA INSERIR NOMES E SALARIOS
for i in range(7):
    dicionario_funcionarios[input('Digite o nome: ')] = input('Digite o salário: ')
