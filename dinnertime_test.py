import dinnertime
import unittest

class TestIngredient(unittest.TestCase):

    #INGREDIENT FUNCTION TESTS

    def test_print_ingredient(self):
        """
        Function to test to make sure ingredients are printed correcly
        """
        from dinnertime import Meatballs
        m = Meatballs()
        self.assertEqual(str(m),"Meatballs")

    #no tests for inspect_ingredient(): only prints things; returns nothing


class TestFridge(unittest.TestCase):

    #FRIDGE FUNCTION TESTS
    
    def test_randomize_contents_length(self):
        """
        Test to make sure the list modified by randomize_contents
        has the correct number of itmes (5)
        """
        f = dinnertime.Fridge()
        f.randomize_contents()
        self.assertEqual(len(f.contents),5)

    def test_randomize_contents_type(self):
        """
        Test to make sure all the elements in the list
        modified by randomize_contents are Ingredients
        """
        f1 = dinnertime.Fridge()
        f1.randomize_contents()
        for i in f1.contents:
            self.assertIsInstance(i,dinnertime.Ingredient)

class TestDish(unittest.TestCase):
    
    #DISH FUNCTION TESTS

    def test_dish_has_ingredients(self):
        """
        Test to check that a dish's ingredients selected by the user are
        indeed ingredients.
        """
        f1 = dinnertime.Fridge()
        f1.randomize_contents()
        d1 = dinnertime.Dish()
        self.assertIsInstance((d1.select_ingredients(f1))[0],dinnertime.Ingredient)


    def test_empty_fridge(self):
        """
        Test to make sure that if all ingredients are selected from the fridge
        that all ingredients are present in the dish's ingredients list.
        Note that since this function uses user input to select ingredients,
        user input to manually empty the fridge is required.
        """
        print("\nmanually empty the fridge for unittest")
        f1 = dinnertime.Fridge()
        f1.randomize_contents()
        d1 = dinnertime.Dish()
        self.assertEqual(len(d1.select_ingredients(f1)),5)

    def test_select_ingredients(self):
        print("\nmanually empty ingredients for unittest, again")
        f2 = dinnertime.Fridge()
        f2.randomize_contents()
        d2 = dinnertime.Dish()
        initial_fridge_contents = set(f2.contents)
        self.assertEquals(set(d2.select_ingredients(f2)),initial_fridge_contents)

    def test_make_dish_name(self):
        """
        Test to check that selecting cooking method changes the name. 
        """
        d1 = dinnertime.Dish()
        print("\nSelect 'Boiled' for unittest")
        d1.make_dish()
        self.assertEqual(d1.name,"Boiled")
    
    def test_is_edible(self):
        """
        Test to check final name generation
        """
        d1 = dinnertime.Dish()
        t1 = dinnertime.Twigs()
        i1 = dinnertime.Ice()
        t1.freshness = -5
        d1.ingredients = [t1]
        print("\nSelect 'Boiled' for unittest")
        d1.make_dish()
        d1.is_edible()
        self.assertIn('Lethal "Boiled Twigs"', d1.name)

    #no test for give_to_son() since nothing is returned and nothing is modified
    #no test for eat_dish() for the aforementioned reasons

#no tests for game class since besides introduction(), which modifies and returns nothing, the other
#function play_game() is simply the combination of all previously tested class methods. 
    
        
if __name__ == '__main__':
    unittest.main()