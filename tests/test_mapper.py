import os
import unittest
import json
import src.mapper
from unittest import TestCase

class Test_NameMapper(unittest.TestCase): 
    """Unit tests for NameMapper class"""

    mapper = src.mapper.NameMapper(None)

    def test_map_pokemon_name(self):
        expected_result = 'pikachu'
        result = self.mapper.map_pokemon_name('Pikachu')
        self.assertEqual(result, expected_result)

        expected_result = 'mimikyu-disguised'
        result = self.mapper.map_pokemon_name('mimikyu')
        self.assertEqual(result, expected_result)

        expected_result = 'mimikyu-disguised'
        result = self.mapper.map_pokemon_name('mimikyu Disguise')
        self.assertEqual(result, expected_result)