# For downloading requests library, run: pip install requests

import requests

base_URL = "https://pokeapi.co/api/v2/"

def getName(pokemon_name):
    
    new_URL = f"{base_URL}/pokemon/{pokemon_name}" 
    response = requests.get(new_URL)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"ERROR of {response.status_code} : {response.reason}")
        
    
pokemon_name = input("Enter a pokemon name for details : ")
# pokemon_name = "ditto"
pokemon_details = getName(pokemon_name)

if pokemon_details:
    print(f"Name : {pokemon_details['name'].capitalize()}")
    print(f"id = {pokemon_details['base_experience']}")
    print(f"height : {pokemon_details['height']}")
    print(f"weight : {pokemon_details['weight']}")
