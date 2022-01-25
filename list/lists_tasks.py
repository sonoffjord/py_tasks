# СПИСКИ
# Задача 1 k-ая буква слова
# На вход программе подается натуральное число n и n-строк, а затем число k.
# Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

ls = list()
for _ in range(int(input())):
    ls.append(input())

k = int(input())
string = ''
for j in range(len(ls)):
    string += ls[j][k-1:k]
print(string)

# Задача 2 search
# На вход программе подается натуральное число n, затем n строк,
# затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки,
# в которых встречаются все поисковые запросы.

ls = [input() for _ in range(int(input()))]
search = [input() for _ in range(int(input()))]
for i in ls:
    for j in search:
        if j.lower() not in i.lower():
            break
    else:
        print(i)

# Задача 3 Произведение чисел
# Напишите программу для определения,
# является ли число произведением двух чисел из данного набора,
# выводящую результат в виде ответа «ДА» или «НЕТ».

array = []
for i in range(int(input())):
    array.append(input())
n = int(input())
flag = 0
for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
        if int(array[i]) * int(array[j]) == n:
            flag = 1
if flag == 1:
    print('ДА')
else:
    print('НЕТ')

# Задача 4 Упаковка дубликатов
# На вход программе подается строка текста, содержащая символы.
# Напишите программу, которая упаковывает последовательности одинаковых
# символов заданной строки в подсписки.
# Пример: Ввод = w w w o r l d g g g g
# Вывод = [['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g']]

char_list = list()
main_list = list()

for char in input().split():
    if not char_list:
        char_list.append(char)
    else:
        if char_list[-1] == char:
            char_list.append(char)
        else:
            main_list.append(char_list)
            char_list = list()
            char_list.append(char)
if char_list:
    main_list.append(char_list)
print(main_list)

# Задача 5 Разбиение на чанки
# На вход программе подаются две строки,
# на одной символы, на другой число n.
# Из первой строки формируется список.
# Реализуйте функцию chunked(),
# которая принимает на вход список и число,
# задающее размер чанка (куска),
# а возвращает список из чанков указанной длины.

# Ввод: строка = a b c d e f, число - 2
# Вывод: [['a', 'b'], ['c', 'd'], ['e', 'f']]


def chunked(string, num):
    temp = ''
    list_main = list()
    string = string.replace(' ', '')
    for i in range(0, len(string), num):
        temp = list(string[i:i+num])
        list_main.append(temp)
        temp = ''
    return list_main


print(chunked(input(), int(input())))

# Задача 6 Подсписки списка
# Подсписок — часть другого списка.
# Подсписок может содержать один элемент, несколько, и даже ни одного.
# Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4].
# Список [2, 3] — подсписок списка [1, 2, 3, 4],
# но список [2, 4] не подсписок списка [1, 2, 3, 4],
# так как элементы 22 и 44 во втором списке не смежные.
# Пустой список — подсписок любого списка.
# Сам список — подсписок самого себя,
# то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].
# На вход программе подается строка текста, содержащая символы.
# Из данной строки формируется список.
# Напишите программу, которая выводит список,
# содержащий все возможные подсписки списка,
# включая пустой список.

# Ввод: a b v
# Вывод: [[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]

def list_sublists(array):
    inc_list = array.split()
    main_list = [[]]
    temp_list = list()
    for i in range(len(inc_list)):
        for j in range(len(inc_list)):
            temp_list = inc_list[j:i+j+1]
            if len(temp_list) == i+1:
                main_list.append(temp_list)
    return main_list
            
print(list_sublists(input()))
