from os import system

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

def read_ecu_sys(num_ecuations):
    ec_sys = []

    for ecuation in range(num_ecuations):
        ec_sys.append([])
        for coef in  range(num_ecuations + 1):
            ec_sys[ecuation].append(0)
    
    for ecuation in range(num_ecuations):
        print('\n\nIngresa los coeficientes de tu ecuación {}:\n'.format(ecuation + 1))
        for coef in  range(num_ecuations + 1):
            if coef < num_ecuations:
                str_coef = '\tx{}: '.format(coef + 1)
            else:
                str_coef = '\t= cte: '
            ec_sys[ecuation][coef] = read_num(str_coef)

    return ec_sys

def order_ecu_sys(matrix_sys):
    row = 1
    num_ecuations = len(matrix_sys)
    diagon = 0
    has_solution = True

    while row < num_ecuations:
        if abs(matrix_sys[0][0]) < abs(matrix_sys[row][0]):
            matrix_sys[0], matrix_sys[row] = matrix_sys[row], matrix_sys[0]
        row += 1
    
    while diagon < num_ecuations:
        row = diagon + 1

        if has_solution:
            while matrix_sys[diagon][diagon] == 0:
                try:
                    matrix_sys[0], matrix_sys[row] = matrix_sys[row], matrix_sys[0]
                except IndexError:
                    has_solution = False
                    break
                row += 1

        else:
            break

        diagon += 1

    if not has_solution:
        ordered_matrix = has_solution
    else:
        ordered_matrix = matrix_sys

    return ordered_matrix
                
def print_error_message():
    print('ERROR!!\n')
    print('¡No hay una solución para el sistema de ecuaciones que introduciste!\n')
    print('Intenta introducir uno nuevo\n\n')
    system('pause')
    system('cls')

def create_m_tri_sup(M):
    num_ecuations = len(M)
    col = 0
    coef = len(M[0])# num de coef por ec, incluido el resultado

    while col < (num_ecuations-1):
        row = num_ecuations - 1
        while row > col:
            piv = M[row][col] / M[col][col]

            for i in range(coef):
                M[row][i] = (M[col][i] * piv) - M[row][i]  

            row -= 1
        col += 1

    return M

def fill_vec_res(M):
    n_unkno = len(M)
    Res = []
    num_coef = len(M[0]) - 1

    col = row = n_unkno - 1

    while col >= 0 :
        while row >= 0:
            aux = M[row][num_coef]
            if len(Res) != 0:
                for i in range(len(Res)):
                    aux -= M[row][-i-2]*Res[i]
            aux /= M[row][row]
            Res.append(aux)
            row -= 1
        col -= 1

    return Res[::-1]

def print_res(Res):
    print('\n\nEl resultado de las incógnitas:\n\n')
    for i in range(len(Res)):
        print('\tx{} = {}'.format(i+1, Res[i]))
    print('\n\n')

def gauss_method():
    while True:
        num_ecuations = abs(int(read_num('Ingresa el número de ecuaciones de tu sistema: ')))
        M = read_ecu_sys(num_ecuations)
        M = order_ecu_sys(M)

        if isinstance(M, list):
            break
        else:
            print_error_message()

    M = create_m_tri_sup(M)
    Res = fill_vec_res(M)
    print_res(Res)

def run():
    system('cls')
    print('Bienvenido al método de Gauss\n\n')
    gauss_method()
    system('pause')
    system('cls')
    
if __name__ == '__main__':
    repeat = True

    while repeat:
        run()
        repeat = _simple_bool_ans('¿Deseas encontrar solución a un nuevo sistema de ecuaciones?')
        