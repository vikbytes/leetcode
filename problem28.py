def strStr(haystack, needle):
    if needle == "" and haystack != "":
        return 0
    elif haystack == "" and needle != "":
        return -1
    elif haystack == "" and needle == "":
        return 0
    else:
        for x in range(len(haystack)):
            if (len(haystack) - x < len(needle)):
                return -1
            if haystack[x] == needle[0]:
                processing = True
                for y in range(1,len(needle)):
                    if haystack[x+y] != needle[y]:
                        processing = False
                if processing == True:
                    return x
        return -1


print(strStr("aaaaa", "bba"))
