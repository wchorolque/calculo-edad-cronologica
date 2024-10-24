import unittest

from datetime import date

from src.calculadora import determinar_edad 

class CalculadoraTests(unittest.TestCase):
    def test_mismo_dia_caso1(self):
        today = date(2024, 10, 24)
        result = determinar_edad(today, today)

        assert 0 == result[0]
        assert 0 == result[1]
        assert 0 == result[2]

    def test_mismo_dia_caso2(self):
        today = date(2016, 2, 8)
        result = determinar_edad(today, today)

        assert 0 == result[0]
        assert 0 == result[1]
        assert 0 == result[2]

    def test_diferencia_un_dia_caso1(self):
        today =  date(2024, 10, 24)
        tomorrow = date(2024, 10, 25)
        result = determinar_edad(today, tomorrow)

        assert 0 == result[0]
        assert 0 == result[1]
        assert 1 == result[2]

    def test_diferencia_un_dia_caso2(self):
        today =  date(2016, 2, 8)
        tomorrow = date(2016, 2, 9)
        result = determinar_edad(today, tomorrow)

        assert 0 == result[0]
        assert 0 == result[1]
        assert 1 == result[2]


    def test_caso1(self):
        fecha = date(1959, 10, 26)
        fecha_actual = date(2024, 10, 24)
        result = determinar_edad(fecha, fecha_actual)

        assert 64 == result[0]
        assert 11 == result[1]
        assert 29 == result[2]

    def test_caso2(self):
        fecha = date(1999, 12, 12)
        fecha_actual = date(2024, 10, 24)
        result = determinar_edad(fecha, fecha_actual)

        assert 24 == result[0]
        assert 10 == result[1]
        assert 12 == result[2]

    def test_caso3(self):
        fecha = date(2016, 2, 8)
        fecha_actual = date(2024, 10, 24)
        result = determinar_edad(fecha, fecha_actual)

        assert 8 == result[0]
        assert 8 == result[1]
        assert 16 == result[2]