def plusOne(digits):
    carry = True
    x = len(digits)-1
    while(x > 0):
            if carry == True:
                digits[x] += 1
                if digits[x] == 10:
                    digits[x] = 0
                    carry = True
                else:
                    carry = False
                x -= 1
            else:
                break
    if digits[0] == 9 and carry == True:
        digits[0] = 0
        digits.insert(0, 1)
    elif carry == True:
        digits[0] += 1
    return digits


input = [9,8,7]

print(plusOne(input))
