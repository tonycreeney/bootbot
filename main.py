def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    frankenstein_path = "books/frankenstein.txt"
    text = get_book_text(frankenstein_path)
    print(text)


main()

