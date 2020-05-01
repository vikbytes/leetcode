def isValid(s):
    if len(s) == 0:
        return True
    openingBrackets = ['(', '{', '[']
    closingBrackets = [')', '}', ']']
    openBrackets = []
    for x in s:
        if (x in openingBrackets):
            openBrackets.append(x)
        elif (x in closingBrackets):
            if len(openBrackets) == 0:
                return False
            elif x == closingBrackets[0] and openBrackets[-1] == openingBrackets[0]:
                openBrackets.pop()
            elif x == closingBrackets[1] and openBrackets[-1] == openingBrackets[1]:
                openBrackets.pop()
            elif x == closingBrackets[2] and openBrackets[-1] == openingBrackets[2]:
                openBrackets.pop()
            else:
                return False
    if len(openBrackets) != 0:
        return False
    else:
        return True