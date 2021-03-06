# СТРОКИ

# Задача 1 Одинаковые соседи
# На вход программе подается одна строка.
# Напишите программу, которая определяет
# сколько в ней одинаковых соседних символов.

s = input()
count = 0
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        count += 1
print(count)

# Задача 2 Гласные и согласные
# На вход программе подается одна строка
# с буквами русского языка.
# Напишите программу, которая определяет
# количество гласных и согласных букв.

s = input().lower()
count_vowels = 0
count_consonants = 0
for i in s:
    if i in 'ауоыиэяюёе':
        count_vowels += 1
    if i in 'бвгджзйклмнпрстфхцчшщ':
        count_consonants += 1
print('Количество гласных букв равно', count_vowels)
print('Количество согласных букв равно', count_consonants)

# Задача 3 Decimal to Binary
# На вход программе подается натуральное число,
# записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное
# число в двоичную систему счисления.

n = int(input())
binary = ''
while n != 0:
    binary += str(n % 2)
    n //= 2
print(binary[::-1])

# Задача 4 Шифр Цезаря
# Формат входных данных:
# В первой строке дается число – сдвиг,
# во второй строке даётся закодированное сообщение
# в виде строки со строчными латинскими буквами.

# Формат выходных данных:
# Программа должна вывести одну строку – декодированное сообщение.
# Обратите внимание, что нужно декодировать сообщение,
# а не закодировать.

step = int(input())
message = input()
for i in range(len(message)):
    n = ord(message[i]) - step
    if n < 97:
        n = 122 - (96 - n)
    print(chr(n), end='')

# Задача 5 Переворот
# На вход программе подается строка текста в которой буква «h»
# встречается как минимум два раза.
# Напишите программу, которая возвращает исходную строку
# и переворачивает последовательность символов,
# заключенную между первым и последним вхождением буквы «h».

s = input()
print(s[:s.find('h')] + s[s.rfind('h'):s.find('h'):-1] + s[s.rfind('h'):])

# Задача 6 Standard American Convention
# На вход программе подаётся натуральное число.
# Напишите программу, которая вставляет в
# заданное число запятые в соответствии со стандартным
# американским соглашением о запятых в больших числах.


def number_separator(num):
    string = ''
    count = 0
    for i in num[::-1]:
        if count < 3:
            string += i
            count += 1
        elif count == 3:
            string += ',' + i
            count = 1
    return string[::-1]


print(number_separator(input()))
