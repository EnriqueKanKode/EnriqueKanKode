import sys
from stats import word_count, get_book_text, character_count, chars_dict_to_sorted_list

def print_report(book_path: str, word_count: int, sorted_list: list[(str, int)]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for _tuple in sorted_list:
        if _tuple[0].isalpha():
            print(f"{_tuple[0]}: {_tuple[1]}")
    print("============= END ===============")
    

def main():
    if len(sys.argv) == 2:
        pass
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_content = get_book_text(path)
    print_report(path, word_count(book_content),chars_dict_to_sorted_list(character_count(book_content)))
    
    
    #print(f"Found {word_count(book_content)} total words")
    #print(chars_dict_to_sorted_list(character_count(book_content)))


    
main()
    