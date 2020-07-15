import os

import discord
import yaml
from discord.ext import commands
from dotenv import load_dotenv

import pokeapi_manager
import embed_builder

load_dotenv()
bot = commands.Bot(command_prefix='!')

config = yaml.load(open('configs//config.yml', 'r'), Loader=yaml.FullLoader)
poke_api = pokeapi_manager.PokeApiManager(config)
builder = embed_builder.EmbedBuilder(config)


@bot.command(name='poke')
async def display_pokemon(ctx, species):
    """
    Return formatted data about the 
    called pokemon by user. 
    
    @call: !poke {id or name}
    """
    pkmn_data = poke_api.get_pokemon_data(species)
    pkmn_desc = poke_api.get_pokemon_description(species)

    embed = builder.format_pokemon_message(pkmn_data, pkmn_desc)

    await ctx.channel.send(embed=embed)


bot.run(os.getenv('DISCORD_TOKEN'))