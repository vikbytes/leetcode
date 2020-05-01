def longestCommonPrefix(strs):
    if(len(strs) == 0):
        return ""
    numberOfStrings = len(strs)
    sortedList = sorted(strs,key=len)
    shortestWord = sortedList[0]
    common = ""
    for x in range(len(shortestWord)):
        allCharsMatched = True
        currentChar = strs[0][x]
        if(allCharsMatched == True):
            for y in range(1,numberOfStrings):
                if strs[y][x] == currentChar:
                    continue
                else:
                    allCharsMatched = False
                    break
        if(allCharsMatched == True):
            common += currentChar
        else:
            break

    return common