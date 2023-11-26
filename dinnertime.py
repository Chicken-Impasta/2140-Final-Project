import random
random.seed()

class Ingredient():

    def __init__(self, name=None, nutritional_value=None, freshness=None):
        """
        Returns nothing
        Initializes an ingredient object
        """
        self.nutritional_value = nutritional_value
        self.freshness = freshness
        self.name = name
    
    def __str__(self):
        """
        Returns the ingredient name as a string
        """
        return str(self.name)
    
    def inpsect_ingredient(self):
        """
        Returns nothing.
        Shows the user information regarding the nutritional value
        and freshness of an ingredient object.
        """
        print("\nYou pick up the " + str(self.name) + ".\n")
        print("Nutritional Value: " + str(self.nutritional_value))

        if str(self.name)[-1] == 's':
            if self.freshness >= 3:
                print("They're still super fresh! WOW!\n")
            elif self.freshness >= 0:
                print("They've been sitting in your fridge for a few days\n")
            elif self.freshness >= -2:
                print("They're starting to go bad...\n")
            else:
                print("They're no longer fit for human consumption... when did you buy them, again?\n")
        else:
            if self.freshness >= 3:
                print("It's super fresh! WOW!\n")
            elif self.freshness >= 0:
                print("It's been sitting in your fridge for a few days\n")
            elif self.freshness >= -2:
                print("It's starting to go bad...\n")
            else:
                print("It's no longer fit for human consumption... when did you buy this, again?\n")

        


class Meatballs(Ingredient):
    def __init__(self):
        """
        Returns nothing
        Initializes a Meatballs object
        """
        super().__init__(name="Meatballs", nutritional_value=10, freshness=random.randrange(-5,5))

class Twigs(Ingredient):
    def __init__(self):
        """
        Returns nothing
        Initializes a Twigs object
        """
        super().__init__(name="Twigs", nutritional_value=1, freshness=random.randrange(-5,5))

class Cheese(Ingredient):
    def __init__(self):
        """
        Returns nothing
        Initializes a Cheese object
        """
        super().__init__(name="Cheese", nutritional_value=7, freshness=random.randrange(-5,5))

class Pasta(Ingredient):
    def __init__(self):
        """
        Returns nothing
        Initializes a Pasta object
        """
        super().__init__(name="Pasta", nutritional_value=5, freshness=random.randrange(-5,5))

class Ice(Ingredient):
    def __init__(self):
        """
        Returns nothing
        Initializes a Ice object
        """
        super().__init__(name="Ice", nutritional_value=1, freshness=random.randrange(-5,5))

class Fridge():

    def __init__(self,contents=[]):
        """
        Returns nothing
        Initializes a Fridge object
        by default contents is an empty list (fridge is empty)
        """
        self.contents = contents
    
    def __str__(self):
        """
        Returns the contents of the fridge as a string in a user-readable format
        """
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
        """
        Returns nothing
        Updates the fridge contents to a random assortment of five ingredients, in which
        there may be multiples of the same ingredient and some ingredients may not 
        be present
        """
        ingredients_list = [Meatballs(), Twigs(),Cheese(),Pasta(),Ice()]
        self.contents = []
        for i in range(5):
            ingredient_picker = ingredients_list[random.randrange(0,len(ingredients_list))]
            self.contents.append(ingredient_picker)

class Dish:

    def __init__(self, name=None, score=0,ingredients=[]):
        self.ingredients = ingredients
        self.name = name
        self.score = score

    def select_ingredients(self,fridge):
        print("Let's get cooking! First select the ingredients")
        contents_dict = {i:0 for i in set(fridge.contents)}
        key = 'y'
        for i in contents_dict:
            for j in fridge.contents:
                if j == i:
                    current_count = contents_dict.get(i)
                    current_count += 1
                    contents_dict.update({i:current_count})
        while key!='n':
            ingredient_number_pairs = []
            shelf_number = 1
            for i in contents_dict:
                current_line = "{} | x{} {}"
                current_line = current_line.format(shelf_number,str(contents_dict.get(i)),str(i))
                ingredient_number_pairs.append((shelf_number,i))
                shelf_number += 1                
                print(current_line)
            selection = input("\nType the number of the desired ingredient to include it in your dish\n")
            for i in ingredient_number_pairs:
                if int(selection) == i[0]:
                    fridge.contents.remove(i[1])
                    current_count = contents_dict.get(i[1])
                    contents_dict.update({i[1]:(current_count-1)})
                    self.ingredients.append(i[1])
                    print("\nAdded " + str(i[1]) + "!")
            if not fridge.contents:
                print("Your fridge is now empty.\n")
                key = 'n'
            else:
                key = input("\nContinue adding ingredients? (y/n): ")
        return self.ingredients
            
        
