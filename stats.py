def get_number_words(book_text):
    word_array = book_text.split()
    return word_array

def get_letter_frequency(booktext):
    
    # cleans the raw text
    lowered_booktext = booktext.lower()

    # sets up the dictionary
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_dict = {}
    for letter in alphabet:
        letter_dict[letter] = 0
    
    # iterates through cleaned text and increments each letter in dictionary
    for letter in lowered_booktext:
        if letter in letter_dict:
            letter_dict[letter] += 1
    
    return letter_dict

def sort_on(dict):
    return dict["num"]

def get_letter_list(letter_dict):
    list_dictionaries = []

    for element in letter_dict:
        current_dict = {"letter" : element, "num" : letter_dict[element]}
        list_dictionaries.append(current_dict)
    list_dictionaries.sort(reverse=True, key=sort_on)

    return list_dictionaries

def print_letter_list(letter_list):
    for element in letter_list:
        print(f"{element["letter"]}: {element["num"]}")