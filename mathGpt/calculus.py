import numpy as np
from math import pi, e, tau, inf, sqrt, exp, log, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, radians
from sympy import symbols, parse_expr, integrate, lambdify, diff
from scipy.integrate import quad
import math
import sympy as sp

def limit(expresion, h):
    try:
        x = symbols('x')
        expresion = expresion.replace('^', '**')
        expresion = parse_expr(expresion)
        limit = expresion.limit(x, h)
        return limit
    except Exception as e:
        print("Ha ocurrido un error:", e)
        return None

def integral(expresion_texto):
    try:
        x = symbols('x')
        expresion_texto = expresion_texto.replace('^', '**')
        expresion_simbolica = parse_expr(expresion_texto)
        integral = integrate(expresion_simbolica, x)
        return integral
    except Exception as e:
        print("Ha ocurrido un error:", e)
        return None

def calculate_integral(expresion_texto, superior, inferior):
    function = integral(expresion_texto)
    function_text = str(function)
    x = symbols('x')
    function = lambdify(x, function, 'numpy')
    return function(superior) - function(inferior), function_text

def derivative(expresion_texto):
    try:
        x = symbols('x')
        expresion_simbolica = parse_expr(expresion_texto)
        derivative = diff(expresion_simbolica, x)
        return derivative
    except Exception as e:
        print("Ha ocurrido un error:", e)

def calculate_derivative(expresion_texto, number):
    function = derivative(expresion_texto)
    function_text = str(function)
    x = symbols('x')
    function = lambdify(x, function, 'numpy')
    return function(number), function_text

def volume_discs(radius_func, interval_start, interval_end):
    def integrand(x):
        return math.pi * radius_func(x)**2

    volume = quad(integrand, interval_start, interval_end)
    return volume[0]

def volume_hollow_cylinders(outer_radius_func, inner_radius_func, interval_start, interval_end):
    def integrand(x):
        return math.pi * (outer_radius_func(x)**2 - inner_radius_func(x)**2)

    volume = quad(integrand, interval_start, interval_end)
    return volume[0]

def differentials(func, variables, point):
    partials = {variable: sp.diff(func, variable).subs(variable, point) for variable in variables}
    total_differential = sp.diff(func, *variables).subs(variables, [point] * len(variables))
    result = {"partials": partials, "total": total_differential}
    return result

def rate_of_change(func, variable, point):
    derivative = sp.diff(func, variable)
    rate = derivative.subs(variable, point)
    return rate

def optimize(func, variable, interval):
    critical_points = sp.solve(sp.diff(func, variable), variable)
    valid_points = [point for point in critical_points if point > interval[0] and point < interval[1]]
    values = [func.subs(variable, point) for point in valid_points]
    optimum_index = values.index(min(values))
    return valid_points[optimum_index]

def derivative_applications(operation_type, func, variable, parameter):
    try:
        parameter = float(parameter)
    except:
        parameter = [float(number) for number in parameter.split(",")]
    func = lambdify(variable, func, 'numpy')
    if operation_type == "rate_of_change":
        return rate_of_change(func, variable, parameter)
    elif operation_type == "optimize":
        return optimize(func, variable, parameter)
    elif operation_type == "differentials":
        return differentials(func, variable, parameter)

def volume_revolution(func, variable, interval, axis):
    if axis == "x":
        return volume_discs(func, interval[0], interval[1])
    elif axis == "y":
        return volume_discs(lambda x: x, interval[0], interval[1])
    elif axis == "x=y":
        return volume_hollow_cylinders(lambda x: x, func, interval[0], interval[1])
    else:
        return False

def length_curve(func, variable, interval):
    x = sp.symbols(variable)
    derivative = sp.diff(func(x), x)
    integrand = sp.sqrt(1 + derivative**2)
    length, _ = quad(lambda x: integrand.subs(variable, x), interval[0], interval[1])
    return length


def area_surface(func, variable, interval):
    x = sp.symbols(variable)
    derivative = sp.diff(func(x), x)
    integrand = 2 * pi * derivative * sp.sqrt(1 + derivative**2)
    area, _ = quad(lambda x: integrand.subs(variable, x), interval[0], interval[1])
    return area

def integral_applications(operation_type, func, variable, interval, axis):
    interval = interval.split(",")
    interval = [float(number) for number in interval]
    func = lambdify(variable, func, 'numpy')
    print(func, variable, interval, axis)
    if operation_type == "volume_revolution":
        return volume_revolution(func, variable, interval, axis)
    elif operation_type == "length_curve":
        return length_curve(func, variable, interval)
    elif operation_type == "area_surface":
        return area_surface(func, variable, interval)
    else:
        return False