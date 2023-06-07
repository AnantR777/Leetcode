def isValid(self, s: str) -> bool:
        dicty = {'(':')', '{':'}','[':']'}
        listofbrackets = []

        for bracket in s:
            if bracket in dicty:
                listofbrackets.append(bracket) # if opening bracket (key in dictionary), add to list
            else: 
                if len(listofbrackets) and dicty[listofbrackets[-1]] == bracket: # checks list not empty and closing bracket matches that at top of stack
                    del listofbrackets[-1]
                else:
                    return False

        return not listofbrackets #if empty will return true
