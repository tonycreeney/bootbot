import sys

from stats import count_chars, count_words, sorted_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def print_list(list):
    for item in list:
        print(f"{item[0]}: {item[1]}")


def title_print(book_path):
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_path}...")


def word_count(num_words):
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")


def character_count(list):
    print("--------- Character Count -------")
    print_list(list)


def end_print():
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    list_of_chars = count_chars(text)
    num_words = count_words(text)
    sorted_list = sorted_dict(list_of_chars)

    for char in sorted_list[:]:
        if not char[0].isalpha():
            sorted_list.remove(char)

    title_print(book_path)
    word_count(num_words)
    character_count(sorted_list)
    end_print()


main()
