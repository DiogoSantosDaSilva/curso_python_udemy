"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

try:
    num_int = int(numero)
    if num_int % 2 == 0:
        print(f'O número {numero} é PAR!')
    else:
        print(f'O número {numero} é IMPAR!')
except:
    print('Não é um número inteiro!')

    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exibe a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""


hora = input('Informe as horas: ')

try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite!')
except:
    print('Por favor digite as horas em formato inteiro.')
    

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva 'Seu nome é curto'; se tiver entre 5 e 6 letras, escreva
'Seu nome é normal', maior que 6 escreva 'Seu nome é muito grande'
"""
nome = input('Digite o seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto.')
elif len(nome) > 4 and len(nome) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')