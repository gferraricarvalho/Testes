import unittest
from SourceDate import get_date

class TestGetDate(unittest.TestCase):

    def test_get_date(self):
        date_str = "24 de Agosto de 2023 - 25 de Agosto de 2023"
        result = get_date(date_str)
        self.assertEqual(result, 1)
        
    def test_get_date_data_minuscula(self):
        date_str = "24 de agosto de 2023 - 25 de agosto de 2023"
        result = get_date(date_str)
        self.assertEqual(result, 1)
        
    def test_get_date_data_acima_de_31(self):
        date_str = "24 de Agosto de 2023 - 32 de Agosto de 2023"
        result = get_date(date_str)
        self.assertEqual(result, 1)
        
    def test_get_date_barras(self):
        date_str = "24/08/2023 - 25/08/2023"
        result = get_date(date_str)
        self.assertEqual(result, 1)
        
    def test_get_date_mes_numeros(self):
        date_str = "24 de 08 de 2023 - 25 de 08 de 2023"
        result = get_date(date_str)
        self.assertEqual(result, 1)

    def test_get_date_invalid(self):
        date_str = "Data inválida"
        with self.assertRaises(ValueError):
            get_date(date_str)
            

if __name__ == '__main__':
    unittest.main()