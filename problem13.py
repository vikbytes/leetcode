def romanToInt(s):
    result = 0
    lengthOfNumber = len(s)
    x = 0
    while(x < lengthOfNumber):
        if s[x] == 'I':
            if x+1 == lengthOfNumber:
                result += 1
                x += 1
            elif(s[x+1] == 'V'):
                result += 4
                x += 2
            elif(s[x+1] == 'X'):
                result += 9
                x += 2
            else:
                result += 1
                x += 1
        elif s[x] == 'X':
            if x+1 == lengthOfNumber:
                result += 10
                x += 1
            elif(s[x+1] == 'L'):
                result += 40
                x += 2
            elif(s[x+1] == 'C'):
                result += 90
                x += 2
            else:
                result += 10
                x += 1
        elif s[x] == 'C':
            if x+1 == lengthOfNumber:
                result += 100
                x += 1
            elif(s[x+1] == 'D'):
                result += 400
                x += 2
            elif(s[x+1] == 'M'):
                result += 900
                x += 2
            else:
                result += 100
                x += 1
        elif s[x] == 'V':
            result += 5
            x += 1
        elif s[x] == 'L':
            result += 50
            x += 1
        elif s[x] == 'D':
            result += 500
            x += 1
        elif s[x] == 'M':
            result += 1000
            x +=1
    return result

print(romanToInt("III"))