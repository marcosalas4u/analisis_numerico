from os import system
from sympy import symbols, sympify, diff

def _simple_bool_ans(str_chain):
    option = None

    print(str_chain)
    print('\t[Cualquier tecla] - Sí')
    print('\t[Enter] - No')

    option = bool(input())
    
    return option

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

    return poly[::-1]#[cte,x,x^2,..,x^n]

def eval_poly(poly, x):
    result = 0.0

    for i in range(len(poly)):
        result += poly[i]*(x**i)

    return result

def _stop_criter(poly, Xr, is_algebraic_polynomial):
    stop = False
    tol = 10**(-10)

    if is_algebraic_polynomial:
        if abs(eval_poly(poly, Xr)) < tol:
            stop = True
    else:
        x = symbols('x')
        if abs(poly.subs(x, Xr)) < tol:
            stop = True

    return stop

def print_poly(poly,func):
    grade = len(poly) - 1
    str_poly = '{}(x) = '.format(func)
    while grade >= 0:
        
        if poly[grade] != 0:

            if poly[grade] < 0:
                str_poly += ' - '

            if abs(poly[grade]) != 1 or grade == 0:
                str_poly += '{}'.format(abs(int(poly[grade])))
            
            if grade > 0:
                str_poly += 'x'

            if grade > 1:
                str_poly += '**{}'.format(grade)

            if poly[grade-1] > 0 and grade > 0:
                str_poly += ' + '

        grade -= 1

    print(str_poly)

def derivative(poly):
    poly_grade = len(poly) - 1
    poly = poly[::-1]#[x^n,..,x^2,x,cte]
    poly_derivative = poly[:poly_grade:]#[x^n,..,x^2,x]

    for i in range(len(poly_derivative)):
        poly_derivative[i] *= poly_grade
        poly_grade -= 1

    return poly_derivative[::-1]#[cte,x,x^2,..,x^n]

def read_sympy_polynomial(func):
    print('\n\nIngresa una {}(x) de una forma comprensible para python'.format(func))
    print('\nEjemplo: {}(x) = 2*x*sin(x**2) - exp(x)'.format(func))
    print('\nNota: Debes escribir únicamente x minúscula')
    return sympify(input('\n\n\t{}(x) = '.format(func)))

def newton_raphson_metod(is_algebraic_polynomial):

    if is_algebraic_polynomial:
        poly = read_polynomial()
        poly_derivative = derivative(poly)
    else:
        x = symbols('x')
        poly = read_sympy_polynomial('f')

        if _simple_bool_ans('\n¿Tienes la derivada de tu f(x)?'):
            system('cls')
            poly_derivative = read_sympy_polynomial('f\'')
        else:
            poly_derivative = diff(poly, x)
    
    Xr = float(input('\n\nIngresa el punto inicial para el método: '))
    stop = False
    iterations = 0

    while not stop:
        if is_algebraic_polynomial:
            Xr -= eval_poly(poly, Xr) / eval_poly(poly_derivative, Xr)
        else:
            Xr -= poly.subs(x , Xr) / poly_derivative.subs(x, Xr)

        stop = _stop_criter(poly, Xr, is_algebraic_polynomial)
        iterations += 1


    system('cls')
    print('Una raíz real de la función: \n\t')

    if is_algebraic_polynomial:
        print_poly(poly,'f')
    else:
        print('f(x) = {}'.format(poly))

    print('\n\tes Xr = {}'.format(Xr))
    print('\n\ny fue calculada con {} iteraciones'.format(iterations))
    print('\npor el método de Newton-Raphson\n\n\n')

def run():
    system('cls')
    print('Bienvenido al método de Newton-Raphson\n\n')
    is_algebraic_polynomial = _simple_bool_ans('¿Es tu f(x) un polinomio algebraico?')
    system('cls')
    newton_raphson_metod(is_algebraic_polynomial)
    system('pause')
    system('cls')
    
if __name__ == '__main__':
    repeat = True

    while repeat:
        run()
        repeat = _simple_bool_ans('¿Deseas encontrar otra raíz?')
        