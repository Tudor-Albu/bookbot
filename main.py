letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

def get_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_number_of_words(text):
    return len(text.split())


def get_charaters_dict(text):
    letter_dict = {}

    text = text.lower()
    for letter in text:
        if letter in letters:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1

    return letter_dict


def print_report(number_of_words, dict_charaters):
    print(number_of_words, "words found in the document", "\n", sep=" ")

    sorted_characters = sorted(dict_charaters.items(), key=lambda item : item[1], reverse=True)

    for character in sorted_characters:
        print(f"The '{character[0]}' character was found {character[1]} times")

    print("--- End report ---")
    

def main():
    print("--- Begin report of books/frankenstein.txt --")

    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    number_of_words = get_number_of_words(text)
    charaters_dict = get_charaters_dict(text)

    print_report(number_of_words, charaters_dict)


main()