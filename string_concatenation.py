import time
import string
import random
import matplotlib.pyplot as plt


def take_time(f):
    def wrapped(*args, **kwargs):
        pre = time.time()
        return_value = f(*args, **kwargs)
        post = time.time()
        wrapped.time = post - pre
        return return_value
    return wrapped


def run_n_times(n):
    def decorator(f):
        def wrapped(*args, **kwargs):
            for i in range(n-1):
                f(*args, **kwargs)
            return f(*args, **kwargs)
        return wrapped
    return decorator


@take_time
@run_n_times(100)
def concat(strings):
    return_value = ""
    for value in strings:
        return_value += value
    return return_value


@take_time
@run_n_times(100)
def concat_join(strings):
    return "".join(strings)


if __name__ == "__main__":
    concat_times = []
    join_times = []

    character_set = string.ascii_letters + string.punctuation
    number_of_characters = 128

    for word_length in range(number_of_characters):
        list_of_strings = [random.choice(character_set) for i in range(word_length)]
        assert concat(list_of_strings) == concat_join(list_of_strings)
        concat_times.append(concat.time)
        join_times.append(concat_join.time)

    plt.plot(list(range(number_of_characters)), concat_times)
    plt.plot(list(range(number_of_characters)), join_times)
    plt.show()
