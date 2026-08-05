#Her er det alle funksjoner er lagret for å bli importerte til main.py


def get_book_text(path_to_book: str) -> str:
    with open(path_to_book) as f:
        book_content = f.read()
        return book_content

def word_count(book_content: str) -> int:
    return len(book_content.split())


#Hvis du looper over en string så vil den itterere over hver character i stringen 1 om gangen.
#perfekt for charachter_count()
"""
def smal_str_loop_test():
    string = "Dette er en test for å skjekke om man kan loope over strings"
    
    for ch in string:
        print(ch)
"""     
#smal_str_loop_test()

def character_count(book_content: str) -> dict[str, int]:
    character_dictionary = {}
    for word in book_content.lower():
        for character in word:
            if character in character_dictionary:
                character_dictionary[character] += 1
            else:
                character_dictionary[character] = 1
    return character_dictionary 


def sort_on(characters: tuple[str, int]) -> int:
    return characters[1]

def chars_dict_to_sorted_list(character_dictionary: dict[str, int]) -> list[tuple[str, int]]:
    unsorted_list = []
    for character in character_dictionary:
        unsorted_list.append((character, character_dictionary[character]))
    return sorted(unsorted_list, reverse=True, key=sort_on)




