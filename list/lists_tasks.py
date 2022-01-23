# СПИСКИ
# Задача 1 k-ая буква слова
# На вход программе подается натуральное число n и n строк, а затем число k.
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
# На вход программе подается натуральное число nn, затем nn строк,
# затем число kk — количество поисковых запросов,
# затем kk строк — поисковые запросы.
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