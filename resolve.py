# -*- coding: utf-8 -*-

# Caulando as raízes de uma equação do segundo grau

# Criado por: Pedro Moraes

active = True

def raizes(a, b, c):
    delta = (b ** 2 - 4*a*c)
    x_positive = (-b + delta ** (1/2)) / (2 * a)
    x_negative = (-b - delta ** (1/2)) / (2 * a)

    print(f'\nValor de X positivo: {x_positive}')
    print(f'\nValor de X negativo: {x_negative}\n')


while active:
    print('\tCalculando as raízes de uma equação do segundo grau:\n')
    a = float(input('Informe o valor de a: '))
    b = float(input('Informe o valor de b: '))
    c = float(input('Informe o valor de c: '))
    raizes(a,b,c)

    continua = input("Se quiser sair digite 'quit' ou aperte Enter para iniciar um novo cáuculo:  ")
    if (continua.lower() == 'quit'):
        print('Até logo!')
        break