def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    x = len(s)
    if x%2==1:
        i=x//2
        return  s[i]
    if x%2==0:
        return s[(x)//2-1:(x)//2+1]

print(main('absgdsde'))