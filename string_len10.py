def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """

    
    if s==s[::-1]:
        return True
    else:
        return False

    # x = len(s)
    # y = str(x[:1])
    # z = str(x-2)
    # if y==z:
    #     return True
    # else:
    #     return False

print(main('abb'))