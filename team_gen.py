import requests
import random

def generate():

    team_dict = {}

    for count in range(6): # generates 6 pokemon
        
        random_mon = random.randint(1, 1010) # generates a random number representing dex number
        api_url = f"https://pokeapi.co/api/v2/pokemon-species/{random_mon}" # gets the pokemon's species from API
        response = requests.get(api_url)
        pokemon = response.json() # turns the response into a dictionary
        ability_list = []

        if pokemon['forms_switchable'] or len(pokemon['varieties']) > 1: # checks if the pokemon has multiple forms/varieties
            
            if len(pokemon['varieties']) > 1: # checks if the pokemon has multiple varieties
                random_variety = random.randint(0, len(pokemon['varieties']) - 1) # if they do then it picks a random form/variety
                
                ability_list = []
                
                variety_page = pokemon['varieties'][random_variety]['pokemon']['url'] # gets the page of the specific variety
                response = requests.get(variety_page)
                pokemon = response.json() # re-initialises the pokemon dictionary with the variety's page
                
                abilities = pokemon['abilities']
                for count in range(len(abilities)): # loops through the abilities
                    ability_list.append(abilities[count]['ability']['name']) # adds the abilities to a list
                
                team_dict[f"{pokemon['name']}"] = { # add the generated pokemon to a team dictionary
                    'abilities' : ability_list,
                    'sprite' : pokemon['sprites']['front_default']}
                
            else:
                api_url = f"https://pokeapi.co/api/v2/pokemon/{random_mon}"
                response = requests.get(api_url)
                pokemon = response.json()
                
                
                random_form = random.randint(0, len(pokemon['forms']) - 1)
                
                if random_form == 17 and random_mon == 493:
                    random_form = random.randint(0, len(pokemon['forms']) - 1)
                    
                ability_list = []
                abilities = pokemon['abilities']
                
                for count in range(len(abilities)):
                    ability_list.append(abilities[count]['ability']['name'])
                
                form_page = pokemon['forms'][random_form]['url']
                response = requests.get(form_page)
                pokemon = response.json() # re-initialises the pokemon dictionary with the form's page
                
                    
                team_dict[f"{pokemon['name']}"] = {
                    'abilities' : ability_list,
                    'sprite' : pokemon['sprites']['front_default']}

        else:
                api_url = f"https://pokeapi.co/api/v2/pokemon/{random_mon}"
                response = requests.get(api_url)
                pokemon = response.json()
                
                ability_list = []
                abilities = pokemon['abilities']
                for count in range(len(abilities)):
                    ability_list.append(abilities[count]['ability']['name'])
                
                team_dict[f"{pokemon['name']}"] = {
                    'abilities' : ability_list,
                    'sprite' : pokemon['sprites']['front_default']}

    print(team_dict)
    pokemon_list = list(team_dict.keys())
    print(pokemon_list)
generate()