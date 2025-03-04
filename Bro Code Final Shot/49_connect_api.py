# connect to an api using python

import requests

# we are using pokemongo API as of now

base_url = "https://pokeapi.co/api/v2"

def get_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        # print("Data retrieved successfully!")
        data = response.json()
        if data:
            print(f"{data['name']}")
            print(f"{data['id']}")
            print(f"{data['height']}")
            print(f"{data['weight']}")
        # for key,value in data.items():
        #     print(f"{key} : {value}")
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokeman_name = "Typhlosion"
get_info(pokeman_name)





