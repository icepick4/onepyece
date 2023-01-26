import unittest

from onepyece import functions, interface


class TestFunctions(unittest.TestCase):
    def test_character_by_id(self):
        character = functions.character_by_id(1)
        self.assertIsInstance(character, interface.API)
        self.assertEqual(character.id, 1)