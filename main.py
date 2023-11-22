import random

class Fridge:

    def __init__(self,contents):
        self.contents = contents

class Ingredient:

    def __init__(self, nutritional_value, freshness):
        self.nutritional_value = nutritional_value
        self.freshness = freshness

class Dish:

    def __init__(self, ingredients, name, score):
        self.ingredients = ingredients
        self.name = name
        self.score = score