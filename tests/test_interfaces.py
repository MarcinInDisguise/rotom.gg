import os
import unittest
import yaml
import json
import src.interfaces
from unittest import TestCase

class Test_PokeApi(unittest.TestCase):
    """Integration tests for PokeApi"""

    config = yaml.load(open(f'./src/configs/config.yml', 'r'), Loader=yaml.FullLoader)
    poke_api = src.interfaces.PokeAPI(config)

    def test_get_pokemon_data(self):
        obj_name = 'bulbasaur'
        res = self.poke_api.get_pokemon_data(obj_name)
        self.assertEqual(res['name'], obj_name)


    def test_get_ability_data(self):
        """Get api reposone in json format about specified ability by id or name"""
        obj_name = 'blaze'
        res = self.poke_api.get_ability_data(obj_name)
        self.assertEqual(res['name'], obj_name)


    def test_get_item_data(self):
        """Get api reposone in json format about specified item by id or name"""
        obj_name = 'leftovers'
        res = self.poke_api.get_item_data(obj_name)
        self.assertEqual(res['name'], obj_name)


    def test_get_move_data(self):
        """Get api reposone in json format about specified move by id or name"""
        obj_name = 'tackle'
        res = self.poke_api.get_move_data(obj_name)
        self.assertEqual(res['name'], obj_name)