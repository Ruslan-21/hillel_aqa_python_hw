
""" Функція, яка розрахує середнє арифметичне списку чисел
"""
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

"""  Функція, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(original_string):
    return original_string[::-1]

"""Функція рахує суму усіх парних чисел в списку"""
def sum_of_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)


"""Функція перевіряє, чи є два слова анаграмами одне одного."""
def is_anagram(word1, word2):
    """
    description
    """
    return sorted(word1) == sorted(word2)

"""Функція розраховує площу трикутника"""
def triangle_area(a, b, c):
    # if a + b <= c or a + c <= b or b + c <= a:
    #     return 0
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
