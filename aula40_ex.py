"""
Interando strings com while
"""
# Resolução do prfessor
#nome = 'Digite o seu nome: '


indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += f'*'
print(novo_nome)

# Exercício incrementado

nome = input('Digite o seu nome: ')
simbolo = input('Digite o simbolo de separação: ')

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'{simbolo}{letra}'
    indice += 1

novo_nome += f'{simbolo}'
print(novo_nome)