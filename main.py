def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_characters(text)

    sorted_dict = sort_dictionary(chars_dict)

    print_report(book_path,num_words,sorted_dict)
    


def get_book_text(path):
    try:
        with open (path) as f:
            return f.read()
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"Error Encountered {e}")

def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    
    chars = {}
    for c in text:
        lowered_char = c.lower()
        if lowered_char in chars:
            chars[lowered_char] += 1
        else:
            chars[lowered_char] = 1
    return chars

def sort_dictionary(chars_dict):
    char_tuple = (chars_dict.items())
    
    sorted_char_tuple = sorted(char_tuple, key=lambda item: item[1], reverse=True)

    return sorted_char_tuple


def print_report(book_path,num_words,sorted_chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for char, count in sorted_chars_dict:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


main()