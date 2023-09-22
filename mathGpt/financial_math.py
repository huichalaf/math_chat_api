import math
from scipy.optimize import root_scalar

def interes_simple(p, r, t):
    return p * r * t
def interes_compuesto(p, r, t):
    return p * (1 + r)**t - p
def vpn(flujos, tasa_descuento):
    return sum([flujo / (1 + tasa_descuento)**t for t, flujo in enumerate(flujos)])
def tir(flujos):
    def tir_func(tasa):
        return sum([flujo / (1 + tasa)**t for t, flujo in enumerate(flujos)])
    
    result = root_scalar(tir_func, bracket=[-1.0, 1.0])
    return result.root
def pago_mensual_hipoteca(p, r, n):
    return p * r * (1 + r)**n / ((1 + r)**n - 1)

valor_futuro = lambda p, r, t: p * (1 + r)**t
descuento_flujo = lambda flujo, tasa, tiempo: flujo / (1 + tasa)**tiempo
roi = lambda ganancias, costos: (ganancias - costos) / costos * 100
tasa_efectiva = lambda tasa_nominal, frecuencia: (1 + tasa_nominal / frecuencia)**frecuencia - 1
valor_presente = lambda flujos, tasa_descuento: sum([flujo / (1 + tasa_descuento)**t for t, flujo in enumerate(flujos)])
indice_rentabilidad = lambda inversion_inicial, flujos: vpn(flujos, 0) / inversion_inicial
wacc = lambda r_e, r_d, e, d, v: (e/v) * r_e + (d/v) * r_d
tasa_equivalente = lambda tasa, periodos: (1 + tasa)**periodos - 1

def wacc(r_e, r_d, e, d, v):
    return (e/v) * r_e + (d/v) * r_d
def periodo_recuperacion(flujos, inversion_inicial):
    for t, flujo in enumerate(flujos):
        if flujo > 0:
            return t
    return None
def apv(flujos, tasa_descuento, deuda_actual):
    vp_flujos = sum([flujo / (1 + tasa_descuento)**t for t, flujo in enumerate(flujos)])
    return vp_flujos - deuda_actual
def punto_equilibrio_unidades(costos_fijos, costo_variable_por_unidad, precio_venta_por_unidad):
    return costos_fijos / (precio_venta_por_unidad - costo_variable_por_unidad)

margen_contribucion_por_unidad = lambda precio_venta_por_unidad, costo_variable_por_unidad: precio_venta_por_unidad - costo_variable_por_unidad

def capm(tasa_libre_riesgo, beta, prima_mercado):
    return tasa_libre_riesgo + beta * prima_mercado
def indice_solvencia(activo_total, pasivo_total):
    return activo_total / pasivo_total
def rotacion_activos(ventas_netas, activo_promedio):
    return ventas_netas / activo_promedio
def rentabilidad_activos(utilidad_neta, activo_promedio):
    return utilidad_neta / activo_promedio
def indice_liquidez(activo_circulante, pasivo_circulante):
    return activo_circulante / pasivo_circulante