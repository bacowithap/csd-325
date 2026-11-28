# Francisco Villa           11/27/2026
# Advanced Python           Module 7.2

import unittest
from city_functions import format_city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_location = format_city_country('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_location = format_city_country('santiago', 'chile', population=5000000)
        self.assertEqual(formatted_location, 'Santiago, Chile - population 5000000')

    def test_city_country_population_language(self):
        formatted_location = format_city_country('santiago', 'chile', population=5000000, language='spanish')
        self.assertEqual(formatted_location, 'Santiago, Chile - population 5000000, Spanish' )

if __name__ == '__main__':
    unittest.main()
