import json
import math
from dotenv import load_dotenv
from src import pokeapi
from src import type_weakness
from enum import Enum

class Calculations:
    
    def calc_weakness(self, pkmn: dict)->type_weakness:
        """Method for calculating specific pokemon weakness
        based on file pokemon-type-chart.json.

        Method returns TypeWeakness object. 
        """
        tw = type_weakness.TypeWeakness()

        first_type = pkmn['types'][0]['type']['name']
        second_type = None if len(pkmn['types']) == 1 else pkmn['types'][1]['type']['name']

        with open(f'./src/resources/pokemon-type-chart.json') as type_chart_file:
            type_chart = json.load(type_chart_file)

            for item in type_chart:
                if first_type in item['x0']:
                    setattr(tw, item['name'], getattr(tw, item['name']) * 0)
                if first_type in item['x2']:
                    setattr(tw, item['name'], getattr(tw, item['name']) * 2)
                if first_type in item['x1/2']:
                    setattr(tw, item['name'], getattr(tw, item['name']) * 0.5)

            if second_type == None:
                return tw

            for item in type_chart:
                if second_type in item['x0']:
                   setattr(tw, item['name'], getattr(tw, item['name']) * 0)
                if second_type in item['x2']:
                    setattr(tw, item['name'], getattr(tw, item['name']) * 2)
                if second_type in item['x1/2']:
                    setattr(tw, item['name'], getattr(tw, item['name']) * 0.5)

            return tw


    def get_attack_stat_for_level(self, pkmn: dict, level: int)->dict:
        """Get pokemon attack stat range"""
        return self.__calc_normal_stat(pkmn['stats'][self.Stats.ATTACK.value]['base_stat'], level)


    def get_defense_stat_for_level(self, pkmn: dict, level: int)->dict:
        """Get pokemon defense stat range"""
        return self.__calc_normal_stat(pkmn['stats'][self.Stats.DEFENSE.value]['base_stat'], level)


    def get_sp_attack_stat_for_level(self, pkmn: dict, level: int)->dict:
        """Get pokemon special attack stat range"""
        return self.__calc_normal_stat(pkmn['stats'][self.Stats.SPECIAL_ATTACK.value]['base_stat'], level)


    def get_sp_defense_stat_for_level(self, pkmn: dict, level: int)->dict:
        """Get pokemon special defense stat range"""
        return self.__calc_normal_stat(pkmn['stats'][self.Stats.SPECIAL_DEFENSE.value]['base_stat'], level)


    def get_speed_stat_for_level(self, pkmn: dict, level: int)->dict:
        """Get pokemon speed stat range"""
        return self.__calc_normal_stat(pkmn['stats'][self.Stats.SPEED.value]['base_stat'], level)


    def __calc_normal_stat(self, base_stat: int, level: int)->dict:
        """Calc range of min and max of normal stat (Atk, Def, SpA, SpD, Spe).

        EV - effort value
        IV - individual value
        """
        MIN_IV, MAX_IV = 0, 31,
        MIN_EV, MAX_EV = 0, 255,
        MIN_NATURE, MAX_NATURE = 0.9, 1.1

        min_stat = self.__normal_stat_formula(base_stat, MIN_IV, MIN_EV, MIN_NATURE, level)
        max_stat = self.__normal_stat_formula(base_stat, MAX_IV, MAX_EV, MAX_NATURE, level)

        return {
            "min_stat": min_stat,
            "max_stat": max_stat
        }


    def __normal_stat_formula(self, base_stat: int, iv: int, ev: int, nature: float, level: int)->int:
        """Math formula of normal stat (Atk, Def, SpA, SpD, Spe)."""
        if level in range (1, 101):
            return int(((((2*base_stat + iv + int((ev/4))) * level)/100) + 5) * nature)
        else:
            raise ValueError(f"Level {level} is not in range 1 - 100")

    
    class Stats(Enum):
        HP = 0
        ATTACK = 1
        DEFENSE = 2
        SPECIAL_ATTACK = 3
        SPECIAL_DEFENSE = 4
        SPEED = 5
