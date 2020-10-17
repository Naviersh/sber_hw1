import re
print("Задание 1")
array = [0,1,2,3,4,5]
print(array[0],array[2],array[-2])
print("Задание 2")
A: int = 3
if len(array) - 1 < A:
    print(-1)
else:
    print(array[A] ** A)
print("Задание 3")
sber_str = str("сбербанк")
b = str(sber_str).count('б')
print(b)
print("Задание 4")
number = int(101100110100)
zero = str(number).count('0')
print(zero)
print("Задание 5")
str = "строка"
print(str[::-1])
print("Задание 6")
array = [2,2,2,3]
for i in range(1,len(array)):
    if array[0] == array[i]:
        continue
    else:
        break
else:
    print('Все элементы массива одинаковые')
print("Задание 7")
s = input()
lower = upper = numbers = 0
for i in range(0,len(s)):
    if 'a' <= s[i] <= 'z':
        lower += 1
    if 'A' <= s[i] <= 'Z':
        upper += 1
    if '0' <= s[i] <= '9':
        numbers += 1
if (lower > 0) & (upper > 0) & (numbers > 0) & (len(s) >= 16):
    print('Пароль надежный')
else:
    print('Пароль ненадежный')
print("Задание 8")
array = [1, 2, 3, 4, 5, [6, 7], 8]
def list_open(array, new_array=[]):
    for i in array:
        if type(i) == list:
            list_open(i)
        else:
            new_array.append(i)
    return new_array
print(list_open(array))
print("Задание 9")
data = {'a': 1.01, 'b': 1.10, 'c': 0.1, 'd': 1 }
def dict(dictionary):
    return max(dictionary, key=dictionary.get)
print(dict(data))
print("Задание 10")
array = [1,2,3,1,3]
new_array = [i for i in array if array.count(i) > 1]
print(new_array)