from stats import word_count, get_book_text, character_count, chars_dict_to_sorted_list

def pirnt_report(book_path: str, word_count: )

def main():
    path = "books/frankenstein.txt"
    book_content = get_book_text(path)
    
    print(f"Found {word_count(book_content)} total words")
    print(chars_dict_to_sorted_list(character_count(book_content)))


    
main()
    