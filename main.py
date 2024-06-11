def main():
    
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path) 
    lowered_text = book_text.lower()
    wordcount = get_wordcount(book_text)
    character_count_dict = get_char_count(lowered_text)
    alphabet_count_dict = filter_alpha(character_count_dict)
    alpha_count_list = make_list(alphabet_count_dict)
    
    
    print_report(wordcount, book_path, alpha_count_list)


def get_char_count(text):
    counter = {}
    for each in text:
        if each in counter:
            counter[each] += 1
        else:
            counter[each] = 1
    return counter

def get_wordcount(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

def filter_alpha(dict):
    all_keys = dict.keys()
    alpha_keys = []
    alpha_dict = {}
    for each in all_keys: 
        if each.isalpha():
            alpha_keys.append(each)
    for each in alpha_keys:
        alpha_dict[each] = dict[each]
    return alpha_dict
def make_list(dict):
    keys = dict.keys()
    
    list = []

    for each in keys:
        char_dict = {}
        char_dict["char"] = each
        char_dict["count"] = dict[each]
        list.append(char_dict)
        
    
    return list
def sort_on(dict):
    return dict["count"]


def print_report(wordcount, book, character_count):
    character_count.sort(reverse=True, key=sort_on)
    list_of_counts = []

    print(f"--- Begin Report of {book} ---")
    print(f"{wordcount} words found in the document")
    
    for each in character_count:
        char = each["char"]
        count = each["count"]
        print(f"The '{char}' character was found '{count}' times")
    
    print("--- End Report---")

main()