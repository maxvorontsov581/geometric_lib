import unittest
import math
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_int_first(self):
        self.assertEqual(area(5, 19), 5 * 19)

    def test_rectangle_int_second(self):
        self.assertEqual(area(57285, 187533), 57285 * 187533)

    def test_rectangle_string_first(self):
        with self.assertRaises(TypeError):
            area("85", "92")

    def test_rectangle_string_second(self):
        with self.assertRaises(TypeError):
            area("85", 19)

    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True, False)

    def test_rectangle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False, False)

    def test_rectangle_negaive_int_first(self):
        with self.assertRaises(ValueError):
            area(-5, 8)

    def test_rectangle_negaive_int_second(self):
        with self.assertRaises(ValueError):
            area(-59853, -15)

    def test_rectangle_zero_int(self):
        with self.assertRaises(ValueError):
            area(0, 8)

class RectanglePerimeterTestCase(unittest.TestCase):
    def test_rectangle_int_first(self):
        self.assertEqual(perimeter(5, 19), 2 * (5 + 19))

    def test_rectangle_int_second(self):
        self.assertEqual(perimeter(57285, 187533), 2 * (57285 + 187533))

    def test_rectangle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("85", "92")

    def test_rectangle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("85", 19)

    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True, False)

    def test_rectangle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False, False)

    def test_rectangle_negaive_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 8)

    def test_rectangle_negaive_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-59853, -15)

    def test_rectangle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0, 8)

if __name__ == '__main__':
    unittest.main()
