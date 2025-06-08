import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN= "562e07e856aecc1ef64bfdac9514c732"
HEADER= { "Content-Type": "application/json", "trainer_token" :TOKEN }



"""body_registration={
    "trainer_token": TOKEN,
    "email": "zajcevslava164@gmail.com",
    "password": "Forward5" 
}

response = requests.post(url = f"{URL}/trainers/reg", headers=HEADER, json= body_registration)
print(response.text)"""

body_create= {
    "name": "xros",
    "photo_id": 983
}

response_create = requests.post(url = f"{URL}/pokemons", headers=HEADER, json= body_create)
print(response_create.text)

POKEMON_ID= response_create.json() ["id"]

body_new_name={
    "pokemon_id": POKEMON_ID,
    "name": "Charic",
    "photo_id": 983
}

response_change = requests.put(url = f"{URL}/pokemons", headers=HEADER, json= body_new_name )
print(response_change.text)

body_catch={
    "pokemon_id":POKEMON_ID 
}

response_catch = requests.post(url = f"{URL}/trainers/add_pokeball", headers=HEADER, json= body_catch )
print(response_catch.json())


