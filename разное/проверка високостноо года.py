# Введите свое решение ниже
def check_date(day, month, year):
    def is_leap(day, month, year):
        if (type(day) is not int) or (type(month) is not int) or (type(year) is not int):
                return False
    # Проверяем год на заданный Sдиапазон
        if (year <= 1900) or (year >= 2025):
            return False
    # Проверяем месяц на заданный диапазон     
        if (month < 1) or (month > 12):
            return False
    # Проверяем день на заданный диапазон  
        if (day < 1) or (day > 31): 
            return False
    # Проверяем апрель, июнь, сентябрь и ноябрь на количество дней
        if (month in [4,6,9,11]) and (day > 30):
            return False
    # Проверяем количество дней в феврале            
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if month == 2 and day > 29:
                return False
        else:
            if month == 2 and day > 28:
                return False                
        return True
    is_leap(day, month, year)
    return is_leap(day, month, year)
print()
print(check_date(18, 9, 1999))
# True
print(check_date(29, 2, 2000))
# True
print(check_date(29, 2, 2021))
# False
print(check_date(13, 13, 2021))
# False
print(check_date(13.5, 12, 2021))
# False