def isPalindrome(x):
    y = str(x)
    if y[0] == '-':
        return False
    else:
        y = y[::-1]
        y = int(y)
        if y == x:
            return True
        else:
            return False