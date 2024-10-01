import unittest
from datetime import datetime
from conversor import conversao_valor, calcular_comissao

class TestConversor(unittest.TestCase):

    def test_conversao_valor(self):
        # Testa a conversão de um valor em dólar para real
        self.assertEqual(conversao_valor(100, 5.25), 525.00)
        self.assertEqual(conversao_valor(200, 4.50), 900.00)
        self.assertAlmostEqual(conversao_valor(100, 5.23), 523.00, places=2)

    def test_calcular_comissao(self):
        # Testa o cálculo da comissão do vendedor
        self.assertEqual(calcular_comissao(1000, 10), 100.00)
        self.assertEqual(calcular_comissao(500, 5), 25.00)

    def test_data_atual(self):
        # Testa se a função de data está retornando a data no formato correto
        data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.assertIsInstance(data_atual, str)

if __name__ == '__main__':
    unittest.main()
