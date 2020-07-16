import unittest
import json
from .context import src

class Test_BuildPokemonBasicStatsText(unittest.TestCase): 
    
    def test_validate_data_correctness(self):
        embed = src.EmbedBuilder(None)

        with open(f'tests\\support\\pokemon_139.json') as json_file:
            expected_result = 'HP 70 / Atk 60 / Def 125 / SpA 115 / SpD 70 / Spe 55'
            input_f = json.load(json_file)
            result = embed.build_pokemon_basic_stats_text(input_f)
            
            self.assertEqual(expected_result, result)
    