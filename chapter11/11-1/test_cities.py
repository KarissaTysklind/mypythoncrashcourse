from city_functions import get_city_country
import unittest

class NamesCityCountry(unittest.TestCase):
    def test_city_country(self):
        city_country = get_city_country('madrid', 'spain')
        self.assertEqual(city_country, 'Madrid, Spain')
    
    def test_city_country_population(self):
        city_country_population = get_city_country('madrid', 'spain', '3,000,000')
        self.assertEqual(city_country_population, 'Madrid, Spain - Population 3,000,000')

if __name__ == '__main__':
    unittest.main()      