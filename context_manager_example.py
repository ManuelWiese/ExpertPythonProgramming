import json


class DictFile:
    """This is a stupid example of a context manager that loads
    a dict from json if file existent and writes changes back to file."""

    def __init__(self, filename):
        self.filename = filename
        self.json_dict = None

    def __enter__(self):
        try:
            with open(self.filename, "r") as file_handle:
                self.json_dict = json.load(file_handle)
        except FileNotFoundError:
            self.json_dict = {}

        return self.json_dict

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.filename, "w") as file_handle:
            json.dump(self.json_dict, file_handle)


if __name__ == "__main__":
    with DictFile("test.json") as my_dict_file:
        print(my_dict_file)
        my_dict_file.update({"test": 1})
        my_dict_file.update({"test3": 0})
