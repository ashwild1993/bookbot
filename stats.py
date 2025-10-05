def number_of_words(book_text):
    words = book_text.split()
    return len(words)

def num_times(book_text):
    lowercase_string = book_text.lower()
    letter_dict = {}
    for letter in lowercase_string:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] +=1
    return letter_dict

def sorted_dictionary(letter_dict):
    dict_list = []
    for letter, number in letter_dict.items():
        if letter.isalpha() == False:
            continue
        dict_list.append({"char": letter, "num": number})
        def by_num(d):
            return d["num"]
        dict_list.sort(key=by_num, reverse =True)
    return dict_list
 