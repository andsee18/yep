import unittest
from test_parser import parse_hh

class TestParser(unittest.TestCase):
    def test_parse_hh(self):
        """
        Тестирует функцию parse_hh на наличие вакансий для запроса 'Python developer'.
        """
        query = 'Python developer'
        vacancies = parse_hh(query)
        self.assertTrue(len(vacancies) > 0, f"No vacancies found for query: {query}")

if __name__ == '__main__':
    unittest.main()