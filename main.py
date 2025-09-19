import sys
from stats import (
    get_num_chars,
    get_num_words,
    sort_chars,
)

def main():
    # set the path to your book here
    book_path = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    # asign text variable to contents of book
    text = get_book_text(book_path)
    # asign num_words to number of words in text
    num_words = get_num_words(text)
    # asign chars to number of characters in text
    chars = get_num_chars(text)
    # asign sorted_chars to sorted characters in chars (using sort_chars function)
    sorted_chars = sort_chars(chars)
    print_report(book_path, num_words, sorted_chars)


def get_book_text(path_to_file: str):
    # open the file and return its contents
    with open(path_to_file) as f:
        return f.read()


def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book: {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # for each character in sorted_chars, if character is alphabetic, print character and number of occurrences
    for c in sorted_chars:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")
    print("============= END ===============")


main()
