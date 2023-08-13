# Para ejecutar colocamos en la consola
#!python -m unittest test_areafunction
#areaXunittest#.py
import unittest
from math import pi
from areafunction import area

class Test_Area(unittest.TestCase):
    def test_area(self):
        print('Valores de área conocidos')
        self.assertAlmostEqual(area(1),pi)

