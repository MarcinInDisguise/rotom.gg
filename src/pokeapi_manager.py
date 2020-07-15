import yaml
import requests
import pathlib

class PokeApiManager:
    def __init__(self, config):
        self.config = config
        self.basic_url = config['pokeapi_url']


    def get_pokemon_data(self, species):
        url = f'{self.basic_url}/pokemon/{species}'
        try:
            return requests.get(url).json()
        except Exception as ex:
            return ex

    
    def get_pokemon_description(self, species):
        url = f'{self.basic_url}/pokemon-species/{species}'
        try:
            return requests.get(url).json()
        except Exception as ex:
            return ex


    def get_pokemon_abilities_from_url(self, url):
        try:    
            return requests.get(url).json()
        except Exception as ex:
            return ex

    


