import random
import time
import subprocess
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
    
    def inspect_ingredient(self):
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
        print("\nInside the fridge you find...\n")
        contents_names = [i.name for i in self.contents]
        contents_dict = {i:0 for i in set(contents_names)}
        for i in contents_dict:
            for j in self.contents:
                if j.name == i:
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
            ingredients_list = [Meatballs(), Twigs(),Cheese(),Pasta(),Ice()]

class Dish:

    def __init__(self, name=None, score=0,ingredients=[]):
        """
        Returns nothing
        Initializes a Dish object
        """
        self.ingredients = ingredients
        self.name = name
        self.score = score

    def select_ingredients(self,fridge):
        """
        Returns a list of Ingredients
        Lets the user select ingredients to be used in a dish, as many as they desire,
        until there are no more ingredients left in the fridge. After selecting a 
        particular ingredient type, the user may either choose to inspect the 
        individual ingredients, or just skip and have a random one chose for them. 
        Note that once the user selects a particular ingredient type they cannot go 
        back to them "main ingredient menu"-- this is by design. 
        """
        print("\nFirst select the ingredients")
        self.ingredients = []
        contents_names = [i.name for i in fridge.contents]
        contents_dict = {i:0 for i in set(contents_names)}
        key = 'y'
        for i in contents_dict:
            for j in fridge.contents:
                if j.name == i:
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
            selection = input("\n\033[1mType the number of the desired ingredient to include it in your dish\033[0m ")
            specific_ingredients_list = []
            for i in ingredient_number_pairs:
                if int(selection) == i[0]:
                    for j in fridge.contents:
                        if j.name == i[1]:
                            specific_ingredients_list.append(j)
            inspect_key = 'n'
            while inspect_key != 'y':
                shelf_number = 1
                ingredient_number_pairs = []
                print("")
                for z in specific_ingredients_list:
                    current_line = "{}| {}"
                    current_line = current_line.format(shelf_number, str(z))
                    ingredient_number_pairs.append((shelf_number,z))
                    shelf_number += 1
                    print(current_line)
                selection = input("\n\033[1mtype number of ingredient to inspect, or ENTER for random selection\033[0m ")
                if selection != '':
                    for v in ingredient_number_pairs:
                        if int(selection) == v[0]:
                            v[1].inspect_ingredient()
                            inspect_key = input("Add ingredient? (y/n) ")
                            if inspect_key == 'y':
                                fridge.contents.remove(v[1])
                                current_count = contents_dict.get(v[1].name)
                                contents_dict.update({v[1].name:(current_count-1)})
                                self.ingredients.append(v[1])
                                print("\n\033[1mAdded " + str(v[1]) + "!\033[0m")
                else:
                    if len(specific_ingredients_list) > 1:
                        selection = random.randrange(1,len(specific_ingredients_list))
                    else:
                        selection = 1
                    for g in ingredient_number_pairs:
                        if int(selection) == g[0]:
                            fridge.contents.remove(g[1])                       
                            current_count = contents_dict.get(g[1].name)
                            contents_dict.update({g[1].name:(current_count-1)})
                            self.ingredients.append(g[1])
                            print("\n\033[1mAdded " + str(g[1]) + "!\033[0m")
                            inspect_key = 'y'  
            if not fridge.contents:
                print("\nYour fridge is now empty.")
                key = 'n'
            else:
                key = input("\nContinue adding ingredients? (y/n): ")
        return self.ingredients

    def make_dish(self):
        """
        Returns nothing
        function to allow the user to choose a cooking method, modifying the name of the dish 
        and calculating the total score for the dish using the selected ingredients.
        """
        cooking_methods = ["Boiled","Fried"]
        counter = 0
        print("\nLet's get cooking! How are you going to prepare this dish?\n")
        for i in cooking_methods:
            cooking_methods_menu = "{} | {}"
            cooking_methods_menu = cooking_methods_menu.format(counter,i)
            print(cooking_methods_menu)
            counter += 1
        method = input("\n\033[1mType the number of the desired cooking method\033[0m ")
        for i in cooking_methods:
            if method == str(cooking_methods.index(i)):
                method = i
        self.name = method
        freshness_score = 0
        nutrition_score = 0
        for i in self.ingredients:
            nutrition_score += i.nutritional_value
            if i.freshness < -2:
                freshness_score -= 20
            else:
                freshness_score += i.freshness
        self.score = nutrition_score / 2 + freshness_score
    
    def is_edible(self):
        """
        Returns nothing
        Modifies the name of the dish based on its previously calculated score.
        """
        if self.score >= 10:
            self.name = "Delicious " + '"' + self.name
        elif self.score >= 5:
            self.name = "Palatable " + '"' + self.name
        elif self.score >= 0:
            self.name = "Inedible " + '"' + self.name
        else:
            self.name = 'Lethal ' + '"' + self.name
        ingredients_name = set(self.ingredients)
        for i in ingredients_name:
            self.name = self.name + " " + i.name
        foods = ["Casserole", "Muffins", "Lasagna", "Stew", "Monstrousity"]
        self.name = self.name + '" ' + foods[random.randrange(len(foods))]

    def give_to_son(self):
        """
        Returns nothing
        Serves as the ending point to the game, in which the son responds appropriately
        to what he has just been given. 
        """
        game_over = "\n----GAME OVER----"
        print("\n\n\nYou give the '" + self.name + "' to your hungry son!\n")
        if "Lethal" in self.name:
            print("Your son is now foaming at the mouth! Time to call poison control.")
            print(game_over)
        elif "Inedible" in self.name:
            print("Your son is thouroughly disgusted by what he has just eaten.")
            print('\n"Food is either eaten for enjoyment or for fuel. This falls into the fuel category." \nhe tells you before leaving the house to walk off what he has just ingested.')
            print(game_over)
        elif "Palatable" in self.name:
            print("Your son asks you why you didn't just heat up instant noodles instead.")
            print(game_over)
        else:
            print("Your son loves it.")
            print("\n'I have a new favorite food, it's: '" + self.name + "'.' he says.")
            print(game_over)
        
    def eat_dish(self):
        """
        Returns nothing
        Controls the outcome of the user eating the dish themselves
        based on the score of the dish
        """
        game_over = "\n----GAME OVER----"
        print("\n\n\nYou decide to eat the '" + self.name + "' yourself.\n")
        if "Lethal" in self.name:
            print("You fall, convulsing, to the floor after one bite! Time to call poision control.")
            print(game_over)
        elif "Inedible" in self.name:
            print("It's disgusting. Maybe cooking just isn't for you.")
            print(game_over)
        elif "Palatable" in self.name:
            print("It's ok, but you think you are going to just make instant noodles next time")
            print("\nYour son comes downstairs and asks where dinner is. Someone has some explaining to do.")
            print(game_over)
        else:
            print("It's delicious!")
            print("\nYour son comes downstairs and asks where dinner is. Someone has some explaining to do.")
            print(game_over)


