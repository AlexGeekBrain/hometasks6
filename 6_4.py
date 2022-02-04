from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        all_list = zip_longest(users, hobby, fillvalue=None)

        with open('users_&_hobby.txt', 'w', encoding='utf-8') as file:
            for i in all_list:
                print(f'{str(i[0]).strip()}: {str(i[1]).strip()}', file=file)

