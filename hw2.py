from collections import Counter
print("Задание 1")
def ex1(str):
    c = Counter(str)
    return c.most_common()[0][0]
print(ex1(sorted("aaaddddb;;   bbbc")))

print("Задание 2")
def ex2(text):
    count = 0
    result = "Нет последовательности из 3-х слов"
    for i in text.split():
        if i.isalpha():
            count += 1
        else:
            count = 0
        if count >= 3:
            result = "Есть последовательность из 3-х слов"
    return result
print(ex2("fss ddd dd 32"))
print("Задание 3")


def ex3(str):
    rescount = 1
    count = 1
    prev = str[0]
    for symbol in str[1:]:
        if symbol == prev:
            count += 1
        else:
            if count > rescount:
                rescount = count
            count = 1
        prev = symbol
    return rescount
print(ex3("аааабббббвв"))
print("Задание 4")


def ex4(up):
    str = ""
    for new_str in up:
        if new_str.isalpha() & new_str.isupper():
            str += new_str
    return str


up = "sadhashduiSDSADX:';  dsafsSDS"
print(ex4(up))
print("Задание 5")
def ex5(mas):
    c = Counter(mas)
    c.most_common()
    new_mas = []
    for key, value in dict(c).items():
        for v in range(value):
            new_mas.append(key)
    return new_mas
print(ex5([4, 4, 6, 4, 2, 2, 4, 6]))
print("Задание 6")
list = [1, 2, 4, 5]
number = 3
def ex6(list, number):
    result = 0
    for i in list:
        if i <= number:
            result = i
    return result
print(ex6(list, number))
print("Задание 7")
