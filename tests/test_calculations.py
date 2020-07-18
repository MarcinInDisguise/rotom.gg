import unittest
import json
import src.calculations
import src.type_weakness
from unittest import TestCase

class Test_Calculations(unittest.TestCase): 
    calc = src.calculations.Calculations()


    def test_calc_weakness(self):
        #check when pokemon has 2 types
        with open(f'tests\\support\\pokemon_139.json') as f:
            data = json.load(f)
            result_weaknesses = self.calc.calc_weakness(data)
            expected_weaknesses = src.type_weakness.TypeWeakness()
            expected_weaknesses.normal = 0.5
            expected_weaknesses.fire = 0.25
            expected_weaknesses.ice = 0.5
            expected_weaknesses.electric = 2.0
            expected_weaknesses.grass = 4.0
            expected_weaknesses.fighting = 2.0
            expected_weaknesses.poison = 0.5
            expected_weaknesses.ground = 2.0
            expected_weaknesses.flying = 0.5
            
            self.assertEqual(vars(expected_weaknesses), vars(result_weaknesses))

        #check when pokemon has 1 typee
        with open(f'tests\\support\\pokemon_025.json') as f:
            data = json.load(f)
            result_weaknesses = self.calc.calc_weakness(data)
            expected_weaknesses = src.type_weakness.TypeWeakness()
            expected_weaknesses.electric = 0.5
            expected_weaknesses.ground = 2
            expected_weaknesses.flying = 0.5
            expected_weaknesses.steel = 0.5
            
            self.assertEqual(vars(expected_weaknesses), vars(result_weaknesses))


    def test_get_attack_stat_for_level(self):
        with open(f'tests\\support\\pokemon_139.json') as f:
            data = json.load(f)

            # Verify when level is set to 1 
            expected_min_stat, expected_max_stat = 5, 7
            result_stats = self.calc.get_attack_stat_for_level(data, 1)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 50
            expected_min_stat, expected_max_stat = 58, 123
            result_stats = self.calc.get_attack_stat_for_level(data, 50)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 100
            expected_min_stat, expected_max_stat = 112, 240
            result_stats = self.calc.get_attack_stat_for_level(data, 100)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 0 - expected raised ValueError exception
            with self.assertRaises(ValueError) as context:
                self.calc.get_attack_stat_for_level(data, 0)

            self.assertTrue("Level 0 is not in range 1 - 100", str(context.exception))     

            # Verify when level is set to -1 - expected raised ValueError exception
            with self.assertRaises(ValueError) as context:
                self.calc.get_attack_stat_for_level(data, -1)

            self.assertTrue("Level 0 is not in range 1 - 100", str(context.exception))


    def test_get_defense_stat_for_level(self):     
        with open(f'tests\\support\\pokemon_139.json') as f:
            data = json.load(f)

            # Verify when level is set to 50
            expected_min_stat, expected_max_stat = 117, 194
            result_stats = self.calc.get_defense_stat_for_level(data, 50)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 100
            expected_min_stat, expected_max_stat = 229, 383
            result_stats = self.calc.get_defense_stat_for_level(data, 100)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 0 - expected raised ValueError exception
            with self.assertRaises(ValueError) as context:
                self.calc.get_defense_stat_for_level(data, 0)

            self.assertTrue("Level 0 is not in range 1 - 100", str(context.exception))     

            # Verify when level is set to -1 - expected raised ValueError exception
            with self.assertRaises(ValueError) as context:
                self.calc.get_defense_stat_for_level(data, -1)

            self.assertTrue("Level 0 is not in range 1 - 100", str(context.exception))


    def test_get_sp_attack_stat_for_level(self):      
        with open(f'tests\\support\\pokemon_139.json') as f:
            data = json.load(f)

            # Verify when level is set to 50
            expected_min_stat, expected_max_stat = 108, 183
            result_stats = self.calc.get_sp_attack_stat_for_level(data, 50)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 100
            expected_min_stat, expected_max_stat = 211, 361
            result_stats = self.calc.get_sp_attack_stat_for_level(data, 100)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 0 - expected raised ValueError exception
            with self.assertRaises(ValueError) as context:
                self.calc.get_sp_attack_stat_for_level(data, 0)

            self.assertTrue("Level 0 is not in range 1 - 100", str(context.exception))     

            # Verify when level is set to -1 - expected raised ValueError exception
            with self.assertRaises(ValueError) as context:
                self.calc.get_sp_attack_stat_for_level(data, -1)

            self.assertTrue("Level 0 is not in range 1 - 100", str(context.exception))


    def test_get_sp_defense_stat_for_level(self):       
        with open(f'tests\\support\\pokemon_139.json') as f:
            data = json.load(f)

            # Verify when level is set to 50
            expected_min_stat, expected_max_stat = 67, 134
            result_stats = self.calc.get_sp_defense_stat_for_level(data, 50)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 100
            expected_min_stat, expected_max_stat = 130, 262
            result_stats = self.calc.get_sp_defense_stat_for_level(data, 100)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 0 - expected raised ValueError exception
            with self.assertRaises(ValueError) as context:
                self.calc.get_sp_defense_stat_for_level(data, 0)

            self.assertTrue("Level 0 is not in range 1 - 100", str(context.exception))     

            # Verify when level is set to -1 - expected raised ValueError exception
            with self.assertRaises(ValueError) as context:
                self.calc.get_sp_defense_stat_for_level(data, -1)

            self.assertTrue("Level 0 is not in range 1 - 100", str(context.exception))


    def test_get_speed_stat_for_level(self):
        with open(f'tests\\support\\pokemon_139.json') as f:
            data = json.load(f)

            # Verify when level is set to 50
            expected_min_stat, expected_max_stat = 54, 117
            result_stats = self.calc.get_speed_stat_for_level(data, 50)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 100
            expected_min_stat, expected_max_stat = 103, 229
            result_stats = self.calc.get_speed_stat_for_level(data, 100)

            self.assertEqual(expected_min_stat, result_stats['min_stat'])
            self.assertEqual(expected_max_stat, result_stats['max_stat'])

            # Verify when level is set to 0 - expected raised ValueError exception
            with self.assertRaises(ValueError) as context:
                self.calc.get_speed_stat_for_level(data, 0)

            self.assertTrue("Level 0 is not in range 1 - 100", str(context.exception))     

            # Verify when level is set to -1 - expected raised ValueError exception
            with self.assertRaises(ValueError) as context:
                self.calc.get_speed_stat_for_level(data, -1)
                
            self.assertTrue("Level 0 is not in range 1 - 100", str(context.exception))