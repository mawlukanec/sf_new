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
# инициализируем пустой словарь chapter_words_tf 
chapter_words_tf = {}   
# цикл по множеству слов в книге
for x in range(count_chapter):
    # определяем общее количество слов в главе X
    j = len(chapter_data[x]) 
    # инициализируем пустой словарь
    keys_temp = {}
    #цикл по ключам словарей в chapter_words_count
    for keys in chapter_words_count[x]:  
        # заменяем частоту слов в словарях на частоту употребления слова в каждой главе
        keys_temp[keys] = (chapter_words_count[x][keys]/j) 
    # всавляем в словарь chapter_words_tf словарь keys_temp с найденым коэффициентом tf в соответствии с номером главы
    chapter_words_tf[x] = keys_temp
# # выводим на экран № главы и количество слов в ней    
# print('количество слов в главе {}: {}'.format(target_chapter, len(chapter_data[target_chapter])))
# # пустая строка
# print()
# # выводим на экран <искомое слово>, номер главы и коэффициент частоты слова в главе (tf)
print('коэффициент частоты (tf) слова <{}> в главе {}: {}'.format(target_word, target_chapter, round((chapter_words_tf[target_chapter][target_word]), 6)))


# задание 2

target_word = 'гостья'
# Ваш код здесь

counts_chapter_word = {} # пустой словарь для вывода количества глав с target word
# создаеи пустой список
word_document_frequency = {}  # пустой словарь для ключей(слов) и их значения (document frequency)
# цикл по множеству слов в книге
for word in word_set:  
    # приводим к 0 переменную <ppp>      
    ppp = 0
    # цикл по главам
    for x in range(count_chapter):   
        # условие нахождения слова в главе
        if word in chapter_data[x]:    
            dict_x = 1
        else:
            continue 
        # подсчет глав в которых имеется искомое слово   
        ppp += dict_x 
    # заносим в словарь слово(word) и количество глав с ним
    counts_chapter_word[word] = ppp   
    # заносим в словарь ключи(слова) и их значения (document frequency)  
    word_document_frequency[word] = ((ppp / count_chapter))  
# выводим на экран искомое слово и количество глав с ним
print(f'слово <{target_word}> встречается в {counts_chapter_word[target_word]} главах')
# выводим на экран искомое слово и коэффициент document frequency
print(f'коэффициент df для слова <{target_word}> составляет {round(word_document_frequency[target_word], 4)}')
# пустая строка
print()
 
 
  # задание 3      

# сообщаем переменной искомое слово
target_word = 'гостья'
# выбираем интересующую главу
target_chapter = 15
from math import log
# trew - копия списка chapter_words_count
tf_idf_date = {}
###### trew = chapter_words_count.copy()
# цикл по главам
for x in range(count_chapter):  
    # пустой словарь
    tf_idf_dict = {}
    #цикл по ключам словарей в chapter_words_count
    for keys in chapter_words_count[x]:  
        # вычисление коэффициента tf_idf для каждого слова в главе и внесение значений в список trew
        tf_idf_dict[keys] = (chapter_words_tf[x][keys]*log(1/word_document_frequency[keys]))
        #trew[x][keys] = round((chapter_words_copy[x][keys]*log(1/word_document_frequency[keys])), 6)
# выводим на экран заданное слово и коэффициент tf_idf
    tf_idf_date[x] = tf_idf_dict
print(f'коэффициент tf_idf для слова <{target_word}>: {round((tf_idf_date[target_chapter][target_word]), 6)}')
# пустая строка
print()


# задание 46

# выбираем интересующую главу
target_chapter = 15
worwordss = {}
word_max_tf_idf = []
# сортируем словарь из списка trew по значению ключей в порядке убывания (reverse=True)  
word_max_sorted = sorted(tf_idf_date[target_chapter].items(), key=lambda x: x[1], reverse=True)
# выводим на экран три самых контрастных слова и соответствующие им значение коэффициента tf_idf
# print(word_max_sorted[:3])

# создаем цикл до 3
for i in range(3):
    # добавляем в список word_max_tf_idf слова с максимальным tf_idf в порядке убывания коэффициента
    word_max_tf_idf.append(word_max_sorted[i][0])
# выводим на экран три самых контрастных слова:
print(f'три самых контрастных слова в главе {target_chapter}: {word_max_tf_idf}')
