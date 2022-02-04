from sys import argv
from itertools import zip_longest

user, hob, f = argv[1:]

with open(fr'{user}\users.csv', 'r', encoding='utf-8') as users:
    with open(fr'{hob}\hobby.csv', 'r', encoding='utf-8') as hobby:
        all_list = zip_longest((' '.join(user.split(',')) for user in users), hobby, fillvalue=None)

        with open(fr'{f}\users_&_hobby.txt', 'w', encoding='utf=8') as file:
            for i in all_list:
                print(f'{str(i[0]).strip()}: {str(i[1]).strip()}', file=file)
