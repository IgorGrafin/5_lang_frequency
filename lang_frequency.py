import sys
import re
import timeit
import collections


def load_data(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def get_most_frequent_words(text, number_of_words):
    dictionary = collections.Counter()
    for line in text:
        words = re.findall("\w+", line.lower())
        dictionary = add_to_dict(words, dictionary)
    return dictionary.most_common(number_of_words)


def add_to_dict(input_words, dictionary):
    for word in input_words:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


if __name__ == "__main__":
    input_data = []
    number_of_words = 10
    try:
        input_data = load_data(sys.argv[1])
    except FileNotFoundError:
        print("File {} not found".format(sys.argv[1]))
        sys.exit(0)
    except IndexError:
        print("Please, put a file name as a parameter.\n"
              "For example: 'python pprint_json.py in.json' ")
        sys.exit(0)

    dictionary = get_most_frequent_words(input_data, number_of_words)
    print(number_of_words, "of the most frequent words")
    for word in dictionary:
        print(word[0], " : ", word[1])

