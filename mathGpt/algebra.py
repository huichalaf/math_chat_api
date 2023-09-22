from math import pi, e, tau, inf, sqrt, exp, log, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, radians
from sympy import symbols, parse_expr, integrate, lambdify, diff
import numpy as np
import math, cmath

add = lambda number1, number2: number1 + number2
substract = lambda number1, number2: number1 - number2
multiply = lambda number1, number2: number1 * number2
divide = lambda number1, number2: number1 / number2
power = lambda number1, number2: number1 ** number2
square_root = lambda number1, number2: number1 ** (1 / number2)
logarithm_function = lambda base, number: log(number) / log(base)

def evaluate_expressions(expresion):
    try:
        expresion = expresion.replace('^', '**')
        expresion = parse_expr(expresion)
        resultado = expresion.evalf()
        return resultado
    except Exception as e:
        print("Ha ocurrido un error:", e)
        return None

def boolean_algebra(expresion):
    try:
        expresion = expresion.replace('AND', '&')
        expresion = expresion.replace('OR', '|')
        expresion = expresion.replace('NOT', '~')
        expresion = parse_expr(expresion)
        resultado = expresion.evalf()
        return resultado
    except Exception as e:
        print("Ha ocurrido un error:", e)
        return None