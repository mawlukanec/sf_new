# Импортируем библиотеку для выполнения HTTP-запросов в интернет
import requests

# Читаем текстовый файл по url-ссылке
data = requests.get("https://raw.githubusercontent.com/SkillfactoryDS/Datasets/master/war_peace_processed.txt").text

# Предобрабатываем текстовый файл
data = data.split('\n')
data.remove('')
data = data + ['[new chapter]']

# Выводим первые 100 слов из книги
# print(data[:100])

# Превращаем список в множество, удаляя дублирующиеся слова
word_set = set(data)
# Удаляем из множества слово, символизирующее раздел между главами
word_set.discard('[new chapter]')
# Выводим результаты
print('Общее количество слов: {}'.format(len(data)))
print('Общее количество уникальных слов: {}'.format(len(word_set)))

# Инициализируем пустой словарь
word_counts = {}
# Инициализируем количество глав
count_chapter = 0
# Создаем цикл по всем словам из списка слов
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == '[new chapter]':
        # Если условие выполняется, то увеличиваем количество глав на 1
        count_chapter += 1
        # Переходим на новую итерацию цикла
        continue
    # Проверяем, что текущего слова еще нет в словаре слов
    if word not in word_counts:
        # Если условие выполняется, инициализируем новый ключ 1
        word_counts[word] = 1
    else:
        # В противном случае, увеличиваем количество слов на 1
        word_counts[word] += 1

# Выводим количество глав
print('Количество глав: {}'.format(count_chapter))

# Создаем цикл по ключам и их порядковым номерам полученного словаря
for i, key in enumerate(word_counts):
    # Выводим только первые 10 слов
    if i == 10:
        break
    print(key, word_counts[key])

# Инициализируем общий список, в котором будем хранить списки слов в каждой главе
chapter_data = []
# Инициализируем список слов, в котором будет хранить слова одной главы
chapter_words = []

# Создаем цикл по всем словам из списка
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == '[new chapter]':
        # Если условие выполняется, добавляем список со словами из главы в общий список
        chapter_data.append(chapter_words)
        # Обновляем (перезаписываем) список со словами из текущей главы
        chapter_words = []
    else:
        # В противном случае, добавляем текущее слово в список со словами из главы
        chapter_words.append(word)

# Проверяем, что у нас получилось столько же списков, сколько глав в произведении
print('Вложенный список содержит {} внутренних списка'.format(len(chapter_data)))
# Выведем первые 100 слов 0-ой главы
# print(chapter_data[0][:100])


# Инициализируем список, в котором будем хранить словари
chapter_words_count = []

# Создаем цикл по элементам внешнего списка со словами
for chapter_words in chapter_data:
    # Инициализируем пустой словарь, куда будем добавлять результаты
    temp = {}
    # Создаем цикл по элементам внутреннего списка
    for word in chapter_words:
        # Проверяем, что текущего слова еще нет в словаре
        if word not in temp:
            # Если условие выполняется, добавляем ключ в словарь
            temp[word] = 1
        else:
            # В противном случае, увеличиваем количество влождений слова в главу
            temp[word] += 1
    # Добавляем получившийся словарь в список
    chapter_words_count.append(temp)

# Выводим результат
#print(chapter_words_count)

# Создаем цикл по ключам словаря - спискам слов и их порядковым номерам
for chapter_number, chapter_dict in enumerate(chapter_words_count):
    # Выводим только первые 5 глав
    if chapter_number == 5:
        break
    # Выводим номер главы
    #print('-' * 40)
    #print('Chapter: {}'.format(chapter_number))
    #print('-' * 40)
    # Создаем цикл по ключам - словам и их порядковым номерам
    for j, word in enumerate(chapter_dict):
        # Выводим первые 10 слов из главы
        if j == 10:
            break
        #print(word, chapter_dict[word])
# word_set - множество из всех слов, которые есть в книге

# count_chapter - количество глав в книге (171)

# word_counts - словарь, ключами которого являются слова, а значениями - количество вхождений этих слов в книгу

# chapter_data - список из 171 списка, где элементы вложенных списков - все слова из главы. Каждый список соответствует своей главе

# chapter_words_count - список из 171 словаря, где ключи - слова, а значения - количество слов в главе. Каждый словарь соответствует своей главе



# задание 1
        


