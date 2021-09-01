"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
 получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

"""


def parsing(name_file):
    data = []
    spam_dict = {}
    for line in name_file:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spam_dict.setdefault(splitted[0], 0)
        spam_dict[splitted[0]] += 1
    return data, spam_dict

with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    print(parsing(file_1))



#c = zip(remote_addr, request_type, requested_resource)

#print(f'{remote_addr} {request_type} {requested_resource}/n')
#print(requested_resource[0:1])
