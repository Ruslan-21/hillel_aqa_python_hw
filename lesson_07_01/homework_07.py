# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def summ(a, b):
    print(a + b)
summ(5, 7)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average():
    return sum(numbers) / len(numbers)
numbers = (5, 10, 15, 17, 21)
print(f"Середне арифметичне: {average()}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_order(text):
    return text[::-1]
text = "Hello World!"
print(f"{reverse_order(text)}")
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def word():
    return max(txt, key=len)
txt = ['Hello', "Hi", 'By Byy']
print(word())
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
# task 7
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
def text_space():
    return adwentures_of_tom_sawer.replace("\n", " ")
print(text_space())
# task 8
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
def text_word():
    return adwentures_of_tom_sawer.count('h')
print(text_word())
# task 9
""" Перевірте чи починається якесь речення з "By the time".
"""
def text_four():
    sentences = adwentures_of_tom_sawer.split('.')
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence.startswith("By the time"):
            return True
    return False

print(text_four())
# task 10
def filter(numbers):
    return [pairs for pairs in numbers if pairs % 2 == 0]

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(filter(number))
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""