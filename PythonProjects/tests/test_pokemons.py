import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '6c6bd8b0ec5a4f37f3f6a0cdf2869649'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '2196'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]['name'] =='Бульбазавр'


def test_part_of_response_trainer():
    response_trainer_name = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_trainer_name.json()["data"][0]['trainer_name'] =='Анастасия'


def test_trainers_status_code():
    response_code = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response_code.status_code == 200    


@pytest.mark.parametrize('key,value', [('name', 'Бульбазавр'),('trainer_id',TRAINER_ID),('id','28429')])
def test_parametrie(key,value):
    response_parametrize = requests.get(url=f'{URL}/pokemons',params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value        

    