from Card import Card
import unittest

class CardTests(unittest.TestCase):
    def test_create_card_with_correct_suite_and_value(self):
        """testing if card can be created"""

        c1 = Card("Hearts", "A")
        c2 = Card("Diamonds", "10")

        self.assertIsInstance(c1,Card)
        self.assertEqual(c1.suit, "Hearts")
        self.assertEqual(c1.value, "A")

        self.assertIsInstance(c2,Card)
        self.assertEqual(c2.suit, "Diamonds")
        self.assertEqual(c2.value, "10")

    def test_create_card_with_incorrect_suite(self):
        """testing if exception raised when suit is incorrect"""

        with self.assertRaises(ValueError):
            c1 = Card("A","A")

    def test_create_card_with_incorrect_value(self):
        """testing if exception raised when value is incorrect"""

        with self.assertRaises(ValueError):
            c1 = Card("Hearts","11")

    def test_create_card_with_incorrect_suite_and_value(self):
        """testing if exception raised when suite and value is incorrect"""

        with self.assertRaises(ValueError):
            c1 = Card("B","11")

        with self.assertRaises(ValueError):
            c2 = Card(None, None)



if __name__ == "__main__":
    unittest.main()
