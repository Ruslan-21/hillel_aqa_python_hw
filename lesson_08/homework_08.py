data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]



def summa():
    for n in data:
        try:
            total_sum = sum((int(p)) for p in n.split(","))
            print(total_sum)
        except ValueError:
            print("Не можу це зробити")


summa()


