#TiY 11-1

import unittest

from city_functions import city_country

class Cities(unittest.TestCase):
    
    def test_city_country(self):
        """results in a correct string"""
        result = city_country('santiago', 'chile')
        expected_result = 'Santiago, Chile'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()