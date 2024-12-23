""" Is in

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _at least one_ of the lists.

"""
def is_in(text, list1, list2):
    """
    The function takes in a string and two lists of strings. 
    It will return true if the item is in _at least one_ of the lists.

    Parameters:
        text (str): The input string we want to check.
        list1 (list): First list to check for the string.
        list2 (list): Second list to check for the string.

    Returns:
        (bool): True if the string is in at least one of the lists, False otherwise.

    Raises:
        AssertionError: If the first argument is not a string.
        AssertionError: If the second argument is not a list.
        AssertionError: If the third argument is not a list.

    Examples:
        >>> is_in("Nada", ["Nada", "Aree"], ["bees", "Nada"])
        True      
        >>> is_in("book", ["pen", "book"], ["bees", "Nada"])
        True      
        >>> is_in("apple", ["Nada", "Aree"], ["bees", "Nada"])
        False
    """
    assert isinstance(text, str), "First argument must be a string."
    assert isinstance(list1, list), "Second argument must be a list."
    assert isinstance(list2, list), "Third argument must be a list."

    # Check if text is in at least one of the lists
    return text in list1 or text in list2
