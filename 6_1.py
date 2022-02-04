from requests import get

r = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

with open('nginx_logs.txt', 'w', encoding='utf-8') as file:
    file.write(r.text)
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
        for i in content:
            print(i)
