''''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''

def sets(text):
    list = [text[i] for i in range(len(text))]
    res = ''
    count = 1
    for i in range(len(list)-1):
        if list[i] == list[i+1]:
            count += 1
        else:
            res = res + str(count) + list[i]
            count = 1
    if count > 1 or (list[len(list)-2] != list[-1]):
        res = res + str(count) + list[-1]
    return res


def decoding(text):
    number = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number = number + text[i]
        else:
            res = res + text[i]*int(number)
            number = ''
    return res


test = 'aaaaaaadwartgtr'
print(test)
print(sets(test))
print()
test2 = '5a6w11d3s'
print(test2)
print(decoding(test2))
