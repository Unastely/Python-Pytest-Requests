import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '6c6bd8b0ec5a4f37f3f6a0cdf2869649'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "unastelya@yandex.ru",
    "password": "Iloveqa111"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change = {
    "pokemon_id": "28426",
    "name": "New Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_catch = {
    "pokemon_id": "28426"
}



'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)
'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER,json = body_confirmation)
print(response_confirmation.text)'''



'''Создание покемона'''
'''response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER,json=body_create) 
print(response_create.status_code)'''


'''message = response_create.json()['message']
print(message)
'''

'''Изменение покемона'''
'''response_change = requests.put(url=f'{URL}/pokemons', headers=HEADER,json=body_change) 
print(response_change.text)'''


'''Поймать покемона в покебол'''
'''response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_catch)
print(response_catch.text)'''