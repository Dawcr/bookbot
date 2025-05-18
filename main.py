import sys

from stats import count_characters, count_words

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1] # relative path to the book
    
    book_contents = get_book_contents(path_to_file) 
    num_words = count_words(book_contents)  # how many words are present in the book
    char_dict = count_characters(book_contents)    # how many times each character appears in the book, not case sensitive(all lowercase)
    print_book_report(path_to_file, num_words, char_dict) # print the book report to terminal

def get_book_contents(path: str) -> str:
    """
    open a file and return its contents
    
    :param path: the path to the file
    :return: the contents of the file
    """
    with open(path) as f:
        return f.read()

def print_book_report(path_to_file: str, words_count: int, character_dict: dict) -> None:
    """
    print the report on how many times each alphabetical character appears in the book to terminal, ordered descendingly by number of appearances 
    
    :param book_name: the name of the book
    :param words_count: the number of words in the book
    :param character_dict: a dictionary containing all alphabetical characters that appear in the book and the amount of times they appear
    """
    book_name = path_to_file.split('/')[-1] # get the name of the book from path
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words" if words_count > 1 
          else "Found 1 word in total" if words_count == 1 
          else "No words found in the document")
    print("--------- Character Count -------")
    for char, amount in sorted(character_dict.items(), key = lambda x: x[1], reverse = True):
        print(f"{char}: {amount}")
    print("============= END ===============")
        
main()