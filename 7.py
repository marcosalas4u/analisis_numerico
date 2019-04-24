from os import system
from matplotlib import pyplot as plt
import numpy as np

def _simple_bool_ans(str_chain):
    print(str_chain)
    print('\t[Cualquier tecla] - Sí')
    print('\t[Enter] - No')

    return bool(input())

def read_num(str_chain):
    while True:
        try:
            num =  float(input(str_chain))
            break
        except ValueError:
            print('\n\nERROR!! \nIngresa un número \n\n')
            system('pause')
            system('cls')
    return num

def read_n_points(n):
    table = np.zeros([n,2])
    
    for point in range(n):
        print('\n\nPunto {}:\n'.format(point + 1))
        str_coef = '\tx{}: '.format(point + 1)
        table[0][point] = read_num(str_coef)
        str_coef = '\tf(x{}): '.format(point + 1)
        table[1][point] = read_num(str_coef)

    return table

def lagrange_interpolation():
    n_points = int(read_num('\n\tIngresa el número de puntos con que cuentas: '))
    table_points = read_n_points(n_points)
    another_point = True

    while another_point:

        x_interpolation = read_num('\n\nIngresa el valor de x que deseas INTERPOLAR: ')
        result = 0
        for j in range(n_points):
            l_j = 1
            for i in range(n_points):
                if i == j:
                    continue
                l_j *= ( (x_interpolation - table_points[0][i]) / (table_points[0][j] - table_points[0][i]) )
            result += (table_points[1][j] * l_j)

        print('\n\nf({}) = {}\n'.format(x_interpolation, result))
        print('A continuación se graficarán:')
        print('\tlos puntos de la tabla ingresada(en color azul)')
        print('\ty el punto encontrado por la interpolación(en color rojo)\n\n')
        system('pause')

        plt.scatter(np.array(table_points[0]), np.array(table_points[1]), color = 'blue', marker = 'o', s = 30)
        plt.scatter(x_interpolation, result, label = 'Interpolación', color = 'red', marker = 'o', s = 30)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Interpolación\nPolinómica\nde Lagrange')
        plt.legend()
        plt.show()

        another_point = _simple_bool_ans('Con los puntos ya ingresados\n¿Deseas interpolar otro valor para x?')

def run():
    system('cls')
    print('Bienvenido a la interpolación polinómica en la forma de Lagrange\n\n')
    lagrange_interpolation()
    print('\n\n\n')
    
if __name__ == '__main__':
    repeat = True

    while repeat:
        run()
        repeat = _simple_bool_ans('¿Deseas realizar otra interpolación polinómica?')
        