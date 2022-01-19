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