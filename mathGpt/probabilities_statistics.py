from math import pi, e, tau, inf, sqrt, exp, log, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, radians
from sympy import symbols, parse_expr, integrate, lambdify, diff
import numpy as np
import math

def statistics_function(numbers, function):
    numbers = numbers.split(',')
    numbers = [float(number) for number in numbers]
    numbers = np.array(numbers)
    if function == 'mean':
        return np.mean(numbers)
    elif function == 'median':
        return np.median(numbers)
    elif function == 'mode':
        return np.mode(numbers)
    elif function == 'standard deviation':
        return np.std(numbers)
    elif function == 'variance':
        return np.var(numbers)
    else:
        return None