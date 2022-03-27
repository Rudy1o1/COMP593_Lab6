import requests
from sys import argv

def main():
    #get the pokemon name
    pokemon_name = argv[1]

    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:

        pb_string = get_title_and_text(pokemon_info)

        pb_url = post_to_pastebin(pb_string[0], pb_string[1])

        print(pb_url)

def get_pokemon_info(pokemon_name):

    print("Getting Pokemon information...", end=" ")
    
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(URL + str(pokemon_name))

    if response.status_code == 200:
        print('success')
        return response.json() # Convert response body to a dictionary

    else:
        print('failed. Response code:', response.status_code)
        return

def get_title_and_text(pokemon_name):

    title = pokemon_name['name'] + "'s Ability"

    body_text=""

    for poke_abi in pokemon_name['abilities']:

        body_text += "-" + poke_abi['ability']['name']+"\n"
    
    return (title, body_text)

def post_to_pastebin(title, body_text):
     
    print("Posting to PasteBin...", end='')

    Params = {
    'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
    'api_option': 'paste',
    'api_paste_code': body_text,
    'api_paste_name': title
    }

    response = requests.post("https://pastebin.com/api/api_post.php", data=Params)

    if response.status_code == 200:
        print('success')
        return response.text # Convert response body to a string

    else:
        print('failed. Response code:', response.status_code)
        return response.status_code 

main()
    