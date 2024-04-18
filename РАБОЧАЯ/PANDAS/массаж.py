import pandas as pd
import urllib.request

x_data = pd.read_csv('d:/python/GUESS/РАБОЧАЯ/PANDAS/data/массаж.csv', sep=';', encoding='windows 1251')
x_df = x_data.copy()

# https://metrika.yandex.ru/stat/tags_utm?goal=313960040&metric=ym%3As%3Agoal%3Cgoal_id%3Eusers&sort=-ym%3As%3Agoal%3Cgoal_
# id%3Evisits&period=2024-04-01%3A2024-04-14&accuracy=1&id=53698513&group=day&isSamplingEnabled=true&stateHash=
# 658d4e23875209000ccec065
opener = urllib.request.FancyURLopener({})
url = "http://stackoverflow.com/"
f = opener.open(url)
content = f.read()
print(content)

# удаление последней строки с обобщенной информацией и NaN
dell = x_df.shape[0]
x_df = x_df[0:dell-1] 
#print(x_df.tail(5))

# приведение времени
x_df['Дата'] = pd.to_datetime(x_df['Дата'])# , dayfirst= True)


def split_gr(gr):
   
    temp = gr.split(' ')[-1] # нужно обрезать список!!!
    temp = temp.split('_')[-1]
    
    return int(temp)

x_df['группа']= x_df['Запись'].apply(split_gr) 
x_df['группа'] = x_df['группа'].astype('int8')
#print(x_df.info())
# print(x_df.tail(3))
# #display(logopedi_df.dtypes)
#print(x_df.tail(5))

# срез данных
# x_tail = x_df.iloc[:, 7:].groupby(by= 'Кампания', ascending= True).copy()
mask_kml = x_df['Кампания'] == 'Массаж лица'
mask_cws = x_df['Кампания'] == 'ШВЗ'

x_df.sort_values(by= 'Кампания', ascending=True).head()

# logoped['k'] = (logoped['Потрачено, руб.']/logoped['Выполненные заявки'])/logoped['Переходы по ссылкам']


# display(logoped.sort_values(by= 'k', ascending= True).head(20))

# # display(logoped.sort_values(by= 'Комментарии', ascending= False).head(20))