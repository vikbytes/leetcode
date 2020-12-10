class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for x in range(1, n+1):
            if x < 3:
                l.append(str(x))
            else:
                if x % 3 == 0:
                    if x % 5 == 0:
                        l.append('FizzBuzz')
                    else:
                        l.append('Fizz')
                elif x % 5 == 0:
                    l.append('Buzz')
                else:
                    l.append(str(x))
        return l