# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser 
# verdaeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existeo tipo Nome que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#   print('Entrada')
# else:
#    print('Sair')
# Avaliação de curto circuito

senha = input('Senha:') or 'sem senha'
print(senha)



