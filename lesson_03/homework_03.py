alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?" \n"That depends a good deal on where you want to get to," said the Cat. \n"I don\'t much care where ——" said Alice. \n"Then it doesn\'t matter which way you go," said the Cat. \n"—— so long as I get somewhere," Alice added as an explanation. \n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland: str = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
selected: list  = []
for  apostrophe in alice_in_wonderland:
    if apostrophe == "'":
        print(apostrophe)
# task 03 == Виведіть змінну alice_in_wonderland на друк
from itertools import count
print(f'\n task 03:\n{alice_in_wonderland}')
# """
#     # Задачі 04 -10:
#     # Переведіть задачі з книги "Математика, 5 клас"
#     # на мову пітон і виведіть відповідь, так, щоб було
#     # зрозуміло дитині, що навчається в п'ятому класі
# """
# # task 04
# """
# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# ське моря разом?
# """
# azov_sea = 37800
# black_sea = 436402
#
# string1 = f"Площа Чорного моря становить {black_sea} km\u00b2, а площа Азовського \nморя становить {azov_sea} км\u00b2. Яку площу займають Чорне та Азов-\nське море разом?"
# print(string1)
# # task 05
#  """
#  Мережа супермаркетів має 3 склади, де всього розміщено
#  375 291 товар. На першому та другому складах перебуває
#  250 449 товарів. На другому та третьому – 222 950 товарів.
#  Знайдіть кількість товарів, що розміщені на кожному складі.
#  """
# total_warehouse = 375291
# fist_second = 250449
# second_third = 222950
# string2 = f"Мережа супермаркетів має 3 склади, де всього розміщено \n{total_warehouse} товар. На першому та другому складах перебуває \n{fist_second} товарів. На другому та третьому - {second_third} товарів.\nЗнайдіть кількість товарів, що розміщені на кожному складі "
# print(string2)
# # task 06
# """
# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.
# """
# monthly_payment = 1179
# months = 18
# computer_cost = monthly_payment * months
# string3 = f"Михайло разом з батьками вирішили купити комп’ютер, ско- \nриставшись послугою «Оплата частинами». Відомо, що сплачу- \nвати необхідно буде півтора року по {monthly_payment} грн/місяць. Обчисліть \nвартість комп`ютера."
# print(string3)
#
# # task 07
# """
# Знайди остачу від діленя чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9
# """
# a = 8019 % 8
# b = 9907 % 9
# c = 2789 % 5
# d = 7248 % 6
# e = 7128 % 5
# f = 19224 % 9
#
# print(f"Знайди остачу від ділення чисел:\n"
#       f"a) 8019 : 8 = {a}\n"
#       f"b) 9907 : 9 = {b}\n"
#       f"c) 2789 : 5 = {c}\n"
#       f"d) 7248 : 6 = {d}\n"
#       f"e) 7128 : 5 = {e}\n"
#       f"f) 19224 : 9 = {f}")
#
# # task 08
# """
# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн
# """
# # Ціни на товари
# large_pizza_price = 274
# medium_pizza_price = 218
# juice_price = 35
# cake_price = 350
# water_price = 21
#
# # Кількість товарів
# large_pizza_quantity = 4
# medium_pizza_quantity = 2
# juice_quantity = 4
# cake_quantity = 1
# water_quantity = 3
#
# # Обчислення загальної вартості
# total_cost = (large_pizza_price * large_pizza_quantity) + \
#              (medium_pizza_price * medium_pizza_quantity) + \
#              (juice_price * juice_quantity) + \
#              (cake_price * cake_quantity) + \
#              (water_price * water_quantity)
#
#
# print(f"Іринка, готуючись до свого дня народження, склала список того,\n"
#       f"що їй потрібно замовити. Обчисліть, скільки грошей знадобиться\n"
#       f"для даного її замовлення.\n\n"
#       f"Назва товару\tКількість\tЦіна\n"
#       f"Піца велика\t\t\t{large_pizza_quantity}\t\t{large_pizza_price} грн\n"
#       f"Піца середня\t\t{medium_pizza_quantity}\t\t{medium_pizza_price} грн\n"
#       f"Сік\t\t\t\t\t{juice_quantity}\t\t{juice_price} грн\n"
#       f"Торт\t\t\t\t{cake_quantity}\t\t{cake_price} грн\n"
#       f"Вода\t\t\t\t{water_quantity}\t\t{water_price} грн\n\n"
#       f"Загальна вартість замовлення: {total_cost} грн")
#
# # task 09
# """
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?
# """
#
# photo = 232
# photos_pages = 8
# pages = (photo + photos_pages - 1) // photos_pages
# print(f"Ігор займається фотографією. Він вирішив зібрати всі свої {photo} \nфотографії та вклеїти в альбом. На одній сторінці може бути \nрозміщено щонайбільше {photos_pages} фото. Скільки сторінок знадобиться \nІгорю, щоб вклеїти всі фото?")
#
# # task 10
# """
# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?
# """
# distance_by_cities = 1600
# fuel_per_100km = 9
# tank_capacity = 48
# print(f"Родина зібралася в автомобільну подорож із Харкова в Буда- \nпешт. Відстань між цими містами становить {distance_by_cities} км. Відомо, \nщо на кожні 100 км необхідно {fuel_per_100km} літрів бензину. Місткість баку \nстановить {tank_capacity} літрів. \n1) Скільки літрів бензину знадобиться для такої подорожі? \n2) Скільки щонайменше разів родині необхідно заїхати на зап- \nравку під час цієї подорожі, кожного разу заправляючи пов- \nний бак?")