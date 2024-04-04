
#import datetime
#birthday = input('enter your birthdea')
#print(f'вы ввели: {birthday}')
#day, month, year = birthday.split('.')
#age_days = datetime.date.today - datetime.date(int(day),int(month),int(year))
#print('число дней с рождения: {age_days}')

#a = 5
#print(id(a), a)
#b = 5
#rint(id(b), b)
#a = a + b - 5
#print(id(a), a)
#print(id(5), 5)


# numbers = '1 2 3 4 5 6 7'
# numbers_split = numbers.split()
# print(numbers_split)
# print('\n'.join(numbers_split))


# colors = 'red green blue'
# colors_split = colors.split() # список цветов по отдельности
# colors_joined = ' \t '.join(colors_split) # объединение строк
# print(colors_joined)


#f=22
# print(chr(f))


# name = 'John'
# dayofweek = 'Friday'
# print('Hello, {}! Today is {}. Have a nice day!'.format(name, dayofweek))


# d = 12942021.24910
# d_str = str(d)
# print('\n'.join(d_str.split('.')))

#kk = 25225.25
#tax = 13.5
#salary = float(kk)
#print(salary * (1-tax/100))


#description = 'tTTtt jjj lll0'
#result_description = description.lower()
#result_description = result_description.split()
#print(result_description)

#salary = '25840 RUB.'
#salary_split = salary.split()
#salary_number = float(salary_split[0]) / 1000
#print(salary_number)


# experience = 'Work experience 2 months'
# experience_split = experience.split()
# experience_year = int(experience_split[2]) // 12
# experience_month = int(experience_split[2]) % 12
# print(experience_year, experience_month)


# Введите свое решение ниже


# description = 'Male , 39 years old , born on November 27 , 1979'
# description_splited = description.split(' , ')
# gender = description_splited [0].lower()
# age = description_splited [1].split(' ')[0]   #внимание!!!!!
# year_of_birth = description_splited [3]
# print(gender, age, year_of_birth)
#print(description_splited)
#print(gender)

# a = 'hello kitty mops'
# a_split = a.split()
# # c = b[0: 1:]
# print(a_split[-3:-1])


# a = "order1"
# b = "order2"
# c = "order3"
# orders = []
# orders.append(a)
# orders.append(b)
# orders.append(c)
# print(orders)


# book1 = 'my book'
# book2 = 'your book'
# books= ['all_books']
# books.append(book1)
# books.append(book2)
# print(books)

# a = 'A'
# b = 'B'
# c = 'C'
# letters = []
# letters.append(a)
# letters.append(b)
# letters.append(c)
# print(letters)
# letters.clear()
# print(letters)


# numbers = []
# numbers = ["2", "3", "5", "1", "5", "1", "1", "2", "2"]
# print(numbers.count("5"))


# all_things = ['order1', 'order2', 'order3']
# only_books = ['book1', 'book2']
# all_things.extend(only_books)
# print(all_things)


# nums = list(range(1, 11))
# nums.reverse()
# print(nums)


# test_dict = dict()
# test_dict.update({5: [3,4,5]})
# test_dict.update({(3,4,5): 'strong man'})
# print(test_dict)

# test_dict2 = {}
# test_dict2['name'] = 'Sancho'
# test_dict2['surname'] = 'Pancho'
# test_dict2['info'] = {'age': 35, 'country': 'Mexico'}
# print(test_dict2)


# s1 = {'a', 'b', 'c', 'd', 'e'}
# s1.remove('a')
# print(s1)  # метод выдаёт ошибку при удалении несуществующего элемента


# s1 = {'a', 'b', 'c', 'd', 'e', 'f'}
# s1.discard('d')
# print(s1)
# # метод не выдает ошибки при удалении несуществующего элемента


# alpha_set = {'a', 'b', 'c', 'd', 'e'}
# name = set('bad boy')
# b = alpha_set.union(name)
# print(b)


# num_set = set(range(0,11,1))
# # print(num_set)
# date_num = set([1,9,4,8])
# num_set.union(date_num)
# print(num_set)



# target_string = "TEG  r g e t"   # задаем значение строки
# target_string_lover = target_string.lower()   # задаем нижний регистр
# target_string_list = target_string_lover.replace(' ', '') # удаляем все пробелы
# result = target_string_list == target_string_list[::-1]  # сравниваем на предмет полинома
# print(result)

