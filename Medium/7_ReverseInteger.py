class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            string = str(-x)
            string.lstrip("0")
            if int("-" + string[::-1]) > -2**31 and int("-" + string[::-1]) < 2**31 - 1:
                return int("-" + string[::-1])
            else:
                return 0

        if x >= 0:
            string = str(x)
            string.lstrip("0")
            if int(string[::-1]) > -2**31 and int(string[::-1]) < 2**31 - 1:
                return int(string[::-1])
            else:
                return 0
