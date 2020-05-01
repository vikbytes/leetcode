class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        if y[0] == '-':
            y1 = y[0]
            y2 = y[1::]
            y2 = y2[::-1]
            y = y1+y2
        else:
            y = y[::-1]
        y = int(y)
        if y < -2**31 or y > 2**31-1:
            return 0
        return int(y)