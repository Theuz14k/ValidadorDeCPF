'''
Este projéto se trata de um validador de CPFs onde o usuário irá digitar um CPF e o algoritimo
irá calcular os digitos verificadores do mesmo e caso os digitos verificadores calculados não forem iguais
aos digitos verificadores mostrados no CPF informado pelo usuário, este CPF será inválido
'''

CPF = input('Digite um CPF: ') #Digite aqui o CPF a ser validado

N = CPF[0:9:1]

lista = [int(N[0]), int(N[1]), int(N[2]), int(N[3]), int(N[4]), int(N[5]), int(N[6]), int(N[7]), int(N[8])]

n1, n2, n3, n4, n5, n6, n7, n8, n9 = lista

# Primeiro digito verificador

v1 = 10 * n1
v2 = 9 * n2
v3 = 8 * n3
v4 = 7 * n4
v5 = 6 * n5
v6 = 5 * n6
v7 = 4 * n7
v8 = 3 * n8
v9 = 2 * n9

SOMA1 = v9 + v8 + v7 + v6 + v5 + v4 + v3 + v2 + v1
calc1 = 11 - (SOMA1 % 11)
if calc1 <= 9:
    print(f'O primeiro digito verificador deste CPF é {calc1}')
else:
    calc1 = 0
    print(f'O primeiro digito verificador deste CPF é {calc1}')

# Segundo digito verificador

f0 = 11 * n1
f1 = 10 * n2
f2 = 9 * n3
f3 = 8 * n4
f4 = 7 * n5
f5 = 6 * n6
f6 = 5 * n7
f7 = 4 * n8
f8 = 3 * n9
f9 = 2 * calc1

SOMA2 = f9 + f8 + f7 + f6 + f5 + f4 + f3 + f2 + f1 + f0
calc2 = 11 - (SOMA2 % 11)

if calc2 <= 9:
    print(f'O segundo digito verificador deste CPF é {calc2}')
else:
    calc2 = 0
    print(f'O segundo digito verificador deste CPF é {calc2}')

print(f'Este CPF será: {n1} {n2} {n3} . {n4} {n5} {n6} . {n7} {n8} {n9} - {calc1} {calc2}')
print(f'O CPF original é: {CPF}')

if calc1 == int(CPF[9]) and calc2 == int(CPF[10]):
    print('Este CPF é válido')
else:
    print('Este CPF é inválido')
