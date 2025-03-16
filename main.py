from sys import argv, exit
from stats import get_num_words, get_char_counts, flatten_and_sort_dict
from pprint import pprint


def get_book_text(filepath):
    with open(filepath) as file:
        result = file.read()

    return result


def main(argv):

    if (len(argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    filepath = argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    char_counts = flatten_and_sort_dict(get_char_counts(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")

    print("-------- Character Count --------")
    for kv in char_counts:
        char = kv.get('char')
        if char.isalpha():
            print(f"{char}: {kv.get('count')}")

    print("============ END ============")


if __name__ == '__main__':
    main(argv)
