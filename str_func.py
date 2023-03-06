def get_capital_letters():
    """
    Returns the input phrase with all letters to be capital
    """
    user_input = input()
    return user_input.upper()


print(get_capital_letters())


def get_first_letters_capital():
    """
    Returns the input phrase with first letters of each word becoming capital
    """
    user_input = input()
    return user_input.title()


print(get_first_letters_capital())
