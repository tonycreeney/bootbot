from stats import count_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    frankenstein_path = "books/frankenstein.txt"
    text = get_book_text(frankenstein_path)

    num_words = count_words(text)
    print(num_words, "words found in the document")


main()
