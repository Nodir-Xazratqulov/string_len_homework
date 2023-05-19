def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    if len(s1)>len(s2) and len(s1)<len(s3) or len(s1)<len(s2) and len(s1)>len(s3):
        return '['+s1+']'
    else:
        if len(s2)>len(s1) and len(s2)<len(s3) or len(s2)<len(s1) and len(s2)>len(s3):
            return '['+s2+']'
        else:
            if len(s3)>len(s1) and len(s3)<len(s2) or len(s3)<len(s1) and len(s3)>len(s2):
                return '['+s3+']'

print(main('code', 'python', 'codeschool'))