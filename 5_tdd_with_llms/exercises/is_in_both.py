""" Is in Both

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _both_ of the lists.

"""
def is_in_both(text, list1, list2):
    """
    The function takes in a string and two lists of strings. 
    It will return true if the item is in _both_ of the lists.


    Parameters:
        text (str): The input text we want to check if its in two list .
        list1 (list): check if text on it
        list2 (list): check if text on it

    Returns:
        (list)True if its in both false if not 

    Raises:
        AssertionError: If the first argument is not str
        AssertionError: If the second  argument is not list
        AssertionError: If the third  argument is not list



    Examples:
        >>> is_in_both("Nada" , ["Nada" , "Aree" ] ,["bees" , "Nada"])
        True      
        >>> is_in_both("book" , ["pen" , "book" ] ,["bees" , "Nada"])
        False      

    """
    assert isinstance(text, str), "First argument must be a string."
    assert isinstance(list1, list)
    assert isinstance(list2, list) 
    if text in list1 and text in list2:
        return True
    return False         
