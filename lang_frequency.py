import sys
import re
import timeit

def load_data(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def get_words(text):
    dictionary = {}
    for line in text:
        words = re.findall("\w+", line)
        dictionary = add_to_dict(words, dictionary)
    return dictionary


def add_to_dict(input_words, dictionary):
    for word in input_words:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


def print_most_frequent_words(dictionary, num):
    i = 0
    print(num, " most frequent words: ")
    for word_in_dict in sorted(dictionary.items(),
                               key=lambda x: x[1],
                               reverse=True):
        print(word_in_dict[0], " : ", word_in_dict[1])
        i += 1
        if i == num:
            break


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
    dictionary = get_words(input_data)
    print_most_frequent_words(dictionary, number_of_words)
