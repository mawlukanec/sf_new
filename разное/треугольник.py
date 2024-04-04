def triangle(p1,p2,p3):
    x1 ,y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    # Вычисляум длины сторон треугольника по координатам точек
    a = ((x2 - x1) ** 2 + (y2 - y1)** 2) ** 0.5
    b = ((x3 - x1) ** 2 + (y3 - y1)** 2) ** 0.5
    c = ((x3 - x2) ** 2 + (y3 - y2)** 2) ** 0.5
    def calculate_perimeter_triangle(a, b, c):
        # Периметр — сумма всех сторон треугольника
        perimeter = a + b + c
        return perimeter
    def calculate_area_triangle(a, b, c):
        # Вычисляем полупериметр 
        # Значение perimeter берётся из объемлющей области видимости
        p = perimeter / 2
        # Вычисляем площадь по формуле Герона
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area
    # проверка на существование треугольника
    def check_exist_triangle(a, b, c):
        if (a+b>c) and (a+c>b) and (b+c >a):
            return True
        else:
            return False
    # выбрасываем ошибку если треугольник не существует
    if check_exist_triangle(a, b, c) is False:
        raise ValueError("Треугольник не существует")
    check_exist_triangle(a, b, c)
    perimeter = calculate_perimeter_triangle(a, b, c)
    area = calculate_area_triangle(a, b, c)
    result = {'a': a, 'b': b, 'c': c, 'perimeter': perimeter, 'area': area}
    return result
print(triangle(p1=(2, 2), p2=(4, 1.25), p3=(1, 4.5)))
## {'a': 2.1360009363293826, 'b': 2.692582403567252, 'c': 4.422951503238533, 'perimeter': 9.251534843135168, 'area': 2.1250000000000027}
print(triangle(p1=(1, 1), p2=(1, 4), p3=(5, 1)))
## {'a': 3.0, 'b': 4.0, 'c': 5.0, 'perimeter': 12.0, 'area': 6.0}
print(triangle(p1=(2.5, 2), p2=(4, 1), p3=(1, 3)))
## ValueError: Треугольник не существует
