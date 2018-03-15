from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("{}: args {} kwargs {}".format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return wrapper


@log_call
def gauss(n):
    return n*(n+1)/2


@log_call
def test_function(x, y, square=True):
    if square:
        return x*x + y*y
    return x + y


if __name__ == "__main__":
    print(gauss(100))
    print(test_function(1, 2, square=True))