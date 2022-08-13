''''
1. Создайте программу для игры в "Крестики-нолики".
'''

import random


def simvol_player(number):
    if number in [1,2]:
        res = []
        if number == 1:
            player = 'X'
            bot = 'O'
        else:
            player = 'O'
            bot = 'X'
        res = [player, bot]
        return res
    else:
        print('Неверно введено значение')


def pole(list):
    print('-------------')
    for i in range(3):
        print ("|", list[0+i*3], "|", list[1+i*3], "|", list[2+i*3], "|")
        print('-------------')

def hod_player(number, simvol, list_hod):
    if number in list_hod:
        res = []
        for i in range(1,10):
            if list_hod[i-1] != number:
                res.append(list_hod[i-1])
            else:
                res.append(simvol)
        return res
    else:
        print('Неверно введено значение')

def hod_bot(simvol, list_hod):
    number = None
    while not number in list_hod:
        number = random.randint(1,9)
    res = []
    for i in range(1,10):
        if list_hod[i-1] != number:
            res.append(list_hod[i-1])
        else:
            res.append(simvol)
    return res


def check_win(list):
    if (list[0] == list[1] == list[2] or list[3] == list[4] == list[5] or list[6] == list[7] == list[8] or
    list[0] == list[3] == list[6] or list[1] == list[4] == list[7] or list[2] == list[5] == list[8] or
    list[0] == list[4] == list[8] or list[2] == list[4] == list[6]):
        return 1
    else:
        return 0




print('Выберите символ: 1 - X, 2 - O')
igroki = ['player', 'bot']
player = int(input('Ваш выбор: '))
simvoli = simvol_player(player)
simvoli = list(zip(igroki, simvoli))
print(f'Ваш символ - {simvoli[0][1]}')
list_pole = range(1,10)
pole(list_pole)
win = 0
for i in range(1,10):
    print()
    number = int(input('Введите число для хода: '))
    list_pole = hod_player(number, simvoli[0][1], list_pole)
    pole(list_pole)
    win = check_win(list_pole)
    if win == 1:
        print('Поздравляю, вы победили!')
        break
    else:
        list_pole = hod_bot(simvoli[1][1], list_pole)
        print()
        print("Ход бота!")
        pole(list_pole)
        win = check_win(list_pole)
        if win == 1:
            print('К сожалению вы проиграли')
            break