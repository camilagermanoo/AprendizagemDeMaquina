# Criar uma estrutura onde peça para ser informado os nomes dos 6 funcionários e seus respectivos salários

dicionario_funcionarios = { }
for i in range(2):
    dicionario_funcionarios[input('Digite o nome: ')] = input('Digite o salário: ')
print(dicionario_funcionarios)
