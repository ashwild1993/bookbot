import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

from stats import number_of_words

from stats import num_times

from stats import sorted_dictionary

def main():
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words = number_of_words(book_text)
    letter_count = num_times(book_text)
    dict_list = sorted_dictionary(letter_count)
    
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for pair in dict_list:
        letter = pair["char"]
        amount = pair["num"]
        print(f"{letter}: {amount}")

    print(f"============= END ===============")


main()