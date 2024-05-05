is_year_leap = int(input('Какой год проверить? '))

if is_year_leap % 4 != 0:
    print('False. Год не високосный.')

elif is_year_leap % 100 == 0:
    if is_year_leap % 400 == 0:
        print('True. Год високосный.')
    else:
        print('False. Год не високосный.')
else:
    print('True. Год високосный.')