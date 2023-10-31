#TiY 11-2 modified test_cities

import unittest

from updated_city_functions import city_country

class Cities(unittest.TestCase):

    def test_city_country(self):

        result = city_country('santiago', 'chile')
        expected_result = 'Santiago, Chile'
        self.assertEqual(result, expected_result)

    def test_city_country_population(self):
        result = city_country('santiago', 'chile', population = 5_000_000)
        expected_result = 'Santiago, Chile - population 5000000'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()