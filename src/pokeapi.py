import yaml
import requests
import pathlib

class PokeAPI:

    def __init__(self, config):
        self.config = config
        self.basic_url = config['pokeapi_url']


    def get_pokemon_data(self, species):
        """
        Get api response in json format about specific pokemon 
        by species id or name.
        """
        url = f'{self.basic_url}/pokemon/{species}'
        try:
            return requests.get(url).json()
        except Exception as ex:
            return ex

    
    def get_pokemon_description(self, species):
        """
        Get api response in json format about specific pokemon 
        species by species id or name.
        """
        url = f'{self.basic_url}/pokemon-species/{species}'
        try:
            return requests.get(url).json()
        except Exception as ex:
            return ex


    def get_type_weakness(self, ptype):
        """
        Get api response in json format about
        all weaknesses of specific type.
        """
        url = f'{self.basic_url}/type/{ptype}'
        try:
            return requests.get(url).json()
        except Exception as ex:
            return ex
       

    def get_pokemon_abilities_from_url(self, url):
        """
        Get api response in json format about 
        specific ability from api by premade url 
        from other response.
        """
        try:    
            return requests.get(url).json()
        except Exception as ex:
            return ex


    


