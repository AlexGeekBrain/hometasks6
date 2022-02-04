from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as a:
    with open('bakery.csv', 'r', encoding='utf-8') as r:
        if len(argv) > 1 and [i for i in argv[1:] if '.' in i and i.replace('.', '').isdigit()]:
            if round(float(argv[1]), 3) <= 1000000.00:
                print(f'{round(float(argv[1]), 3):>010}', file=a)
            else:
                print('Число не можеть быть больше 1000000.00')
        else:
            print(r.read())
