def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    wordcount = get_wordcount(book_text)
    print(f"{wordcount} words found in the document")

def get_wordcount(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()
    
main()