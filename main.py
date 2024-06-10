def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path) 
    lowered_text = book_text.lower()
    wordcount = get_wordcount(book_text)
    character_count = get_char_count(lowered_text)
    #print(f"{lowered_text}")
    print(f"{wordcount} words found in the document")
    print(f"{character_count}")

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
    
main()