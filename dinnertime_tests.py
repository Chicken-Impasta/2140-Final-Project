import dinnertime
import unittest

class FactTest(unittest.TestCase):

    #INGREDIENT TESTS

    def test_print_ingredient(self):
        """
        Function to test to make sure ingredients are printed correcly
        """
        from dinnertime import Meatballs
        m = Meatballs()
        self.assertEqual(str(m),"Meatballs")

    #FRIDGE TESTS
    
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
        

if __name__ == '__main__':
    unittest.main()