# # сообщаем переменной искомое слово
target_word = 'гостья'
# # выбираем интересующую главу
target_chapter = 15

chapter_words_copy = chapter_words_count.copy() # делаем копию списка со словарями
# цикл по множеству слов в книге
for x in range(count_chapter):
    
    # определяем общее количество слов в главе X
    j = len(chapter_data[x]) 
    #цикл по ключам словарей в chapter_words_count
    for keys in chapter_words_count[x]:  
        # заменяем частоту слов в словарях на частоту употребления слова в каждой главе
        chapter_words_copy[x][keys] = ((chapter_words_count[x][keys]/j)) 
# выводим на экран № главы и количество слов в ней    
print('количество слов в главе {}: {}'.format(target_chapter, len(chapter_data[target_chapter])))
# пустая строка
print()
# выводим на экран <искомое слово>, номер главы и коэффициент частоты слова в главе (tf)
print('коэффициент частоты (tf) слова <{}> в главе {}: {}'.format(target_word, target_chapter, round((chapter_words_copy[target_chapter][target_word]), 6)))
print()




# задание 2

target_word = 'человек'
# Ваш код здесь

counts_chapter_word = {} # пустой словарь для вывода количества глав с target word

word_document_frequency = {}  # пустой словарь для ключей(слов) и их значения (document frequency)
# цикл по множеству слов в книге
for word in word_set:  
    # приводим к 0 переменную <ppp>      
    ppp = 0
    # цикл по главам
    for x in range(count_chapter):   
        # условие нахождения слова в главе
        if word not in chapter_data[x]:    
            dict_x = 0
        else:
            dict_x = 1
        # подсчет глав в которых имеется искомое слово   
        ppp += dict_x 
    # заносим в словарь слова и количество глав с ним
    counts_chapter_word[word] = ppp   
    # заносим в словарь ключи(слова) и их значения (document frequency)  
    word_document_frequency[word] = ((ppp / count_chapter))  
# выводим на экран искомое слово и количество глав с ним
print(f'слово <{target_word}> встречается в {counts_chapter_word[target_word]} главах')
# пустая строка
# выводим на экран искомое слово и коэффициент document frequency
print(f'коэффициент df для слова <{target_word}> составляет {round(word_document_frequency[target_word], 4)}')
print()
 
 
 
  # задание 3      

# сообщаем переменной искомое слово
target_word = 'анна'
# выбираем интересующую главу
target_chapter = 4
from math import log
# trew - копия списка chapter_words_count
trew = chapter_words_count.copy()
# цикл по главам
for x in range(count_chapter):  
    #цикл по ключам словарей в chapter_words_count
    for keys in chapter_words_count[x]:   # цикл по ключам словарей
        # вычисление коэффициента tf_idf для каждого слова в главе и внесение значений в список trew
        trew[x][keys] = round((chapter_words_copy[x][keys]*log(1/word_document_frequency[keys])), 6)
# выводим на экран заданное слово и коэффициент tf_idf
print(f'коэффициент tf_idf для слова <{target_word}>: {trew[target_chapter][target_word]}')
print()


# задание 4


# выбираем интересующую главу
target_chapter = 3
worwordss = {}
word_max_tf_idf = []
# сортируем словарь из списка trew по значению ключей в порядке убывания (reverse=True)  
word_max_sorted = sorted(trew[target_chapter].items(), key=lambda x: x[1], reverse=True)
# выводим на экран три самых контрастных слова и соответствующие им значение коэффициента tf_idf
print(word_max_sorted[:3])
print()
# выводим на экран три самых контрастных слова
for i in range(3):
    word_max_tf_idf.append(word_max_sorted[i][0])
print(f'три самых контрастных слова в главе {target_chapter}: {word_max_tf_idf}')


# пустая строка
    


# print()
# # преобразуем список кортежей в словарь
# words_keys_max = dict(word_max[:3])
# # сообщаем переменной word_keys три ключа словаря words_keys_max
# words_keys = list(words_keys_max.keys())
# # слова в порядке убывания коэффициента tf_idf в заданной главе
# print(words_keys)
# # пустая строка
# print()
# # сортируем ключи
# words_keys.sort()
# # выводим на экран три самых контрастных слова в заданной главе в алфавитном порядке 
# print(f'три самых контрастных слова в главе {target_chapter}: {words_keys}')



