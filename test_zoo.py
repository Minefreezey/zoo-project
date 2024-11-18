import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(7), 50)
    
    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(18), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(35), 150)

    def test_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(111), 100)

    def test_belowZero_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-2), -1)
       
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()