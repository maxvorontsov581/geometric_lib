import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_triangle_int_first(self):
        self.assertEqual(area(5), 5 * 8 / 2)

    def test_triangle_int_second(self):
        self.assertEqual(area(57285), 57285 * 57285 / 2)

    def test_triangle_string_first(self):
        with self.assertRaises(TypeError):
            area("85")

    def test_triangle_string_second(self):
        with self.assertRaises(TypeError):
            area("ITMO")

    def test_triangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True)

    def test_triangle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False)

    def test_triangle_negaive_int_first(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_triangle_negaive_int_second(self):
        with self.assertRaises(ValueError):
            area(-59853)

    def test_triangle_zero_int(self):
        with self.assertRaises(ValueError):
            area(0)

class trianglePerimeterTestCase(unittest.TestCase):
    def test_triangle_int_first(self):
        self.assertEqual(perimeter(9, 8), 9 + 8 + 1)

    def test_triangle_int_second(self):
        self.assertEqual(perimeter(394732, 123450), 39473 + 123450 + 198345)

    def test_triangle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("85", "35")

    def test_triangle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("ITMO", "type")

    def test_triangle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True)

    def test_triangle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter( False)

    def test_triangle_negaive_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 158)

    def test_triangle_negaive_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-59853, -15)

    def test_triangle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0, 19)

if __name__ == '__main__':
    unittest.main()
