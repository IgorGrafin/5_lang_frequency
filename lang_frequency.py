import sys
import re
from collections import Counter


def load_data(file_path):
    with open(file_path, "r") as file:
        return file.read()


def get_most_frequent_words(text, number_of_words):
    words = re.findall("\w+", text.lower())
    return Counter(words).most_common(number_of_words)


if __name__ == "__main__":
    number_of_words = 10
    try:
        input_data = load_data(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File {} not found".format(sys.argv[1]))
    except IndexError:
        sys.exit("Please, put a file name as a parameter.\n"
                 "For example: 'python pprint_json.py in.json' ")

    dictionary = get_most_frequent_words(input_data, number_of_words)
    print(number_of_words, "of the most frequent words")
    for word, count in dictionary:
        print(word, " : ", count)
