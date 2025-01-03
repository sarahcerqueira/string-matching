from app.stringMatchingTemplate import StringMatchingAlgorithmTemplate

class  KnuthMorrisPratt (StringMatchingAlgorithmTemplate):
    
    def hasPattern(text:str, pattern: str) -> bool:
        if pattern == "":
            return True
        
        table = KnuthMorrisPratt.__createTable(pattern)
        sizeText = len(text)
        sizePattern = len(pattern)
        indexPattern = 0
        indexText = 0

        while indexText < sizeText:
            while indexPattern > 0 and pattern[indexPattern] != text[indexText]:
                indexPattern = table[indexPattern - 1]

            if text[indexText] == pattern[indexPattern]:
                if indexPattern == sizePattern - 1:
                    return True
                indexPattern += 1

            indexText += 1
        return False

    @staticmethod
    def __createTable(pattern:str)->list:
        i = 0
        j = 1
        size = len(pattern)
        table = [0] * size

        while j < size:
            if pattern[i] == pattern[j]:
                table[j] = i + 1
                i += 1
                j += 1

            elif i == 0:
                table[j] = 0
                j += 1

            else:
                i = table[i - 1]

        return table