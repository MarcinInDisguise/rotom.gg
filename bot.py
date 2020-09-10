import os

import discord
import yaml
from discord.ext import commands
from dotenv import load_dotenv
from src import interfaces
from src import calculations
from src import embed_builder
from src import mapper

load_dotenv()
bot = commands.Bot(command_prefix='!')

config = yaml.load(open(f'./src/configs/config.yml', 'r'), Loader=yaml.FullLoader)

poke_api = interfaces.PokeAPI(config)
calc = calculations.Calculations()
builder = embed_builder.EmbedBuilder(config, poke_api)
name_mapper = mapper.NameMapper(config)


@bot.command(name='poke')
async def pokemon_command(ctx, species):
    """Send formatted data about the called pokemon by user. 
    
    command: !poke {id or name}
    """
    formatted_species_name = name_mapper.map_pokemon_name(species)
    pkmn_data = poke_api.get_pokemon_data(formatted_species_name)
    pkmn_desc = poke_api.get_pokemon_description(formatted_species_name)
    embed = builder.pokemon_message(pkmn_data, pkmn_desc)

    await ctx.channel.send(embed=embed)


@bot.command(name="ability")
async def ability_command(ctx, ability):
    """Send formatted data about the called ability by user

    command: !ability {id or name}
    """
    ability_data = poke_api.get_ability_data(ability)
    embed = builder.ability_message(ability_data)

    await ctx.channel.send(embed=embed)


@bot.command(name="item")
async def item_command(ctx, item):
    """Send formatted data about the called item by user

    command: !item {id or name}
    """
    item_data = poke_api.get_item_data(item)
    embed = builder.item_message(item_data)

    await ctx.channel.send(embed=embed)


@bot.command(name="move")
async def move_command(ctx, move):
    """Send formatted data about the called move by user

    command: !move {id or name}
    """
    move_data = poke_api.get_move_data(move)
    embed = builder.move_message(move_data)

    await ctx.channel.send(embed=embed)


@bot.command(name="weak")
async def weakness_command(ctx, species: str):
    """Send formated data about the called pokemon weakness.

    command: !weak {name}
    """
    formatted_species_name = name_mapper.map_pokemon_name(species)
    pkmn_data = poke_api.get_pokemon_data(formatted_species_name)
    weakness = calc.calc_weakness(pkmn_data)
    embed = builder.type_weakness_message(pkmn_data, weakness)

    await ctx.channel.send(embed=embed)


@bot.command(name="speed")
async def speed_command(ctx, species: str, level: int = 50):
    """Send formated data about the pokemon min-max speed stat based 
    on specified level. Default pokemon level is set to 50 - it is the 
    most popular format in competitive.

    command: !speed {pokemon} <level>
    """
    try:
        formatted_species_name = name_mapper.map_pokemon_name(species)
        pkmn_data = poke_api.get_pokemon_data(formatted_species_name)
        speed_stat = calc.get_speed_stat_for_level(pkmn_data, level)
        embed = builder.stat_message(pkmn_data, speed_stat, level, 'speed')

        await ctx.channel.send(embed=embed)
    except ValueError as ex:
        await ctx.channel.send(ex)


bot.run(os.getenv('DISCORD_TOKEN'))
bot.add_cog(interfaces.TopGG(bot))