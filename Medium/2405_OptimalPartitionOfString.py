class Solution:
    def partitionString(self, s: str) -> int:
        substrings = []
        for character in s:
            if substrings == []:
                substrings.append(character)
            else:
                if character not in substrings[-1]:
                    substrings[-1] += character
                else:
                    substrings.append(character)
        return len(substrings)
