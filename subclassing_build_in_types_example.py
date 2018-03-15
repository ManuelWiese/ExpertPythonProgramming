class TypedList(list):
    def __init__(self, T, iterable=None):
        self.T = T
        super().__init__()
        if iterable is not None:
            self.extend(iterable)

    def append(self, item):
        if isinstance(item, self.T):
            super().append(item)
        else:
            raise TypeError

    def insert(self, position, item):
        if isinstance(item, self.T):
            super().insert(position, item)
        else:
            raise TypeError

    def extend(self, iterable):
        for item in iterable:
            if not isinstance(item, self.T):
                raise TypeError
        super().extend(iterable)


if __name__ == "__main__":
    typedList = TypedList(int, [0,1])
    typedList.append(10)
    typedList.insert(0, 2)
    typedList.extend(range(10))
    typedList.extend([])
    print(typedList)