# или

# # Приводим строку к нижнему регистру и заменяем пробелы на пустые строки
# target_string = target_string.lower().replace(' ', '')
# # Сравниваем преобразованную строку с ней же в развернутом варианте
# result = target_string == target_string[::-1]




# diagnosis_1, diagnosis_2, diagnosis_3 = 'yes', 'yes', '3yes'
# result = diagnosis_1 == 'yes' or (diagnosis_2 == 'yes' or diagnosis_3 =='yes')
# print(diagnosis_1, diagnosis_2, diagnosis_3)
# print(result)


# N = 6904768
# x = str(N)[0]
# first_is_even = int(str(N)[0]) % 2 == 0
# print(first_is_even)



# n, m, k = 5, 4 , 10
# # длина, ширина прямоугольника. k - часть прямоугольника
# result = ((k % n == 0) or (k % m ==0)) and ((n*m) > k)
# # условие возможности взятия части прямоугольника
# print(result)



# phone = None
# phone_is_defined = phone is not None
# print(phone_is_defined)


# arrival_of_goods = {
#     '148902': {
#         'Футболка с принтом': 180,
#         'Свитшот черный': 245,
#         'Джинсы серые': 252
#     },
#     '893516': {
#         'Футболка с принтом': 43,
#         'Свитшот черный': 64,
#         'Джинсы черные': 102
#     },
#     '893481': {
#         'Кружка керамическая': 35,
#         'Свитшот черный': 10,
#         'Джинсы сервые': 14
#     }
# }
# invoice_number = '8913516'
# d = arrival_of_goods.get(invoice_number)
# invoice_exists = (arrival_of_goods.get(invoice_number)) is not None
# print(invoice_exists)



# credit_history = 'good'
# deposit = False
# guarantors = True
# credit = 11000.0

# if credit_history == 'bad':
#     if deposit:
#          if guarantors:
#             print('Issue a loan')
#          else:
#             print('Not to issue a loan')
#     else:
#         print('Not to issue a loan')
# else:
#     if credit > 1000:
#          print('Issue a loan')
#     else:
#         print('Not to issue a loan')


# number = 15
# if number % 2 == 0 or number % 5 == 0:
#     if number % 2 ==0:
#         if number % 5 == 0:
#             print('{0} делится на 2 и на 5'.format(number))
#         else:
#             print('{0} делится на 2, но не делится на 5'.format(number))
#     if number % 5 == 0:
#         if number % 2 != 0:
#             print('{0} не делится на 2, но делится на 5'.format(number))
# else:
#     print('{0} не делится ни на 2, ни на 5'.format(number))

# ИЛИ ЭТАЛОННЫЙ ОТВЕТ:
# number = 10
# if number % 2 == 0:
#     if number % 5 == 0:
#         print('{0} делится на 2 и на 5'.format(number))
#     else:
#         print('{0} делится на 2, но не делится на 5'.format(number))
# else:
#     if number % 5 == 0:
#         print('{0} не делится на 2, но делится на 5'.format(number))
#     else:
#         print('{0} не делится ни на 2, ни на 5'.format(number))



# x, y = (5, 5)
# if x > 0:
#     if y > 0:
#         print('1')
#     else:
#         print('4')
# else:
#     if y < 0:
#         print('3')
#     else:
#         print('2')


# time = 13
# print('Пора вставать!' if 7 <= time <= 12 else 'Ты проспал!')



# target_word = 'ero'
# if 'q' in target_word or 'z' in target_word:
#     print('Ух ты! Вы ввели редкое слово!')
# else:
#     print('Это не очень редкое слово...')



#player_1 = 'ножницы'
# #player_2 = 'бумага'
# if player_1 == player_2:
#     print('Ничья!')
# elif player_1 == 'камень' and player_2 == 'ножницы':
#     print('Первый игрок — победитель!')
# elif player_1 == 'бумага' and player_2 == 'камень':
#     print('Первый игрок — победитель!')
# elif player_1 == 'ножницы' and player_2 == 'бумага':
#     print('Первый игрок — победитель!')
# else:
#     print('Второй игрок — победитель!')


