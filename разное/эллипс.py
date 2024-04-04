def ellipse(p1, p2, p3):

    def semi_axes(p1, p2, p3):
        x1, y1 = p1; x2, y2 = p2; x3, y3 = p3
        # точка p1 - центр эллипса
        a = ((x2-x1)**2 + (y2-y1)**2)**0.5
        b = ((x1-x3)**2 + (y1-y3)**2)**0.5
        return (a, b)
    def calculate_area_ellipse(a, b):
        area = pi * a * b
        return area
    def calculate_length_ellipse(a, b):
        length = 2* pi * ((a**2+b**2)/2)**0.5
        return length
    a, b = semi_axes(p1, p2, p3)
    area = calculate_area_ellipse(a, b)
    length = calculate_length_ellipse(a, b)
    result = {'a': a, 'b': b, 'length': round(length, 3), 'area': round(area, 3)}
    return result
    

pi = 3.1416
print(ellipse(p1=(3, 2.5), p2=(4.5, 2.5), p3=(3, 3.5)))

## {'a': 1.5, 'b': 1.0, 'length': 8.01, 'area': 4.712}

pi = 3.1416
print(ellipse(p1=(0, 0), p2=(0, 1), p3=(1, 0)))

## {'a': 1.0, 'b': 1.0, 'length': 6.283, 'area': 3.142}

pi = 3.14
print(ellipse(p1=(0, 0), p2=(0, 1), p3=(1, 0)))
## {'a': 1.0, 'b': 1.0, 'length': 6.28,'area': 3.14}