from collections import defaultdict


def count_characters(string):
    character_counts = defaultdict(int)
    for character in string:
        character_counts[character] += 1

    return character_counts


if __name__ == "__main__":
    print(count_characters("hello how are you today?"))
