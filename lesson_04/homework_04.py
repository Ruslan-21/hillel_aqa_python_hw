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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
text = adwentures_of_tom_sawer.replace("\n", "")
print(text)
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
text = re.sub(r"\s*\.{4}\s*", " ", adwentures_of_tom_sawer)
print(text)
# або такий варіант, але замінює на 4 пробіли
text = adwentures_of_tom_sawer.replace("....", " ")
print(text)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
text_one_space: list = " ".join(adwentures_of_tom_sawer.split())
print(text_one_space)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print(f"Зустрічається літера 'h' {count_h} разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()
count = sum(1 for word in words if word.istitle())

print(f"Кількість слів, що починаються з великої літери: {count}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_index = adwentures_of_tom_sawer.find("Tom")
second_index = adwentures_of_tom_sawer.find("Tom", first_index + 1) if first_index != -1 else -1
if second_index != -1:
    print(f'Зустрічається слово "Tom": {second_index}')
else:
    print("Слово 'Tom' зустрічається менше двох разів.")
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

print(adwentures_of_tom_sawer_sentences)
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
sentences = adwentures_of_tom_sawer.splitlines()

if len(sentences) >= 4:
    fourth_sentence = sentences[3].strip()
    print(fourth_sentence.lower())
else:
    print("Четверте речення не знайдено.")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
sentences = adwentures_of_tom_sawer.splitlines()
for sentence in sentences:
    if sentence.strip().startswith("By the time"):
        print(f"Знайдено речення: {sentence.strip()}")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
text = adwentures_of_tom_sawer.split(". ")
sentence = text[-1]
words_sentence = sentence.split()

print(f"Кількість слів в останньому реченні: {len(words_sentence)}")