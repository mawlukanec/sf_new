
def circle(p1, p2):
    def radius_okr(p1, p2):
        x1, y1 = p1; x2, y2 = p2
        radius = (((x2 - x1)**2 + (y2 - y1)**2)**0.5)
        return radius
    def calculate_circumference(radius):
        circumference = 2* pi* radius
        return circumference
    
    def calculate_area_circle(radius):
        area = pi * radius**2
        return area
    radius = radius_okr(p1, p2) 
    circumference = calculate_circumference(radius)
    area = calculate_area_circle(radius)
    result = {'radius': round(radius, 3), 'circumference': round(circumference, 3), 'area': round(area, 3)}
    return result 

pi = 3.1416
print(circle(p1=(3, 2.5), p2=(4, 4.5)))
## {'radius': 2.236, 'circumference': 14.05, 'area': 15.708}

pi = 3.1416
print(circle(p1=(0, 0), p2=(1, 1)))
## {'radius': 1.414, 'circumference': 8.886, 'area': 6.283}

pi = 3.14
print(circle(p1=(3, 2.5), p2=(4, 4.5)))
## {'radius': 2.236, 'circumference': 14.043, 'area': 15.7}
