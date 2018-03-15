import random

class RandomNumbers:
    def __init__(self, size):
        self.size = size

    def __iter__(self):
        return self

    def __next__(self):
        if self.size <= 0:
            raise StopIteration
        self.size -= 1
        return random.random()


if __name__ == "__main__":
    for number in RandomNumbers(10):
        print(number)

    print("The iterator can be used to create lists")
    print(list(RandomNumbers(3)))

