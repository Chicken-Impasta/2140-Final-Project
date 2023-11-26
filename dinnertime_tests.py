import dinnertime
import unittest

class FactTest(unittest.TestCase):

    #INGREDIENT FUNCTION TESTS

    def test_print_ingredient(self):
        """
        Function to test to make sure ingredients are printed correcly
        """
        from dinnertime import Meatballs
        m = Meatballs()
        self.assertEqual(str(m),"Meatballs")

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
    
    #DISH FUNCTION TESTS

    def dish_has_ingredients(self):
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
        f1 = dinnertime.Fridge()
        f1.randomize_contents()
        d1 = dinnertime.Dish()
        self.assertEquals(len(d1.select_ingredients(f1)),5)
    
        

if __name__ == '__main__':
    unittest.main()