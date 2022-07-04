# Задание: создать программу, возвращающую список чисел
# Фибоначчи с помощью итератора.

from itertools import takewhile, islice


def fib(n):
    result = [0, 1]
    if n == 0:
        return [0]
    else:
        while result[-1] + result[-2] <= n:
            result.append(result[-1] + result[-2])
        return result


class FibonacchiList:
    def __init__(self, data):
        self.result = [0, 1]
        self.idx = -1
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx == 0:
            return 0
        elif self.idx == 1:
            return 1
        else:
            if self.result[-1] + self.result[-2] <= max(self.data):
                self.result.append(self.result[-1] + self.result[-2])
                del self.result[0]
                while self.result[-1] not in self.data:
                    self.result.append(self.result[-1] + self.result[-2])
                    if self.result[-1] + self.result[-2] > max(self.data):
                        raise StopIteration
                    del self.result[0]
                return self.result[-1]
            else:
                raise StopIteration


def fib_iter(numbers):
    return takewhile(lambda x: x <= max(numbers), fibonacci_gen())


def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibo4(n):
    gen = fibonacci_gen()
    for i in range(n):
        print(next(gen))


def test_fibo_1():
    assert fib(10) == [0, 1, 1, 2, 3, 5, 8], "fib(10) != [0, 1, 1, 2, 3, 5, 8]"


def test_fibo_2():
    assert list(FibonacchiList([0, 1, 5, 10])) == [0, 1, 1, 5], "list(FibonacchiList([0, 1, 5, 10])) != [0, 1, 1, 5]"


def test_fibo_3():
    assert list(islice(fibonacci_gen(), 9)) == [0, 1, 1, 2, 3, 5, 8, 13, 21], "list(islice(fibonacci_gen(), 9)) != [0, 1, 1, 2, 3, 5, 8, 13, 21]"


def test_fibo_4():
    assert list(fib_iter(range(5))) == [0, 1, 1, 2, 3], "list(fib_iter(range(5))) == [0, 1, 1, 2, 3]"


if __name__ == '__main__':
    test_fibo_1()
    test_fibo_2()
    test_fibo_3()
    test_fibo_4()
    fibo4(10)