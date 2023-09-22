from math import pi, e, tau, inf, sqrt, exp, log, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, radians
from sympy import symbols, parse_expr, integrate, lambdify, diff
import numpy as np
import math

def matrix_determinant(matrix):
    #transformamos la matriz a un array
    matrix = np.array(matrix)
    return np.linalg.det(matrix)

def matrix_multiplication(matrix1, matrix2):
    if ';' not in matrix1 or ';' not in matrix2:
        return None
    if ',' not in matrix1 or ',' not in matrix2:
        return None
    matrix1 = matrix1.split(';')
    matrix2 = matrix2.split(';')
    matrix1 = [row.split(',') for row in matrix1]
    matrix2 = [row.split(',') for row in matrix2]
    matrix1 = [[float(number) for number in row] for row in matrix1]
    matrix2 = [[float(number) for number in row] for row in matrix2]
    matrix1_real = np.array(matrix1)
    matrix2_real = np.array(matrix2)
    try:
        return np.matmul(matrix1_real, matrix2_real)
    except Exception as e:
        print("Ha ocurrido un error:", e)
        return None
def matrix_transpose(matrix):
    matrix = np.array(matrix)
    return np.transpose(matrix)

def matrix_inverse(matrix):
    matrix = np.array(matrix)
    return np.linalg.inv(matrix)

def eigenvalues(matrix):
    matrix = np.array(matrix)
    return np.linalg.eigvals(matrix)

def eigenvectors(matrix):
    matrix = np.array(matrix)
    return np.linalg.eig(matrix)

def matrix_rank(matrix):
    matrix = np.array(matrix)
    return np.linalg.matrix_rank(matrix)

def matrix_trace(matrix):
    matrix = np.array(matrix)
    return np.trace(matrix)

def matrix_solve(matrix, vector):
    if ';' not in matrix or ',' not in matrix:
        return None
    matrix = matrix.split(';')
    vector = vector.split(',')
    matrix = [row.split(',') for row in matrix]
    matrix = [[float(number) for number in row] for row in matrix]
    vector = [float(number) for number in vector]
    matrix = np.array(matrix)
    vector = np.array(vector)
    try:
        return np.linalg.solve(matrix, vector)
    except np.linalg.LinAlgError:
        return "matriz singular"

def matrix_alone_operations(matrix, operation_type):
    if ';' not in matrix or ',' not in matrix:
        return None
    matrix = matrix.split(';')
    for i in range(len(matrix)):
        matrix[i] = matrix[i].split(',')
        for j in range(len(matrix)):
            matrix[i][j] = float(matrix[i][j])
    if operation_type == "determinant":
        try:
            return matrix_determinant(matrix)
        except np.linalg.LinAlgError:
            return "matriz singular"
    elif operation_type == "transpose":
        try:
            return matrix_transpose(matrix)
        except np.linalg.LinAlgError:
            return "matriz singular"
    elif operation_type == "inverse":
        try:
            return matrix_inverse(matrix)
        except np.linalg.LinAlgError:
            return "matriz singular"
    elif operation_type == "eigenvalues":
        try:
            return eigenvalues(matrix)
        except np.linalg.LinAlgError:
            return "matriz singular"
    elif operation_type == "eigenvectors":
        try:
            return eigenvectors(matrix)
        except np.linalg.LinAlgError:
            return "matriz singular"
    elif operation_type == "rank":
        try:
            return matrix_rank(matrix)
        except np.linalg.LinAlgError:
            return "matriz singular"
    elif operation_type == "trace":
        try:
            return matrix_trace(matrix)
        except np.linalg.LinAlgError:
            return "matriz singular"
    else:
        return None
