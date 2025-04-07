import sys

from stats import get_number_words, get_letter_frequency, get_letter_list, print_letter_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def run_bookbot():

    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_array = get_number_words(book_text)
    num_words = len(word_array)
    letter_frequency_dict = get_letter_frequency(book_text)
    letter_frequency_list = get_letter_list(letter_frequency_dict)

    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {num_words} total words\n--------- Character Count -------")
    print_letter_list(letter_frequency_list)
    print("============= END ===============")

run_bookbot()
