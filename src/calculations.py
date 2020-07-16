import pokeapi
import type_weakness
import json

class Calculations:

    def __init__(self, poke_api):
        self.poke_api = poke_api


    def calc_weakness(self, first_type, second_type):
        """
        Method for calculating specific pokemon weakness
        based on file pokemon-type-chart.json.

        Method returns TypeWeakness object. 
        """
        tw = type_weakness.TypeWeakness()

        with open(f'src\\resources\\pokemon-type-chart.json') as type_chart_file:
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
