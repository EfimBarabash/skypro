# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def read(csv):
    data = [line.split(';') for line in csv.split('\n')]
    return data

def sort_asc(data: list):
    sort_data = data.copy()
    sort_data.sort(key=lambda elem: int(elem[1]))
    return sort_data

def filter(data: list):
    return [elem for elem in data if int(elem[1]) > 10]


def get_users_list():
   data = read(csv)
   data = sort_asc(data)
   data = filter(data)
   return data

if __name__ == '__main__':
    print(get_users_list())