# purchases = []         # <class 'list'>
# prices = {'Adidas': 4298, 'Nike': 6550, 'Puma': 4490, 'Asics': 3879}      #<class 'dict'>
# prices_values = None
# prices_all = None
# purchases_list = list(purchases)
# orders = len(purchases_list)    #  определяем количество заказанных кросовок ()
# if orders > 0:           #  определяем что количество заказов > 0
#     if purchases[0] == purchases[1]:   # если заказы одинаковые
#         prices_all = prices[purchases[0]]+ prices[purchases[1]]   # сумма заказа
#         prices_values = round(prices_all*0.90, 2)  # округляем до 0.1
#         print('Стоимость заказа составила: {}. С учетом скидки в 10% — {}'.format(prices_all, prices_values))
#     elif purchases[0] != purchases[1]:
#         prices_all = prices[purchases[0]]+ prices[purchases[1]]
#         prices_values = round(prices_all*0.95, 2)
#         print('Стоимость заказа составила: {}. С учетом скидки в 5% — {}'.format(prices_all, prices_values))
# else:  # если заказа нет
#     print('Ваша корзина пуста')



# #date = '05.01.2018 20:15'       # вводим дату
# #date_split = int(date.split()[0][3:5])    # извлекаем из неё первый срез и месяц в виде числа <int>
# #day, month, year = int(date_split.split('.'))
# #print(day, month, year)
# # print(date_split)
# #if 1 <= date_split <= 5:
#     if date_split == 5:
#          print('category = 1')
#     elif 1 <= date_split < 5:
#          print('category = 2')
# #else:
#     print('category = 3')


# date = '05.02.2018 20:15'       # вводим дату
# category = None
# date_split = str(date.split()[0])
# print(date_split.split('.'))   # извлекаем из неё первый срез
# day, month, year = date_split.split('.')  # сообщаем соответствующим переменным значения
# # # print(day, month, year)     #  <class 'str'>
# if int(year) == 2019:    # сравниваем год
#     if int(month) == 5:
#         category = 1
#     else:
#         category = 2
# else:
#     category = 3
# print(category)


# city_info = "Москва , не готов к переезду , готов к командировкам"
# million_cities = ['Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань', 'Челябинск', 'Омск', 'Самара', 'Ростов-на-Дону', 'Уфа', 'Красноярск', 'Пермь', 'Воронеж', 'Волгоград']
# city_info_split = city_info.split(' , ')
# # print(city_info_split[0])
# if city_info_split[0] == 'Москва':
#     city = "Москва"
# elif city_info_split[0] == 'Санкт-Петербург':
#     city = "Санкт-Петербург"
# elif city_info_split[0] in million_cities:
#     city = "Город миллионник"
# else:
#     city = "Другое"

# # Добавляем конструкцию try-except для отлова нашей ошибки
# try:
#     print("Before exception") # Перед исключением
#     # Теперь пользователь сам вводит числа для деления
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b
#     # Печатаем c = a / b, если всё хорошо
#     print(c)
# # Добавляем тип именно той ошибки которую хотим отловить.
# except ZeroDivisionError as e:
#     print("After exception") # После исключения
# # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т. е. не произошло никакого исключения)
# else:
#     print("Everything's fine!")# Всё отлично!
# # код в блоке finally выполнится в любом случае при выходе из try-except
# finally:
#     print("Finally finished!") # Наконец-то завершено!

# print("After After exception") # После после исключения



# index = 7
# images_db = [101252, 521929, 215251]
# # a = images_db[index]
# # print(a)
# try:
#     img_id = images_db[index]
# except IndexError:           # ошибку не показывает
#     img_id = images_db[-1]    # выдаёт последнее значение в списке
# print(f'Image id: {img_id}')


# number = 0
# if number == 0:
#     raise ZeroDivisionError('Вы собираетесь делить на 0')   # создаём сами ошибку! и завершаем прогу
# else:
#     result = round(10/number, 3)
#     print(result)








# numbers = list(range(0,66,1))
# print(numbers)
# for asic in numbers:
#     print(asic)


# s = 0
# n = 2
# for s in range(1, n+1):
#     s +=s
# print(s)

# факториал
# # n = 150
# p = 1
# s = 0
# for s in list(range(1, n+1)):
#     p *= s
# # print(p)



# weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15]
# num = 1  # номер груза
# max_weight = 100
# for weight in weight_of_products:
#     if weight > max_weight:
#         print('{} truk {}'.format(num, weight))
#     else:
#         print('{} car {}'.format(num, weight))
#     num += 1



#weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15]


# # Задаём максимальное значение веса груза
# max_weight = 100
# # Задаём начальный номер груза
# num = 1
# # Создаём цикл по элементам списка со значениями массы товаров
# # weight — текущее значение веса
# for weight in weight_of_products:
#     # Если текущий вес меньше максимального,
#     if weight < max_weight:
#         # выводим номер груза, его вес и отправляем его в легковую машину.
#         print('Product {}, weight: {} -passenger car'.format(num, weight))
#     else:
#         # В противном случае
#         # выводим номер груза, его вес и отправляем его в грузовую машину.
#         print('Product {}, weight: {} -truck'.format(num, weight))
#     # Увеличиваем значение номера груза на 1
#     num += 1


# # Задаём список значений массы товаров
# weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15]
# # Задаём максимальное значение веса груза
# max_weight = 100
# # Вычисляем длину списка
# N = len(weight_of_products)
# # Создаём цикл по последовательности чисел от 0 до N (не включая N)
# # i — текущее значение последовательности
# for i in range(N):
#     # Обращаемся к элементу по индексу и сравниваем его с максимумом
#     if weight_of_products[i] < max_weight:
#         # Если текущий вес меньше максимального,
#         # выводим номер груза, его массу и отправляем его в легковую машину.
#         print('Product {}, weight: {} -passenger car'.format(i+1, weight_of_products[i]))
#     else:
#         # В противном случае
#         # выводим номер груза, его массу и отправляем его в грузовую машину
#         print('Product {}, weight: {} -truck'.format(i+1, weight_of_products[i]))



# # Список мест, которые хотим посетить.
# places = [
#     'Red Square',
#     'Swallow Nest',
#     'Niagara Falls',
#     'Grand Canyon',
#     'Louvre',
#     'Hermitage'
# ]
# # Словарь соответствия мест и стран
# location = {
#     'Red Square': 'Russia',
#     'Swallow Nest': 'Russia',
#     'Niagara Falls': 'USA',
#     'Grand Canyon': 'USA',
#     'Louvre': 'France',
#     'Hermitage': 'Russia'
# }
# # Вычисляем длину списка
# N = len(places)
# # Создаём цикл по списку мест, которые хотим посетить.
# # i — текущее значение последовательности
# for i in range(N):
#     # places[i] — i-й элемент в списке places
#     # Получаем страну из словаря location по ключу
#     country = location[places[i]]
#     # Сравниваем название стран
#     if country != 'Russia':
#         # Помечаем место как недоступное
#         places[i] = 'Unavailable'
# # Выводим результирующий список
# print(places)


# ## Будет выведено:
# ## ['Red Square', 'Swallow Nest', 'Unavailable', 'Unavailable', 'Unavailable', 'Hermitage']



# my_list = [1]
# for i in range(10):
#     my_list.append(my_list[i] * 2)
# print(my_list)

# num_list = [1, 10, 3, -5]
# num_list.sort()
# print(num_list)


# # num_list = [1, 10, 3, -5, 9, -7, 9.7]
# num_list.sort()
# i = len(num_list)
# for num in range(i):
#     nums = num_list[num]
#     print('element {}: {}'.format(num, nums))




# num_list = list(range(0, 100, 3))
# num_r = len(num_list)
# count_even = 0
# for num in range(num_r):
#     if num_list[num] % 2 == 0:
#         count_even += 1
# print(count_even)


# mixture_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']
# count_str = 0
# mixture_len = len(mixture_list)
# for i in range(mixture_len):
#     if type(mixture_list[i]) is str:
#         count_str += 1
# print(count_str)


# word_list = [   "     My", "name", "is", "Sergei", "EOS", "I'm", "from", "Moscow", "EOS"]
# text = str()
# word_len = len(word_list)
# for i in range(word_len):
#     if word_list[i] != 'EOS':
#         text = text + ' ' + word_list[i]
#     else:
#         text = text + '.'
# text = text.strip()        # .STRIP - удаляем лишние пробелы справа и с лева строки
# print(text)


# Создаём накопительную переменную, в которой будем считать сумму.
# S = 0
# # Задаём текущее натуральное число
# n = 1

