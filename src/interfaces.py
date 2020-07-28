from discord.ext import commands, tasks
import yaml
import requests
import pathlib
import dbl
import asyncio

class PokeAPI:

    def __init__(self, config):
        self.config = config


    def get_pokemon_data(self, species):
        """ Get api response in json format about specified pokemon by species id or name."""
        return self.__build_api_request('pokemon', species)

    
    def get_pokemon_description(self, species):
        """Get api response in json format about specified pokemon species by species id or name."""
        return self.__build_api_request('pokemon-species', species)


    def get_ability_data(self, ability):
        """Get api response in json format about specified ability by id or name."""
        return self.__build_api_request('ability', ability)


    def get_item_data(self, item):
        """Get api reposone in json format about specified item by id or name"""
        return self.__build_api_request('item', item)


    def get_move_data(self, move):
        """Get api reposone in json format about specified move by id or name"""
        return self.__build_api_request('move', move)


    def get_type_weakness(self, ptype: str):
        """Get api response in json format about all weaknesses of specific type."""
        return self.__build_api_request('type', ptype)


    def get_data_from_url(self, url):
        """Get api response in json format about specific ability from api by premade url from other response."""
        try:    
            return requests.get(url).json()
        except Exception as ex:
            return ex


    def __build_api_request(self, endpoint, arg):
        """ Send request to pokeapi with specified endpoint and arg"""
        try:
            return requests.get(f"{self.config['pokeapi_url']}/{endpoint}/{arg}").json()
        except Exception as ex:
            return ex


class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""
    
    def __init__(self, bot, token):
        self.dblpy = dbl.DBLClient(bot, token)
        self.update_stats.start()


    def cog_unload(self):
        self.update_stats.cancel() 


    @tasks.loop(minutes=30.0)
    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count"""
        try:
            await self.dblpy.post_guild_count()
        except:
            pass