import math

distance = lambda x1, y1, x2, y2: math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
angle = lambda x1, y1, x2, y2: math.degrees(math.atan2(y2 - y1, x2 - x1))
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
distance_to_line = lambda x, y, x1, y1, x2, y2: abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
midpoint = lambda x1, y1, x2, y2: ((x1 + x2) / 2, (y1 + y2) / 2)
polar_to_cartesian = lambda r, theta_degrees: (r * math.cos(math.radians(theta_degrees)), r * math.sin(math.radians(theta_degrees)))
cartesian_to_polar = lambda x, y: (math.sqrt(x**2 + y**2), math.degrees(math.atan2(y, x)))
parametric_to_cartesian = lambda t, x, y: (x(t), y(t))
cartesian_to_parametric = lambda x, y: (lambda t: x, lambda t: y)
polar_to_parametric = lambda t, r, theta_degrees: (r(t), theta_degrees(t))
parametric_to_polar = lambda t, x, y: (lambda t: x, lambda t: y)
circle_area = lambda radius: math.pi * radius**2
circle_circumference = lambda radius: 2 * math.pi * radius
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
angle_radians = lambda x1, y1, x2, y2: math.atan2(y2 - y1, x2 - x1)
square_area = lambda side: side**2
rectangle_area = lambda base, height: base * height
cylinder_volume = lambda radius, height: math.pi * radius**2 * height
sphere_volume = lambda radius: (4/3) * math.pi * radius**3
cone_volume = lambda radius, height: (1/3) * math.pi * radius**2 * height
hypotenuse = lambda a, b: math.sqrt(a**2 + b**2)

def cartesian_transform(operation_type, coordinates):
    try:
        coordinates = [float(i) for i in coordinates.split(',')]
    except:
        coordinates = coordinates.replace(' ', '')
        coordinates = coordinates.replace('(', '')
        coordinates = coordinates.replace(')', '')
        coordinates = coordinates.replace('[', '')
        coordinates = coordinates.replace(']', '')
        coordinates = coordinates.split(',')
        coordinates = [float(i) for i in coordinates]
    if operation_type == "polar_to_cartesian":
        try:
            r = coordinates[0]
            theta_degrees = coordinates[1]
            cartesian = polar_to_cartesian(r, theta_degrees)
            return cartesian
        except:
            return False
    elif operation_type == "cartesian_to_polar":
        try:
            print("si")
            x = coordinates[0]
            y = coordinates[1]
            print(x, y)
            polar = cartesian_to_polar(x, y)
            print(polar)
            return polar
        except:
            return False
    elif operation_type == "parametric_to_cartesian":
        try:
            t = coordinates[0]
            x = coordinates[1]
            y = coordinates[2]
            cartesian = parametric_to_cartesian(t, x, y)
            return cartesian
        except:
            return False
    elif operation_type == "cartesian_to_parametric":
        try:
            x = coordinates[0]
            y = coordinates[1]
            parametric = cartesian_to_parametric(x, y)
            return parametric
        except:
            return False
    elif operation_type == "polar_to_parametric":
        try:
            t = coordinates[0]
            r = coordinates[1]
            theta_degrees = coordinates[2]
            parametric = polar_to_parametric(t, r, theta_degrees)
            return parametric
        except:
            return False
    elif operation_type == "parametric_to_polar":
        try:
            t = coordinates[0]
            x = coordinates[1]
            y = coordinates[2]
            polar = parametric_to_polar(t, x, y)
            return polar
        except:
            return False
    else:
        return False

def cartesian_functions(operation_type, coordinates):
    if operation_type == "distance_to_line":
        try:
            coordenadas1 = coordinates[0]
            coordenadas2 = coordinates[1]
            coordenadas2_1 = coordenadas2[0]
            coordenadas2_2 = coordenadas2[1]
            distancia = distance_to_line(coordenadas1[0], coordenadas1[1], coordenadas2_1[0], coordenadas2_1[1], coordenadas2_2[0], coordenadas2_2[1])
            return distancia
        except:
            return False
    elif operation_type == "slope":
        try:
            coordenadas1 = coordinates[0]
            coordenadas2 = coordinates[1]
            pendiente = slope(coordenadas1[0], coordenadas1[1], coordenadas2[0], coordenadas2[1])
            return pendiente
        except:
            return False
    elif operation_type == "distance":
        try:
            coordenadas1 = coordinates[0]
            coordenadas2 = coordinates[1]
            distancia = distance(coordenadas1[0], coordenadas1[1], coordenadas2[0], coordenadas2[1])
            return distancia
        except:
            return False
    elif operation_type == "angle":
        try:
            coordenadas1 = coordinates[0]
            coordenadas2 = coordinates[1]
            angulo = angle(coordenadas1[0], coordenadas1[1], coordenadas2[0], coordenadas2[1])
            return angulo
        except:
            return False
    elif operation_type == "hipotenuse":
        try:
            a = coordinates[0]
            b = coordinates[1]
            hipotenusa = hypotenuse(a, b)
            return hipotenusa
        except:
            return False
    elif operation_type == "midpoint":
        try:
            coordenadas1 = coordinates[0]
            coordenadas2 = coordinates[1]
            punto_medio = midpoint(coordenadas1[0], coordenadas1[1], coordenadas2[0], coordenadas2[1])
            return punto_medio
        except:
            return False
    else:
        return False

def geometric_functions(operation_type, coordinates):
    if operation_type=="square_area":
        try:
            side = coordinates[0]
            area = square_area(side)
            return area
        except:
            return False
    elif operation_type=="rectangle_area":
        try:
            base = coordinates[0]
            height = coordinates[1]
            area = rectangle_area(base, height)
            return area
        except:
            return False
    elif operation_type=="circle_area":
        try:
            radius = coordinates[0]
            area = circle_area(radius)
            return area
        except:
            return False
    elif operation_type=="circle_circumference":
        try:
            radius = coordinates[0]
            circumference = circle_circumference(radius)
            return circumference
        except:
            return False
    elif operation_type=="cylinder_volume":
        try:
            radius = coordinates[0]
            height = coordinates[1]
            volume = cylinder_volume(radius, height)
            return volume
        except:
            return False
    elif operation_type=="sphere_volume":
        try:
            radius = coordinates[0]
            volume = sphere_volume(radius)
            return volume
        except:
            return False
    elif operation_type=="cone_volume":
        try:
            radius = coordinates[0]
            height = coordinates[1]
            volume = cone_volume(radius, height)
            return volume
        except:
            return False
    else:
        return False

def trigonometric_function(function, number, tipo):
    if tipo == 'degrees':
        number = radians(number)
    if function == 'sin' or function == 'sine':
        return sin(number)
    elif function == 'cos' or function == 'cosine':
        return cos(number)
    elif function == 'tan' or function == 'tg':
        return tan(number)
    elif function == 'arcsin' or function == 'asin':
        return asin(number)
    elif function == 'arccos' or function == 'acos':
        return acos(number)
    elif function == 'arctan' or function == 'atan':
        return atan(number)
    elif function == 'sinh' or function == 'sineh':
        return sinh(number)
    elif function == 'cosh' or function == 'cosineh':
        return cosh(number)
    elif function == 'tanh' or function == 'tgh':
        return tanh(number)
    elif function == 'arcsinh' or function == 'asinh':
        return asinh(number)
    elif function == 'arccosh' or function == 'acosh':
        return acosh(number)
    elif function == 'arctanh' or function == 'atanh':
        return atanh(number)
    else:
        return None