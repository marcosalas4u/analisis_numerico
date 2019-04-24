from os import system
from matplotlib import pyplot as plt
import numpy as np

def _simple_bool_ans(str_chain):
    option = None

    print(str_chain)
    print('\t[Cualquier tecla] - Sí')
    print('\t[Enter] - No')

    option = bool(input())
    
    return option

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
    table = np.zeros([2,n])
    
    for point in range(n):
        print('\n\nPunto {}:\n'.format(point + 1))
        str_coef = '\tx{}: '.format(point + 1)
        table[0][point] = read_num(str_coef)
        str_coef = '\tf(x{}): '.format(point + 1)
        table[1][point] = read_num(str_coef)

    return table

def create_identity_m(M):
    n_coef = len(M[0])
    #num de coef por ec, incluido el resultado
    num_ec = len(M)
    pos_b_res = len(M[0]) - 1

    res = []

    for col in range(num_ec):
        for row in range(num_ec):
            if col != row:
                piv = M[row][col] / M[col][col]
                for i in range(n_coef):
                    M[row][i] = (M[col][i] * piv) - M[row][i]
    
    #realizando las divisiones
    #para obtener la matriz identidad

    for row in range(len(M)):
        aux = M[row][pos_b_res] / M[row][row]
        res.append(aux)
    
    return res

def fill_m_linear_(table_points):
    M = np.zeros([2,3])
    n_points = len(table_points[0])

    for i in range(n_points):
        M[0][0] += (table_points[0][i]**2)
        M[0][1] += table_points[0][i]
        M[0][2] += ( table_points[0][i] * table_points[1][i] )
        M[1][2] += table_points[1][i]

    M[1][0] = M[0][1]
    M[1][1] = n_points

    return M

def linear_regresion(table_points, x_eval):
    M = fill_m_linear_(table_points)
    res_m_b = create_identity_m(M)
    return (res_m_b[0]*x_eval) + res_m_b[1]

def lagrange_interpolation(table_points, x_interpolation):
    result = 0
    n_points = len(table_points)
    
    for j in range(n_points):
        l_j = 1
        for i in range(n_points):
            if i == j:
                continue
            l_j *= ( (x_interpolation - table_points[0][i]) / (table_points[0][j] - table_points[0][i]) )
        result += (table_points[1][j] * l_j)

    return result

def start():
    n_points = int(read_num('\n\tIngresa el número de puntos con que cuentas: '))
    table_points = read_n_points(n_points)
    another_point = True

    while another_point:
        system('cls')
        print('A continuación se graficarán los puntos de la tabla ingresada')
        print('Analízala, después cierra la ventana\n\n')
        system('pause')

        plt.scatter(table_points[0], table_points[1], color = 'blue', marker = 'o', s = 30)
        plt.title('Puntos ingresados')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.show()
        
        do_interpolation = _simple_bool_ans('\n\nSegún tu criterio\n¿Deseas realizar una regresión LINEAL?')
        x_eval = read_num('\n\nIngresa el valor de x que deseas EVALUAR: ')
        system('cls')
        
        if do_interpolation:
            str_choice = 'Regresión Lineal'
            result = linear_regresion(table_points, x_eval)
        else:
            str_choice = 'Interpolación de Lagrange'
            result = lagrange_interpolation(table_points, x_eval)

        print('A continuación se graficarán:\n')
        print('\tlos puntos de la tabla ingresada\n')
        print('\ty el punto encontrado por {}: \n\t\tf({}) = {}\n\n'.format(str_choice, x_eval, result))
        system('pause')

        plt.scatter(table_points[0], table_points[1], label = 'Puntos Ingresados',color = 'blue', marker = 'o', s = 30)
        plt.scatter(x_eval, result, label = str_choice, color = 'red', marker = 'o', s = 30)
        plt.title(str_choice)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.show()

        another_point = _simple_bool_ans('\n\nCon los puntos ya ingresados\n¿Deseas interpolar otro valor para x?')

def run():
    system('cls')
    print('Bienvenido a la interpolación\n\n')
    start()
    system('pause')
    system('cls')
    
if __name__ == '__main__':
    repeat = True

    while repeat:
        run()
        repeat = _simple_bool_ans('¿Deseas realizar otra interpolación?')
        