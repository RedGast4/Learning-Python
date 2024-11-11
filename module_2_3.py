my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
Data_Index = int(input('Введите индекс от |1 - 12| Ввод в консоль---> ')) - 1
while index < Data_Index:
    number = my_list[index]
    index = index + 1
    if number == 0:
        continue
    elif number < 0:
        print('ERROR: stop - number < 0', number )
        break
    elif index == len(my_list):
        print(number)
    else:
        print(number)