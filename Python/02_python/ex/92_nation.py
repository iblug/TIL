import requests

names = ['min', 'hong', 'j', 'J']
for name in names:
    URL = f'https://api.nationalize.io?name={name}'

    res = requests.get(URL).json()
    data = res.get('country')[0].get('country_id')
    per = res.get('country')[0].get('probability')
    
    print(data, per)