import discord
from dotenv import load_dotenv
from src import pokeapi
from src import type_weakness
from enum import Enum

class EmbedBuilder:

    def __init__(self, config: dict, poke_api: pokeapi.PokeAPI):
        self.config = config
        self.poke_api = poke_api
        self.bot_name = config['rotomgg']['bot_name']
        

    def pokemon_message(self, pkmn_data: dict, pkmn_desc: dict)->discord.embeds.Embed:
        """Build embed message about specific pokemon."""
        flavor_text = list(filter(lambda x:x['language']['name']=='en', pkmn_desc['flavor_text_entries']))

        embed=discord.Embed(title=f"#{pkmn_data['id']} {pkmn_data['species']['name']}", url="", description=flavor_text[0]['flavor_text'])
        embed.set_author(name=self.bot_name, icon_url=self.config['rotomgg']['icon_url'])
        embed.set_thumbnail(url=pkmn_data['sprites']['front_default'])
        embed.add_field(name='Basic', value=self.__build_pokemon_default_data_text(pkmn_data, pkmn_desc), inline=False)
        embed.add_field(name='Stats', value=self.__build_pokemon_basic_stats_text(pkmn_data), inline=False)

        for ability in self.__build_abilities_list(pkmn_data):
            embed.add_field(name=ability['name'], value=ability['effect'], inline=False)

        return embed


    def type_weakness_message(self, pkmn_data: dict, weakness: type_weakness.TypeWeakness)->discord.embeds.Embed:
        """Build embed message about specific pokemon's weakness."""
        formated_weakness = self.__build_effectiveness_data(weakness)

        embed=discord.Embed(title=f"#{pkmn_data['id']} {pkmn_data['species']['name']}", description="(ignoring abilities)")
        embed.set_author(name=self.bot_name, icon_url=self.config['rotomgg']['icon_url'])
        embed.set_thumbnail(url=pkmn_data['sprites']['front_default'])
        embed.add_field(name='Weaknesses', value=formated_weakness['weaknesses'] or '-', inline=False)
        embed.add_field(name='Resistances', value=formated_weakness['resistances'] or '-', inline=False)
        embed.add_field(name='Immunities', value=formated_weakness['immunities'] or '-', inline=False)

        return embed


    def stat_message(self, pkmn_data: dict, stat: dict, level: int, stat_name: str)->discord.embeds.Embed:
        """
        Build embed message about specific pokemon's min-max 
        speed stat in specified level.
        """
        embed=discord.Embed(title=f"#{pkmn_data['id']} {pkmn_data['species']['name']} lv {level} - {stat_name} stat",  description=f"{stat['min_stat']} - {stat['max_stat']}")
        embed.set_author(name=self.bot_name, icon_url=self.config['rotomgg']['icon_url'])
        embed.set_thumbnail(url=pkmn_data['sprites']['front_default'])

        return embed


    def __build_pokemon_basic_stats_text(self, pkmn_data: dict)->str:
        """
        Format default data about base stats 
        of specific pokemon.

        Remove last two chars from string to 
        get rid of unnecessary end "/ ".  
        """
        pkmn_stats = pkmn_data['stats']
        counter, text = 0, ''

        for stat in self.Stats:
            text += f"{stat.value} {pkmn_stats[counter]['base_stat']} / "
            counter += 1

        return text[:-2]


    def __build_pokemon_default_data_text(self, pkmn_data: dict, pkmn_desc: dict)->str:
        """Format default data about specific pokemon."""
        genra = list(filter(lambda x:x['language']['name']=='en', pkmn_desc['genera']))

        if len(pkmn_data['types']) == 2:
            type_text = f"{pkmn_data['types'][0]['type']['name']} / {pkmn_data['types'][1]['type']['name']}"
        else:
            type_text = pkmn_data['types'][0]['type']['name'] 

        return f"{genra[0]['genus']} | {type_text} | Height: {pkmn_data['height']/10}m | Weight: {pkmn_data['weight']/10}kg"


    def __build_abilities_list(self, pkmn_data: dict)->list:
        """Format list with data about specific pokemon's abilities."""
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
    

    def __build_effectiveness_data(self, weakness: type_weakness.TypeWeakness)->dict:
        '''Format data about specific pokemon's weakness. 

        If type weakness is hyper un/effective (x4 or 
        0.25) make type bold.

        Remove last two chars from string to 
        get rid of unnecessary end ", ".  
        '''
        weaknesses = ''
        resistances = ''
        immunities = ''

        for ptype in dir(weakness):
            if ptype.startswith('_'):
                continue

            if getattr(weakness, ptype) == 4:
                weaknesses += f'**{ptype}**, '
            if getattr(weakness, ptype) == 2:
                weaknesses += f'{ptype}, '
            if getattr(weakness, ptype) == 0.5:
                resistances += f'{ptype}, '
            if getattr(weakness, ptype) == 0.25:
                resistances += f'**{ptype}**, '
            if getattr(weakness, ptype) == 0:
                immunities += f'{ptype}, '
            
        return { 
            'weaknesses': weaknesses[:-2], 
            'resistances': resistances[:-2], 
            'immunities': immunities[:-2] 
        }


    class Stats(Enum):
        HP = 'HP'
        ATTACK = 'Atk'
        DEFENSE = 'Def'
        SPECIAL_ATTACK = 'SpA'
        SPECIAL_DEFENSE = 'SpD'
        SPEED = 'Spe'


