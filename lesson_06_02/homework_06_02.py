while True:
    word = input("Введіть слово з літерою 'h': ")
    if 'h' in word.lower():
        print("Ви ввели правильне слово:", word)
        break
    else:
        print("У слові немає літери 'h'.")