from json import load

with open('news.json', 'r') as json_file:
    json_content = load(json_file)

print(sorted(json_content, key=lambda i: i['created'], reverse=True))