# # Создаём цикл, который будет работать, пока сумма не превысит 500.
# while S < 500:  # делай, пока …
#     # Увеличиваем сумму, равносильно S = S + n
#     S += n
#     # Увеличиваем значение натурального числа
#     n += 1
#     # Выводим строку ожидания
#     print("Still counting...", S)
# # Отделяем промежуточный вывод от результата пустой строкой
# print()
# # Выводим результирующую сумму
# print("Sum is: ", S)
# # Выводим результирующее количество чисел
# print("Numbers total: ", n-1)



# n = 156
# x = 1
# while True:
#     if (x ** 2) % n != 0:
#         x += 1
#     else:
#         break
# print(x)


# year_count = 0
# target_money = 1000000000
# money = 50000
# debit = 500
# while money < target_money:
#     money += money * debit/100
#     year_count +=1
# print(year_count)


# seconds_num = 0
# health = 10
# damage = 100
# while True:
#     if health > 0:
#         seconds_num += 1
#         health = health - damage
#     else:
#         break
# print(seconds_num)

# #   ПОСЛЕДОВАТЕЛЬНОСТЬ ФИБОНАЧЧИ
# a, b, i = 1, 1, 2
# fibonacci_list = [1, 1]
# c = 0
# n = 3
# while i <= n-1:
#     c = a + b
#     a = b
#     i += 1
#     #fibonacci_list.append(b)
#     b = c
#     fibonacci_list.append(c)
# print(fibonacci_list)




# # Инициализируем последовательность
# f1 = f2 = 1
# fibonacci_list = [f1]
# i = 2
# # Создаём цикл, который будет выполняться по i < n.
# while i <= n:
#     # f1 приравнивается к f2, f2 приравнивается к f1 + f2.
#     f1, f2 = f2, f1 + f2
#     # Увеличиваем i на 1
#     i += 1
#     # Добавляем новый элемент последовательности в список
#     fibonacci_list.append(f1)



# temperature = [
#     [13, 15, 10],
#     [14, 13, 9],
#     [8, 9, 6]
# ]
# N = len(temperature)
# M = len(temperature[0])
# # print(temperature[4][1])
# # for row in temperature: # row — текущее значение из списка matrix
# #     # Выводим содержимое на экран
# #     print('Current row', row)
# for i in range(N):
#     print('current row',i)
#     for j in range(M):
#         print('current num', temperature[i][j])
#     print()


# hours = list(range(9, 24, 2))
# minuts = list(range(0, 60, 15))
# for hour in hours:
#     print(hour)
#     for minute in minuts:
#         if minute == 0:
#             print('alarms is set: {}:{}0'.format(hour, minute))
#         else:
#             print('alarms is set: {}:{}'.format(hour, minute))
#     print()


# str_list = ['text', 'morning', 'notepad', 'television', 'ornament']
# # Задаём начальное количество символов 'e'
# count = 0
# # Создаём цикл по элементам списка str_list
# for text in str_list:
#     for symbol in text:
#     # Проверяем условие, что текущий символ == 'e'
#         if symbol == 'e':
#             # Если условие истинно, увеличиваем количество символов 'e'.
#             count += 1
# # Выводим результат
# print("Count symbol 'e':", count)


# str_list = ['text', 'morning', 'notepad', 'television', 'ornament']
#  # Задаём начальное количество символов 'e'
# count = 0
#  # Создаём цикл по элементам списка str_list
# for text in str_list:
#     # Увеличиваем количество символов 'e'
#     # Метод str.count() считает, сколько раз символ встречается в строке text.
#     count += text.count('e')
# print("Count symbol 'e':", count)




# text_list = [
#     'afbaad',
#     'faaf',
#     'afaga',
#     'agag'
# ]
# count = 0
# for text in text_list:
#     count += text.count('a')
# print("Count symbol 'a':", count)




# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5, 7, 2]
# ]
# # Задаём пустой список с минимальными значениями строк
# min_value_rows = []
# # Создаём цикл по строкам матрицы random_matrix
# for row in random_matrix: # row — текущая строка таблицы
#     # Задаём начальное значение кандидата на минимум
#     min_value = row[0]
#     print()
#     # Создаём цикл по элементам списка row
#     # elem — текущий элемент из списка row
#     for elem in row:
#         # Проверяем условие, что текущий элемент меньше кандидата на минимум.
#         if elem < min_value:
#             # Если условие выполняется, заменяем кандидата на минимум.
#             min_value = elem
#     # Добавляем полученный минимум строки в список
#     min_value_rows.append(min_value)
# # Выводим минимальные элементы
# print("Minimal elements:", min_value_rows)


