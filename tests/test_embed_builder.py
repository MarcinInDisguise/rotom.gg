import os
import unittest
import yaml
import json
import src.embed_builder
import src.interfaces
from unittest import TestCase

class Test_EmbedBuilder(unittest.TestCase):
    """Unit tests for EmbedBuilder class"""

    config = yaml.load(open(f'./src/configs/config.yml', 'r'), Loader=yaml.FullLoader)
    pokeapi = src.interfaces.PokeAPI(config)
    embed_builder = src.embed_builder.EmbedBuilder(config, pokeapi)

    def test_pokemon_message(self):
        with open('./tests/data/pokemon_025.json') as pokemon_file, open('./tests/data/species_025.json', encoding="utf8") as species_file:
            pkmn_data = json.load(pokemon_file)
            species_data = json.load(species_file)   
            expected_result = {'thumbnail': {'url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png'}, 'author': {'name': 'rotom.gg', 'icon_url': 'https://i.imgur.com/qxnOpVb.jpg'}, 'fields': [{'inline': False, 'name': 'Basic', 'value': 'Mouse Pokémon | electric | Height: 0.4m | Weight: 6.0kg'}, {'inline': False, 'name': 'Stats', 'value': 'HP 35 / Atk 55 / Def 40 / SpA 50 / SpD 50 / Spe 90 '}, {'inline': False, 'name': '[ability] static', 'value': "Whenever a move makes contact with this Pokémon, the move's user has a 30% chance of being paralyzed.\n\nPokémon that are immune to electric-type moves can still be paralyzed by this ability.\n\nOverworld: If the lead Pokémon has this ability, there is a 50% chance that encounters will be with an electric Pokémon, if applicable."}, {
                'inline': False, 'name': '[hidden ability] lightning-rod', 'value': "All other Pokémon's single-target electric-type moves are redirected to this Pokémon if it is an eligible target.  Other Pokémon's Electric moves raise this Pokémon's Special Attack one stage, negating any other effect on it, and cannot miss it.\n\nIf the move's intended target also has this ability, the move is not redirected.  When multiple Pokémon with this ability are possible targets for redirection, the move is redirected to the one with the highest Speed stat, or, in the case of a tie, to a random tied Pokémon.  follow me takes precedence over this ability.\n\nIf the Pokémon is a ground-type and thus immune to Electric moves, its immunity prevents the Special Attack boost."}], 'type': 'rich', 'description': 'When several of\nthese POKéMON\ngather, their\x0celectricity could\nbuild and cause\nlightning storms.', 'title': '#25 pikachu'}
            embed_result = self.embed_builder.pokemon_message(pkmn_data, species_data)      
            self.assertEqual(embed_result.to_dict(), expected_result)


    def test_ability_message(self):
        with open('./tests/data/ability_blaze.json', encoding="utf8") as ability_file:
            ability_data = json.load(ability_file)
            expected_result = {'author': {'name': 'rotom.gg', 'icon_url': 'https://i.imgur.com/qxnOpVb.jpg'}, 'fields': [
                {'inline': False, 'name': 'Pokemons', 'value': 'charmander\ncharmeleon\ncharizard\ncyndaquil\nquilava\ntyphlosion\ntorchic\ncombusken\nblaziken\nchimchar\nmonferno\ninfernape\ntepig\npignite\nemboar\n**pansear**\n**simisear**\nfennekin\nbraixen\ndelphox\nlitten\ntorracat\nincineroa'}], 'type': 'rich', 'description': 'When this Pokémon has 1/3 or less of its HP remaining, its fire-type moves inflict 1.5× as much regular damage.', 'title': 'blaze'}
            embed_result = self.embed_builder.ability_message(ability_data)
            self.assertEqual(embed_result.to_dict(), expected_result)

    
    def test_item_message(self):
        with open('./tests/data/item_leftovers.json', encoding="utf8") as item_file:
            item_data = json.load(item_file)
            expected_result = {'thumbnail': {'url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/leftovers.png'}, 'author': {'name': 'rotom.gg',
                'icon_url': 'https://i.imgur.com/qxnOpVb.jpg'}, 'type': 'rich', 'description': 'Held: Heals the holder by 1/16 its max HP at the end of each turn.', 'title': 'leftovers'}
            embed_result = self.embed_builder.item_message(item_data)
            self.assertEqual(embed_result.to_dict(), expected_result)


    def test_move_message(self):
        with open('./tests/data/move_tackle.json', encoding="utf8") as move_file:
            move_data = json.load(move_file)
            expected_result = {'author': {'name': 'rotom.gg', 'icon_url': 'https://i.imgur.com/qxnOpVb.jpg'},
                               'type': 'rich', 'description': 'Inflicts regular damage.', 'title': 'tackle | Power: 40 | PP: 35 | physical'}
            embed_result = self.embed_builder.move_message(move_data)
            self.assertEqual(embed_result.to_dict(), expected_result)
