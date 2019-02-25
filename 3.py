from os import system

def ask_to_repeat():
    option = None

    system('pause')
    system('cls')

    print('¿Deseas encontrar otra raíz?')
    print('\t[Cualquier tecla] - Si')
    print('\t[Enter] - No')

    option = bool(input())
    
    return option

def _false_rule(interv, poly):
    f_a = eval_poly(poly, interv[0])
    f_b = eval_poly(poly, interv[1])
    a = interv[0]
    b = interv[1]

    return float( ((a * f_b) - (b * f_a)) / (f_b - f_a) )

def rel_err(val_ver, val_calc):
    return abs( (val_ver - val_calc) / val_ver ) * 100

def read_polynomial():
    grade = abs(int(input('Ingresa el grado del polonomio: ')))
    poly = []
    print('\nIngresa los coeficientes de: \n')

    while grade >= 0:
        if grade != 0:
            poly.append(float(input('\tx^{}: '.format(grade))))
        else:
            poly.append(float(input('\tcte: ')))
        grade -= 1

    return poly[::-1]

def eval_poly(poly, x):
    result = 0.0

    for i in range(len(poly)):
        result += poly[i]*x**i

    return result

def _valid_interval(poly, interv):
    valid = True

    if eval_poly(poly,interv[0]) * eval_poly(poly,interv[1]) >= 0:
        valid = False
        # print('El intervalo ingresado no es apto para empezar a iterar\n\n')
        # system('pause')

    return valid

def read_interval(poly):
    interval = [0, 0]

    while not _valid_interval(poly, interval):
        system('cls')
        print('Ingresa valores para el intervalo:')
        interval[0] = float(input('\tlímite izquierdo: '))
        interval[1] = float(input('\tlímite derecho: '))

    return interval

def stop_criter(poly, x):
    stop = False

    if abs(eval_poly(poly, x)) < 10**(-15):
        stop = True

    return stop

def print_poly(poly):
    grade = len(poly) - 1
    str_poly = 'f(x) = '
    while grade >= 0:
        
        if poly[grade] != 0:

            if poly[grade] < 0:
                str_poly += ' - '

            if abs(poly[grade]) != 1 or grade == 0:
                str_poly += '{}'.format(abs(int(poly[grade])))
            
            if grade > 0:
                str_poly += 'x'

            if grade > 1:
                str_poly += '^{}'.format(grade)

            if poly[grade-1] > 0 and grade > 0:
                str_poly += ' + '

        grade -= 1

    print(str_poly)

def false_rule_method(poly):
    
    interval = read_interval(poly)
    stop = False

    iterations = 0

    while not stop:
        Xr = _false_rule(interval, poly)
        stop = stop_criter(poly, Xr)
        criterio = eval_poly(poly, Xr) * eval_poly(poly, interval[0])
        iterations += 1

        if criterio > 0:
            interval[0] = Xr
        elif criterio < 0:
            interval[1] = Xr

    system('cls')
    print('Una raíz real de la función: \n\t')
    print_poly(poly)
    print('\n\tes Xr = {}'.format(Xr))
    print('\n\ny fue calculada con {} iteraciones'.format(iterations))
    print('\npor el método de la Regla falsa\n\n\n')
    
if __name__ == '__main__':
    repeat = True

    while repeat:
        system('cls')
        print('Bienvenido al método de la Regla falsa\n\n')
        false_rule_method(read_polynomial())
        repeat = ask_to_repeat()
    