# random_matrix = [
#     [9, 121, 1, 10, 42],
#     [91, 5, 3, 34, -1],
#     [-8, 98, 5, 24, -420]
# ]
# max_value_rows = []
# for row in random_matrix:
#     max_value = row[0]
#     for elem in row:
#         if elem > max_value:
#             max_value = elem
#     #print(max_value)
#     max_value_rows.append(max_value)
# ## max_value_rows = [9, 5, 8]
# print(max_value_rows)



# Заданная таблица со студентами
# student_scores = [
#     [56, 90, 80],
#     [80, 86, 92],
#     [91, 76, 89],
#     [91, 42, 60],
#     [65, 30, 90]
# ]
# N = len(student_scores) # Задаём число студентов
# M = len(student_scores[0]) # Задаём число экзаменов
# summa = 0 # Задаём начальное значение общего балла
# math_sum = 0 # Задаём начальное значение общего балла по математике
# info_sum = 0 # Задаём начальное значение общего балла по информатике
# rus_sum = 0 # Задаём начальное значение общего балла по русскому языку
# # Создаём цикл по последовательности от 0 до N (не включая N)
# for i in range(N):
#     math_sum += student_scores[i][0]
#     info_sum += student_scores[i][1]
#     rus_sum += student_scores[i][2]
#     for j in range(M):
#         summa += student_scores[i][j]
# #print('общий балл по математике: {}, общий балл по информатике: {}, общий балл по русскому языку: {}'.format(math_sum/N, info_sum/N, rus_sum/N))
# print('общий балл по математике:', math_sum/N)
# print('общий балл по информатике:', info_sum/N)
# print('общий балл по русскому языку:', rus_sum/N )
# print(summa/(M*N))


# test_matrix = [
#     [1, 2, 3],
#     [7, -1, 2],
#     [123, 2, -1]
# ]
# N = len(test_matrix)
# for i in range(N):
#     M = len(test_matrix[i])
# is_square = N == M
# print(is_square)


# temp = [[25, 27, 28, 26, 27, -26, -25, -2, 26],
#          [21, 22, 28, 27, 28, 26, 25, 19, 26],
#            [-19, 21, 25, -27, 28, 25, 21, 20, 26]
# ]
# N = len(temp)
# s = list()
# for i in range(N):
#     M = len(temp[i])
#     for j in range(M):
#         if temp[i][j] < 0:
#             temp[i][j] = temp[i][j]*(-1)
# print(temp)


# customer_satisfaction = [
#     [0.87, 0.56, 0.77],
#     [0.22, 0.46, 0.56, 0.89, 0.95],
#     [0.45, 0.44, 0.68],
#     [0.73, 0.88, 0.95, 0.49]
# ]
# month_max, max_satisfaction = 0, 0
# month_satisfaction = []
# for row in customer_satisfaction:
#     # print(row)
#     month = 0
#     i = 0
#     for elem in row:
#         i += 1
#         month += elem
#         month_max = month/i
#     if month_max > max_satisfaction:
#         max_satisfaction = round(month_max, 2)
#     month_satisfaction.append(round(month/i,2))
# print(month_satisfaction, max_satisfaction)


   #        enumerate()

# user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# number = 1
# for dynamic in user_dynamics:
#     print('day {}:{}'.format(number, dynamic))
#     number += 1


# user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# N = len(user_dynamics)
# for i in range(N):
#     print('day {} :{}'.format(i+1, user_dynamics[i]))


# user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# for i, dynamic in enumerate(user_dynamics):
#     print('Day {}:{}'.format(i, dynamic))




# user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# number_negative = None #объявляем переменную, в которой будем хранить номер последнего дня оттока, изначально она пустая (None)
# N = len(user_dynamics) #вычисляем длину списка
# #создаём цикл по элементам последовательности от 0 до N (не включая N)
# for i in range(N): # i — индекс текущего элемента
#     #проверяем условие оттока — текущий элемент отрицательный
#     if user_dynamics[i] < 0: #если условие истинно,
#         number_negative = i+1  #перезаписываем значение номера дня
#         print("Churn value: ", user_dynamics[i]) # выводим количество ушедших в этот день пользователей
#         print("Number day: ", number_negative) # выводим номер дня

