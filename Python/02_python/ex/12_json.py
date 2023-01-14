import json

with open('data/movie.json', 'r', encoding='utf-8') as movie:
    text = json.load(movie)
print(text)