from app.stringMatchingTemplate import StringMatchingAlgorithmTemplate

class  BoyerMooreHorspool (StringMatchingAlgorithmTemplate):

    def hasPattern(text:str, pattern: str) -> bool:
        if pattern == "":
            return True

        bmhTable = BoyerMooreHorspool.__createBmhTable(pattern)
        i = len(pattern) - 1
        j = i
        sizeS = len(text)

        while i < sizeS:
            k = i
            while text[k] == pattern[j] and j >= 0:
                k -= 1
                j -= 1

            if j < 0:
                return True

            if text[i] in bmhTable:
                i = i + bmhTable[text[i]]
            else:
                i = i + bmhTable['*']
            j = len(pattern) - 1

        return False

    @staticmethod
    def __createBmhTable(pattern:str)->dict:
        bmhTable = {}
        size = len(pattern)
        patternIndex = 0

        while patternIndex < size - 1:
            bmhTable[pattern[patternIndex]] = size - patternIndex - 1
            patternIndex += 1

        bmhTable['*'] = size

        return bmhTable
