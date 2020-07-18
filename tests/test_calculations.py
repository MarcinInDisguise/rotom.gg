import unittest
import json
import src.calculations

class Test_Calculations(unittest.TestCase): 
    calc = src.calculations.Calculations(None)


    def test_calc_weakness(self):
        NotImplemented


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