# user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# #создаём цикл по элементам последовательности и их значениям
# for i, value in enumerate(user_dynamics): # i — индекс текущего элемента, user - значение
#     #проверяем условие оттока — текущий элемент отрицательный
#     if value < 0: #если условие истинно,
#         print("Churn value: ", value) # выводим количество ушедших в этот день пользователей
#         print("Number day: ", i+1) # выводим номер дня




# str_list = ['Hello', 'my', 'name', 'is', 'Ezeikel', 'I', 'like', 'knitting']
# cut_str_list, y = [], []
# # cut_str_list = [[0, 'Hel'], [1, 'my'], [2, 'nam'], [3, 'is'], [4, 'Eze'], [5, 'I'], [6, 'lik'], [7, 'kni']]
# for i, text in enumerate(str_list):
#    y = [i, text[:3]]
#    cut_str_list.append(y)
# print(cut_str_list)


# to_inventory = ['Blood Moon Sword', 'Sunset-colored sword', 'Bow of Stars', 'Gain Stone']
# item = list()
# for i in to_inventory:
#     if len(item) == 3:
#         print('its full')
#         break
#     item.append(i)
# print(item)

#                    гипотеза  Сиракуз
# n = 8
# origin = n

# # Создаём бесконечный цикл
# while True:
#     if n % 2 == 0:
#         n = n // 2
#         # Проверяем, что результат равен 1
#         if n == 1:
#         # Если условие выполняется, выводим утвердительное сообщение.
#             print(f'Syracuse hypothesis holds for number {origin}')
#             break
#         else:
#             n = n //2

#     else:
#         n = (n * 3 + 1) // 2




# mixture_dict = {'key1': 24, 'key2': '1.4', 'key3': 14, 'key4': 16.24, 'key6': 124.2414, 'key7': 12.2}
# сount_numbers = 0

# for item in mixture_dict:
#     if type(mixture_dict[item])  is str:
#         continue
#     else:
#         count_numbers  += 1
# print(count_numbers)


# text = """
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I am sure.
# So if she sells sea shells on the sea shore,
# I am sure that the shells are sea shore shells.
# """
# count_punctuation = {'.':0, ',':0, ';':0, '?':0, '!':0, '—':0}
# dict1 = {}  
# for symbol in text:
#     if symbol not in dict1:
#         dict1[symbol] = 1
#     else:
#         dict1[symbol] += 1
# for keys in count_punctuation.keys():
#     if keys in dict1.keys():
#         count_punctuation[keys] = dict1[keys]
#         continue
# #print(count_punctuation)
# # print(dict(sorted(count_punctuation.items(), key=lambda item: item[1], reverse=True)))






# text = sentence = 'A roboT MAY Not injure a humAn BEING or, tHROugh INACtion, allow a human BEING to come to harm.'
# text = text.lower()
# text.replace(',', '')
# text.replace('.', '')
# text_split = text.split()
# dict_words = {}
# for word in text_split:
#     if word not in dict_words:
#         dict_words[word] = 1
#     else:
#         dict_words[word] += 1
 
# print(dict_words)

#  = {'a': 3, 'robot': 1, 'may': 1, 'not': 1, 'injure': 1, 'human': 2, 'being': 2, 'or': 1, 'through': 1, 'inaction': 1, 'allow': 1, 'to': 2, 'come': 1, 'harm': 1}





# str_list = ["text", "morning", "notepad", "television", "ornament"]
# symbol_to_check = 't'
# word_dict = {}
# for word in str_list:
#     t = 0
#     for symbol in word:
#         if symbol == symbol_to_check:
#             t += 1
#         else:
#             word_dict[word] = 0
#         word_dict[word] = t
            
        

# print(word_dict)


# Импортируем библиотеку для выполнения HTTP-запросов в интернет
# import requests
# # Читаем текстовый файл по url-ссылке
# data = requests.get("https://raw.githubusercontent.com/SkillfactoryDS/Datasets/master/war_peace_processed.txt").text

# # Предобрабатываем текстовый файл
# data = data.split('\n')
# data.remove('')
# data = data + ['[new chapter]']

# # Выводим первые 100 слов из книги
# print(data[:100])

# from math import log
# print(log(18))


print(trew[11])