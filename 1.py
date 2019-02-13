from os import system
from math import radians, sin, exp

def factorial(n):
    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n-1)

    return fact

def menu():
    option = None

    while option != 's' and option != 'e':
        system('cls')

        print('Selecciona una función para evaluar')
        print('\t[s]en(x)')
        print('\t[e](x)')

        option = input()

    if option == 's':
        option = 'sen(x)'

    elif option == 'e':
        option = 'e(x)'

    return option

def ask_to_repeat():
    option = None

    system('pause')
    system('cls')

    print('¿Deseas evaluar otro valor?')
    print('\t[Cualquier tecla] - Si')
    print('\t[Enter] - No')

    option = bool(input())
    
    return option

def my_sin(x):
    acum = 0.0
    calc = 1
    n = 0

    while abs(calc) > (10**(-15)):
        aux = 2*n + 1
        calc = ((-1)**n) * (x**aux) / factorial(aux)
        acum += calc
        n += 1

    return [acum,n]

def my_exp(x):
    acum = 0.0
    calc = 1
    n = 0

    while calc > (10**(-15)):
        calc = (x**n) / factorial(n)
        acum += calc
        n += 1

    return [acum,n]

def rel_err(val_ver, val_calc):
    return round(abs( (val_ver - val_calc) / val_ver ) * 100, 4)

def run():
    funct = menu()

    system('cls')

    num = float(input('Ingresa x para evaluar {}: '.format(funct)))

    if funct == 'sen(x)':
        evaluation = my_sin(radians(num))
        real_val = sin(radians(num))

    elif funct == 'e(x)':
        evaluation = my_exp(num)
        real_val = exp(num)

    print('\n\nEvaluando {} con {} y en {} iteraciones'.format(funct, num, evaluation[1]))
    print('\n\t{} = {}'.format(funct, evaluation[0]))

    print('\nValor real de python:')
    print('\n\t{} = {}'.format(funct, real_val))

    print('\n\nError relativo: {}%\n\n'.format(rel_err(real_val, evaluation[0])))
    
if __name__ == '__main__':
    repeat = True

    while repeat:
        run()
        repeat = ask_to_repeat()
    