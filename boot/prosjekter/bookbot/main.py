import sys
from stats import wordcount, char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return(file_content)
    
def sort_on(items):
    return items["num"]

def formating_report(filepath , wordcount: int, char_count : list):
    print("="*8," BOOKBOT ","="*8, "\n")
    print(f"Analyszing book found at {filepath} ...\n")
    print ("-"*11, " Word Count ", "-"*11, "\n")
    print(f"Found {wordcount} total words \n")
    print ("-"*9, " Character Count ", "-"*9, "\n")
    for char in char_count:
        print(f"{char["name"]}: {char["num"]}" )
    print ("="*13, " END ", "="*13, "\n")
    
    
    
def main():
    #print(sys.argv)
    filepath = "books/frankenstein.txt"
    book = get_book_text(filepath)
    formating_report(filepath, wordcount(book),char_count(book))

main()




