def count_words(book_text):
    words_of_text = book_text.split()
    num_words = len(words_of_text)
    return num_words


def count_chars(book_text):
    dict_of_chars = {}

    for word in book_text:
        for char in word:
            lower_char = char.lower()
            if lower_char not in dict_of_chars:
                dict_of_chars.update({lower_char: 1})
            else:
                dict_of_chars[lower_char] += 1

    return dict_of_chars


def sorted_dict(char_dict):
    new_list = list(char_dict.items())

    new_list.sort(reverse=True, key=lambda item: item[1])
    return new_list
