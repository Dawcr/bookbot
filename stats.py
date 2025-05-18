from string import ascii_lowercase


def count_words(book_content: str) -> int:
    """
    return the number of words contained in book_content, split by space

    :param book_content: the input string to count the words for
    :return: an integer representing the amount of words contained in the string book_content
    """
    return len(book_content.split())


def count_characters(book_content: str) -> dict[str, int]:
    """
    return the number of times each alphabetical character appears in book_content, not case sensitive

    :param book_content: the input string to count the characters for
    :return: a lowercase dictionary containing the amount of times each character appears in the string book_content
    """
    character_dict = dict.fromkeys(ascii_lowercase, 0) # create a dictionary of characters from ascii so it's ordered

    for c in book_content.lower():
        if c not in character_dict: # if the character is not a letter of the alphabet ignore it
            continue
        character_dict[c] += 1
    return character_dict