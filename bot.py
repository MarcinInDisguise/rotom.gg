import os

import discord
import yaml
from discord.ext import commands
from dotenv import load_dotenv

from src import calculations
from src import pokeapi
from src import embed_builder

load_dotenv()
bot = commands.Bot(command_prefix='!')

config = yaml.load(open(f'./src/configs/config.yml', 'r'), Loader=yaml.FullLoader)

poke_api = pokeapi.PokeAPI(config)
calc = calculations.Calculations()
builder = embed_builder.EmbedBuilder(config, poke_api)

@bot.command(name='poke')
async def display_pokemon(ctx, species: str):
    """Send formatted data about the 
    called pokemon by user. 
    
    call: !poke {id or name}
    """
    pkmn_data = poke_api.get_pokemon_data(species)
    pkmn_desc = poke_api.get_pokemon_description(species)

    embed = builder.pokemon_message(pkmn_data, pkmn_desc)

    await ctx.channel.send(embed=embed)


@bot.command(name="weak")
async def display_weakness(ctx, species: str):
    """Send formated data about the called
    pokemon weakness.

    call: !weak {name}
    """
    pkmn_data = poke_api.get_pokemon_data(species)
    weakness = calc.calc_weakness(pkmn_data)
    embed = builder.type_weakness_message(pkmn_data, weakness)

    await ctx.channel.send(embed=embed)


@bot.command(name="speed")
async def display_speed(ctx, species: str, level: int = 50):
    """Send formated data about the 
    pokemon min-max speed stat based 
    on specified level.

    call: !speed {pokemon} {level}
    call: !speed {pokemon}
    """
    try:
        pkmn_data = poke_api.get_pokemon_data(species)
        speed_stat = calc.get_speed_stat_for_level(pkmn_data, level)
        embed = builder.stat_message(pkmn_data, speed_stat, level, 'speed')

        await ctx.channel.send(embed=embed)
    except ValueError as ex:
        await ctx.channel.send(ex)


bot.run(os.getenv('DISCORD_TOKEN'))

