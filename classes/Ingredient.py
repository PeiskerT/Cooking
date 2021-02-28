class Ingredient:
    def __init__(self, name, amount, measurementUnit, position = None):
        self.name = name
        self.amount = amount
        self.unit = measurementUnit
        self.position = position  # location of this item in your supermarket (REWE Schlüterhallen in my case)

