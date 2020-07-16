import pokeapi
import discord
from enum import Enum

class EmbedBuilder:

    def __init__(self, config):
        self.config = config       
        self.bot_name = "rotom.gg"


    def open_pokeapi(self):
        self.poke_api = pokeapi.PokeAPI(self.config)


    def pokemon_message(self, pkmn_data, pkmn_desc):
        """
        Build embed message about specific pokemon.
        """
        flavor_text = list(filter(lambda x:x['language']['name']=='en', pkmn_desc['flavor_text_entries']))

        embed=discord.Embed(title=f"#{pkmn_data['id']} {pkmn_data['species']['name']}", url="", description=flavor_text[0]['flavor_text'])
        embed.set_author(name=self.bot_name, icon_url=self.config['rotomgg']['icon_url'])
        embed.set_thumbnail(url=pkmn_data['sprites']['front_default'])
        embed.add_field(name='Basic', value=self.__build_pokemon_default_data_text(pkmn_data, pkmn_desc), inline=False)
        embed.add_field(name='Stats', value=self.__build_pokemon_basic_stats_text(pkmn_data), inline=False)

        for ability in self.__build_abilities_list(pkmn_data):
            embed.add_field(name=ability['name'], value=ability['effect'], inline=False)

        return embed


    def __build_pokemon_basic_stats_text(self, pkmn_data):
        """
        Build default data about base stats 
        of specific pokemon.

        Remove last two chars from string to 
        get rid of unnecessary end "/ ".  
        """
        pkmn_stats = pkmn_data['stats']
        counter = 0
        text = ''

        for stat in self.Stats:
            text += f"{stat.value} {pkmn_stats[counter]['base_stat']} / "
            counter += 1

        return text[:-2]


    def __build_pokemon_default_data_text(self, pkmn_data, pkmn_desc):
        """
        Build default data about specific pokemon.
        """
        genra = list(filter(lambda x:x['language']['name']=='en', pkmn_desc['genera']))

        if len(pkmn_data['types']) == 2:
            type_text = f"{pkmn_data['types'][0]['type']['name']} / {pkmn_data['types'][1]['type']['name']}"
        else:
            type_text = pkmn_data['types'][0]['type']['name'] 

        return f"{genra[0]['genus']} | {type_text} | Height: {pkmn_data['height']/10}m | Weight: {pkmn_data['weight']/10}kg"


    def __build_abilities_list(self, pkmn_data):
        res = []

        for ability in pkmn_data['abilities']:
            ability_precisely_data = self.poke_api.get_pokemon_abilities_from_url(ability['ability']['url'])
            effect_entries = list(filter(lambda x:x['language']['name']=='en', ability_precisely_data['effect_entries']))
            if ability['is_hidden']:
                ability_type = 'hidden ability'
            else:
                ability_type = 'ability'

            data = {
                'name': f"[{ability_type}] {ability['ability']['name']}", 
                'effect': effect_entries[0]['effect']
            }

            res.append(data)

        return res
    

    class Stats(Enum):
        HP = 'HP'
        ATTACK = 'Atk'
        DEFENSE = 'Def'
        SPECIAL_ATTACK = 'SpA'
        SPECIAL_DEFENSE = 'SpD'
        SPEED = 'Spe'


