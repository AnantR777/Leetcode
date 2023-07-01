def romanToInt(self, s: str) -> int:
        dictionary = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        sum = 0
        for i in range(len(s)):
            sum += dictionary[s[i]]
            if i != len(s) - 1:
                if s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                    sum -= 200
                elif s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                    sum -= 20
                elif s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                    sum -= 2
        return sum
