from functools import wraps
#Task1

def numbers_generator(N):
    for num in range(0, N, 2):
        yield num
    yield N + 1

for value in numbers_generator(21):
    print(value)

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in fibonacci(21):
 print(num)



#Task2
class reverse_iterator:
    def __init__(self, data):
        self.stack = []
        for item in data:
            self.stack.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        return self.stack.pop()
lst = [1, 2, 3, 4]
for item in reverse_iterator(lst):
    print(item)



class even_numbers_Iterator:
    def __init__(self, N):
        if type(N) != int:
            raise TypeError("N number must be an integer")
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

        if not isinstance(N, int):
         raise TypeError("N number must be an integer")


#Task3

def log_result(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception {func.__name__}: {e}")
            return None
    return wrapper



@log_result
@catch_exceptions
def divide(a, b):
    return a / b

divide(21, 11)
divide(5, 0)