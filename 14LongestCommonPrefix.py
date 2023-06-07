def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return prefix

        minwordlength = len(strs[0])
        i = 0
        while i < len(strs) - 1:
            if len(strs[i]) < len(strs[i+1]):
                minwordlength = len(strs[i])
            i = i + 1

        letterindex = 0
        while letterindex < minwordlength:
            wordindex = 0
            while wordindex < len(strs) - 1:
                if len(strs[wordindex]) <= letterindex or len(strs[wordindex + 1]) <= letterindex:
                    break
                if strs[wordindex][letterindex] == strs[wordindex + 1][letterindex]:
                    wordindex = wordindex + 1
                else:
                    break
            if wordindex == len(strs) - 1:
                prefix += strs[wordindex][letterindex]
            else:
                break

            letterindex = letterindex + 1

        return prefix
