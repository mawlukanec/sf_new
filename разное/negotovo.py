s = input('Введите строку: ')

import string
alphabet = string.ascii_lowercase

def replace_duplicates(temp):
    # запускаем бесконечный цыкл
    while True:
        # сравниваем длинну введенной строки с множеством этой же строки для определения наличия повторяющихся элементов
        if len(temp) == len(set(temp)):
            # если повторяющихся элементов строки нет - завершаем бесконечный цикл
            break
        # если есть повторения элементов 
        else:
            # инициализируем пустой словарь
            dict_t = {}
            print(len(dict_t))
            # цикл по элементам строки множества
            for i in str(set(temp)):
                # инициализируем пустую строку
                index = []
                # инициализируем переменные nums_index и  duble для подсчета индека повторяющегося элемента и определения его поторения соответственно
                nums_index, duble = 0, 0
                # если буква есть в списке temp 
                for letter in temp:
                    # увеличиваем переменную nums_index для подсчета индека повторяющегося элемента на 1
                    nums_index += 1
                    # если элемент строки множества равен элементу в строке temp 
                    if i == letter:
                        # увеличиваем duble на 1
                        duble +=1
                        # добавляем индекс поторяющегося элемента
                        index.append(nums_index)
                        # если число совпадений  = 2
                        if duble == 2:
                            # добавляем в словарь по ключу letter список с индексами дублирующихся элементов
                            dict_t[letter] = index
                            # завершаем цикл
                            break
            # сообщаем переменной dict_keys ключи словаря
            dict_keys = list(dict_t)
            # сообщаем переменным letter_indexes и litera_dupl значение первого ключа и сам ключ соответственно
            letter_indexes, litera_dupl = dict_t[dict_keys[0]], dict_keys[0]
            # цикл по индексам alphabet

            for i in range(len(alphabet)):
                # если буква из alphabet соответствует дублирующимся буквам

                if alphabet[i] == litera_dupl:
                    # записываем в переменную chenge_litera следующую букву из alphabet
                    if alphabet[i] == 'z':
                        chenge_litera = alphabet[1]  
                    else:
                        chenge_litera = alphabet[i+1]  
                    # завершаем цикл              
                    break
            # добавляем вконец строки заменяющую дубль букву (chenge_litera) согласно alphabet    
            temp += chenge_litera
            # преобразуем строку в список для исрользования метода .pop()            
            temp = list(temp)
            # удаляем дублирующийся элемент в обратном порядке
            temp.pop(letter_indexes[1]-1); temp.pop(letter_indexes[0]-1)
    # возвращаем получившийся список в виде строки      
    return  ''.join(temp)

print(replace_duplicates(s))