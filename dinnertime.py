import random
random.seed()
contents = []

class Ingredient():

    def __init__(self, name=None, nutritional_value=None, freshness=None):
        self.nutritional_value = nutritional_value
        self.freshness = freshness
        self.name = name
    
    def __str__(self):
        return str(self.name)



class Meatballs(Ingredient):

    def __init__(self):
        """
        function to initialize Meatballs object
        """
        super().__init__(name="Meatballs", nutritional_value=10, freshness=random.randrange(-5,5))

class Twigs(Ingredient):

    def __init__(self):
            """
            function to initialize Twiggs obejct
            """
            super().__init__(name="Twigs", nutritional_value=1, freshness=random.randrange(-5,5))

class Cheese(Ingredient):

    def __init__(self):
            super().__init__(name="Cheese", nutritional_value=7, freshness=random.randrange(-5,5))

class Pasta(Ingredient):

    def __init__(self):
            super().__init__(name="Pasta", nutritional_value=5, freshness=random.randrange(-5,5))

class Ice(Ingredient):

    def __init__(self):
            super().__init__(name="Ice", nutritional_value=1, freshness=random.randrange(-5,5))

class Fridge():

    def __init__(self,contents):
        self.contents = contents
    
    def __str__(self):
        print("Inside the fridge you find...\n")
        contents_dict = {i:0 for i in set(self.contents)}
        for i in contents_dict:
            for j in self.contents:
                if j == i:
                    current_count = contents_dict.get(i)
                    current_count += 1
                    contents_dict.update({i:current_count})
        for i in contents_dict:
            current_line = "x{} {}"
            current_line = current_line.format(str(contents_dict.get(i)),str(i))
            print(current_line)
        return ""
    
    def randomize_contents(self):
        ingredients_list = [Meatballs(), Twigs(),Cheese(),Pasta(),Ice()]
        for i in range(5):
            ingredient_picker = ingredients_list[random.randrange(0,len(ingredients_list))]
            self.contents.append(ingredient_picker)

class Dish:

    def __init__(self, ingredients, name, score):
        self.ingredients = ingredients
        self.name = name
        self.score = score

m = Meatballs()
F1 = Fridge(contents)
F1.randomize_contents()
print(F1)
