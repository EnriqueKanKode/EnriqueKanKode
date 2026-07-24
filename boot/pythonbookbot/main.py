

def get_book_tekst(filepath : path) --> str:
    with open(filepath) as f:
        file_content = f.read
        print(file_content)
        
get_book_tekst("books /frankeinstein.txt")

