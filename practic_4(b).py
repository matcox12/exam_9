import json
from collections import Counter

#открываем файл data.json
with open('data.json', 'r') as file:
    data = json.load(file)


# Словарь для подсчета действий
count = Counter()

#перебираем по событиям и считаем действия по клиентам
for i in data:
    if i['category'] == 'page':
        client_id = i['client_id']
        count[client_id] += 1

#считаем количество клиентов с 5 действиями
res = 0

# Проходим по всем значениям словаря
for i in count.values():
    #если значение равно 5 увеличиваем счетчик на 1
    if i == 5:
        res += 1


print(res)
