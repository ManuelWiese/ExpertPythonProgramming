import time


class MyInteger:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 0

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    my_dict = {}
    my_hash_collision_dict = {}

    for i in range(1000):
        my_dict.update({i: i})
        my_hash_collision_dict.update({MyInteger(i): i})

    pre = time.time()
    my_sum = 0
    for key in my_dict:
        my_sum += my_dict[key]
    print(my_sum)
    print(time.time() - pre)

    pre = time.time()
    my_sum = 0
    for key in my_hash_collision_dict:
        my_sum += my_hash_collision_dict[key]
    print(my_sum)
    print(time.time() - pre)
