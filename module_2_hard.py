import random

def get_fist():
    numbers_l = list(range(3, 21))
    fist = random.choice(numbers_l)
    return fist

def get_passwords(n):
    password = {}
    password.update({3: 12,
                     4: 13,
                     5: 1423,
                     6: 121524,
                     7: 162534,
                     8: 13172635,
                     9: 1218273645,
                     10: 141923283746,
                     11: 11029384756,
                     12: 12131511124210394857,
                     13: 112211310495867,
                     14: 1611325212343114105968,
                     15: 1214114232133124115106978,
                     16: 1317115262143531341251161079,
                     17: 11621531441351261171089,
                     18: 12151811724272163631545414513612711810,
                     19: 118217316415514613712811910,
                     20: 13141911923282183731746416515614713812911})
    password = password.get(n)
    return password

g = get_fist()
print('------------hardcode------------------------')
print('Шифр:', g)

looker = list(range(1, g))
grand_looker = list(range(1, g))
pairs = []
result = ''

for i in looker:
    for j in grand_looker:
        pn1 = i
        pn2 = j
        if pn1 >= pn2:
            continue
        else:
            sum_ = g % (pn1 + pn2)
            if sum_ == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print('Пары чисел', *pairs)
print('Введите пароль: ', result, 'во вторую вставку')
if int(result) == get_passwords(g):
    print('Госпади Египет, вы намудрили')
print('--------------------------------------------')