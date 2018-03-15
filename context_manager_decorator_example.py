from contextlib import contextmanager
import json


@contextmanager
def dict_file(filename):
    try:
        with open(filename, "r") as file_handle:
            json_dict = json.load(file_handle)
    except FileNotFoundError:
        json_dict = {}

    try:
        yield json_dict
    except Exception as e:
        print("An exception occured: {}".format(e))
        raise
    else:
        with open(filename, "w") as file_handle:
            json.dump(json_dict, file_handle)


if __name__ == "__main__":
    with dict_file("test.json") as my_dict_file:
        print(my_dict_file)
        my_dict_file.update({"test": 1})
        my_dict_file.update({"test3": 0})
