# Функция для регистрации пользователей
def register(surname, name, date, middle_name=None, registry=None):
    # Вспомогательная функция для предобработки даты
    def preprocessing_date(date):        
        # Разделяем строку по символу точки
        day, month, year = date.split('.')
        # Преобразуем все данные к типу данных int
        day, month, year = int(day), int(month), int(year)
        
        def check_date(day, month, year):
            # Проверяем день, месяц и год на целочисленность
            if (type(day) is not int) or (type(month) is not int) or (type(year) is not int):
                return False
    # Проверяем год на заданный диапазон
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
    # Проверяем количество дней в феврале с проверкой високостности года           
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if month == 2 and day > 29:
                    return False
            else:
                if month == 2 and day > 28:
                    return False                
            return True
         # если дата не верная, выбрасываем ошибку
        if check_date(day, month, year) is False:
            raise ValueError("Invalid Date!")

        check_date(day, month, year)  # проверка дат,
        # print(day, month, year)

        # print(check_date(28,2,2003))       
        return day, month, year
    # Если список не был передан — создаём пустой список
    if registry is None:
        registry = list()
    # Разделяем дату на составляющие
    day, month, year = preprocessing_date(date)
    # Добавляем данные в список
    registry.append((surname, name, middle_name, day, month, year))
    return registry

reg = register('Petrova', 'Maria', '13.03.2003', 'Ivanovna')
reg = register('Ivanov', 'Sergej', '24.09.1995', registry=reg)
reg = register('Smith', 'John', '29.02.2004', registry=reg)
print(reg)