class Game():

    def __intit__(self):
        """
        Returns nothing
        Initializes a Game object
        """
        self.mode = None
    
    def introduction(self):
        """
        Returns nothing
        Reads out the introductory message from a file, to be implimemnted at the start of a game
        """
        with open("intro.txt",'rt') as myFile:
            line = 'x'
            while line:
                line = myFile.readline()
                print(line)
    
    def play_game(self):
        """
        Returns nothing
        controls the game state
        """
        key = 'x'
        while key:
            self.introduction()
            key = input("\033[1mpress ENTER to continue\033[0m ")
        key = 'x'
        f = Fridge()
        f.randomize_contents()
        while key:
            print(f)
            key = input("\033[1mpress ENTER to continue\033[0m ")
        key = 'x'
        d = Dish()
        d.select_ingredients(f)
        d.make_dish()
        d.is_edible()
        print("\nYou sit and wait for your dish to cook...")
        time.sleep(3)
        print("\n...it's finished! You made: " + '\033[1m'+ d.name + '\033[0m')
        key = input("\n\033[1mEat the " + d.name + " yourself? (y/n)\033[0m ")
        if key == 'y':
            d.eat_dish()
        else:
            d.give_to_son()
        
class Hardmode(Game):

    def __init__(self):
        """
        Returns nothing
        initializes hardmode object
        """
        super().__init__()
        self.score = 0

    def play_game(self):
        """
        Returns nothing
        controls the game state, for hardmode the rules are displayed along with the
        normal introduction. If the dish requirement is not met, the player's
        computer will be force restarted. If the timer runs out while the player
        is in the process of creating a dish, they will still get to finish 
        their current dish before they have to face the consequences. 
        """
        key = 'x'
        while key:
            self.introduction()
            print("\033[1myou have 15 seconds to make 5 dishes for you hungry son before he runs upstairs and restarts your computer,")
            print("deleting all of your unsaved work and open tabs! What a pest!")
            
            key = input("\npress ENTER to continue\033[0m ")
        start = time.time()
        while time.time() - start < 15:
            key = 'x'
            f = Fridge()
            f.randomize_contents()
            while key:
                print(f)
                key = input("\033[1mpress ENTER to continue\033[0m ")
            key = 'x'
            d = Dish()
            d.select_ingredients(f)
            d.make_dish()
            d.is_edible()
            print("\nYou sit and wait for your dish to cook...")
            time.sleep(3)
            print("\n...it's finished! You made: " + '\033[1m'+ d.name + '\033[0m')
            self.score += 1
        if self.score >= 5:
            print("WOW! You cook fast!")
        else:
            print("\n\n\033[1mTIME IS UP. You rush upstairs to find your hungry son restarting your computer\033[0m")
            print("\nAs he restarts your computer, your son locks eyes with you as he says:")
            print('\n"The greatest glory in living lies not in never falling,')
            print('but in rising every time we fall."')
            print("\n(you made " + str(self.score) +" dishes)")
            time.sleep(10)
            subprocess.call(["shutdown", "-r", "-t", "0"])

if __name__ == '__main__':
    mode_selection = input("\033[1mType gamemode selection (Normal/Hard)\033[0m ")
    if mode_selection == "Normal" or mode_selection == "normal":
        g1 = Game()
        g1.play_game()
    else:
        g1 = Hardmode()
        g1.play_game()

