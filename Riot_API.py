import requests

API_KEY = "RGAPI-eca03f3c-493e-4dfd-8160-3b271d3a0687"

default_region_code = "euw1"

default_region = "europe"

url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Aatricks?api_key=" + API_KEY

def get_summoner_info(summoner_name=None, region=default_region_code):
    if not summoner_name:
        summoner_name= input("Enter summoner name: ")
    
    api_url="https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/Aatricks?api_key={}".format(region, API_KEY)
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(err)
        return None

def get_summoner_id(dict):
    return dict["id"]
    
def get_summoner_rank(summoner_id, region=default_region_code):
    api_url="https://{}.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}".format(region, summoner_id, API_KEY)
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        r= response.json()
        print (response.json()[0]["tier"], response.json()[0]["rank"], "with {} LP, in {} wins and {} losses".format(response.json()[0]["leaguePoints"], response.json()[0]["wins"], response.json()[0]["losses"]))
    except requests.exceptions.RequestException as err:
        print(err)
        return None

get_summoner_rank(get_summoner_id(get_summoner_info()))