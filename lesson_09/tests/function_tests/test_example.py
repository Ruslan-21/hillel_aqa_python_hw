import unittest
from lesson_09.homework_09 import calculate_average, reverse_string, sum_of_even_numbers, is_anagram, triangle_area



class MyTest(unittest.TestCase):


    def test_average_positive(self):
        result = calculate_average([5, 4, 3])
        self.assertEqual(result, 4)


    def test_average_negative(self):
        result = calculate_average([5, 4, 3])
        self.assertEqual(result, 3)

class MyTest(unittest.TestCase):

    def test_reverse_string_positive(self):
        my_string = "Hello"
        result = reverse_string(my_string)
        self.assertEqual(result, "olleH")

    def test_reverse_string_negative(self):
        my_string = "Hello"
        result = reverse_string(my_string)
        self.assertEqual(result, "Hello")


class MyTest(unittest.TestCase):

    def test_sum_of_even_numbers_positive(self):
        number = [1,2,3,4,5]
        result = sum_of_even_numbers(number)
        self.assertEqual(result, 6)

    def test_sum_of_even_numbers_negative(self):
        number = [1,2,3,4,5]
        result = sum_of_even_numbers(number)
        self.assertEqual(result, 3 )

class MyTest(unittest.TestCase):

    def test_is_anagram_positive(self):
        word1 = "word"
        word2 = "owrd"
        result = is_anagram(word1, word2)
        self.assertTrue(result)



    def test_is_anagram_negative(self):
        word1 = "word"
        word2 = "owrq"
        result = is_anagram(word1, word2)
        self.assertTrue(not result)

class MyTest(unittest.TestCase):

    def test_triangle_area_positive(self):
        a = 5
        b = 6
        c = 7
        result = triangle_area(a,b,c)
        self.assertTrue(result >= 14.69)


    def test_triangle_area_negative(self):
        a = 4
        b = 5
        c = 9
        result = triangle_area(a,b,c)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
