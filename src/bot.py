import os

import discord
import yaml
from discord.ext import commands
from dotenv import load_dotenv

import calculations
import pokeapi
import embed_builder

load_dotenv()
bot = commands.Bot(command_prefix='!')

config = yaml.load(open(f'src\\configs\\config.yml', 'r'), Loader=yaml.FullLoader)

poke_api = pokeapi.PokeAPI(config)
calc = calculations.Calculations(poke_api)
builder = embed_builder.EmbedBuilder(config)
builder.open_pokeapi()


@bot.command(name='poke')
async def display_pokemon(ctx, species):
    """
    Return formatted data about the 
    called pokemon by user. 
    
    @call: !poke {id or name}
    """
    pkmn_data = poke_api.get_pokemon_data(species)
    pkmn_desc = poke_api.get_pokemon_description(species)

    embed = builder.pokemon_message(pkmn_data, pkmn_desc)

    await ctx.channel.send(embed=embed)


@bot.command(name="weak")
async def display_weakness(ctx, species):
    """
    Return formated data about the called
    pokemon weakness.
    """
    pkmn_data = poke_api.get_pokemon_data(species)
    if len(pkmn_data['types']) == 1:
        weakness = calc.calc_weakness(pkmn_data['types'][0]['type']['name'], None)
    else:
        weakness = calc.calc_weakness(pkmn_data['types'][0]['type']['name'], pkmn_data['types'][1]['type']['name'])

    embed = builder.type_weakness_message(pkmn_data, weakness)

    await ctx.channel.send(embed=embed)


bot.run(os.getenv('DISCORD_TOKEN'))