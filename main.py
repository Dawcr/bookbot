from string import ascii_lowercase

def main():
    path_to_file = "books/frankenstein.txt" # relative path to the book
    book_name = path_to_file.split('/')[-1] # get the name of the book from path
    
    book_contents = get_book_contents(path_to_file) 
    num_words = count_words(book_contents)  # how many words are present in the book
    char_dict = count_characters(book_contents)    # how many times each character appears in the book, not case sensitive(all lowercase)
    print_book_report(book_name, num_words, char_dict) # print the book report to terminal

def get_book_contents(path):
    """
    open a file and return its contents
    
    :param path: the path to the file
    :return: the contents of the file
    """
    with open(path) as f:
        return f.read()

def count_words(str):
    """
    return the number of words contained in str, split by space
    
    :param str: the input string to count the words for
    :return: an integer representing the amount of words contained in the string
    """
    return len(str.split())

def count_characters(str):
    """
    return the number of times each alphabetical character appears in str, not case sensitive
    
    :param str: the input string to count the characters for
    :return: a lowercase dictionary containing the amount of times each character appears in the string
    """
    character_dict = dict.fromkeys(ascii_lowercase, 0) # create a dictionary of characters from ascii so it's ordered
    
    for c in str.lower():
        if c not in character_dict: # if the character is not a letter of the alphabet ignore it
            continue
        character_dict[c] += 1
    return character_dict

def print_book_report(book_name, words_count, character_dict):
    """
    print the book report to terminal
    
    :param book_name: the name of the book
    :param words_count: the number of words in the book
    :param character_dict: a dictionary containing all alphabetical characters that appear in the book and the amount of times they appear
    """
    print(f"--- Begin report of {book_name} ---")
    print(f"{words_count} words found in the document" if words_count > 1 
          else "1 word found in the document" if words_count == 1 
          else "no words found in the document")
    print('\n') # print 2 newlines
    for char in character_dict:
        print(f"The character '{char}' was found {character_dict[char]} times" if character_dict[char] > 1
              else f"The character '{char}' was found {character_dict[char]} time")
        
main()