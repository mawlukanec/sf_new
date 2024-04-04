
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

description = 'Male , 39 years old , born on November 27 , 1979'
description_splited = description.split(' , ')
gender = description_splited [0].lower() 
age = description_splited [1].split(' ')[0]   #внимание!!!!!
year_of_birth = description_splited [3] 
print(gender, age, year_of_birth)     
#print(description_splited)
#print(gender)
