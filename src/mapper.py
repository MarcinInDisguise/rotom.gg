import json

class NameMapper:
    """Name mapper for different objects to match API specifications."""

    def __init__(self, config):
        self.config = config

    
    def map_pokemon_name(self, name_spelling):
        """Name mapper for mapping pokemon names to match API specifications.
        
        A lot of pokemon names have different variants and forms. It helps choose basic variant.
        For example species like Mimikyu has only one form in PokeApi called Mimikyu-Disquised.
        """
        name_spelling = name_spelling.lower().replace("","-")
        with open(f'./src/resources/pokemon-list.json') as pokemon_mapper_file:
            pokemon_mapper = json.load(pokemon_mapper_file)
            mapped_names = list(filter(lambda x:x["name"].startswith(name_spelling), pokemon_mapper['pokemons']))
            return mapped_names[0]['name']