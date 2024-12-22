def repeat_character(text, char, repetition):
    """
    The function returns a string with each occurrence of the character repeated n times.

    Parameters:
        text (str): The input text.
        char (str): The character to be repeated.
        repetition (int): The number of times to repeat the character.

    Returns:
        str: The modified string with the character repeated.

    Raises:
        AssertionError: If the inputs are invalid (e.g., char is not a single character).

    Examples:
        >>> repeat_character("Omnia", "m", 7)
        "Ommmmmmmnia"
        
        >>> repeat_character("Nada", "a", 4)
        "Naaaada"
    """
    assert isinstance(text, str), "First argument must be a string."
    assert isinstance(char, str) and len(char) == 1, "Second argument must be a single character."
    assert isinstance(repetition, int) and repetition >= 0, "Third argument must be a non-negative integer."
    repeated_test=""
    for item in text :
        if item != char :
            repeated_test += item
        else:
            repeated_test  += item * repetition
    return repeated_test             
