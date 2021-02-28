import json

class RecipeManual:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


class RecipeJson:
    def __init__(self, name):
        self.name = name
        with open(name) as json_file:
            self.ingredients = json.load(json_file)  # TODO: implement correclty

