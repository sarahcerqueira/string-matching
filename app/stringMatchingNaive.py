from app.stringMatchingTemplate import StringMatchingAlgorithmTemplate

class StringMatchingNaive (StringMatchingAlgorithmTemplate):

    def hasPattern(text:str, pattern: str) -> bool:
        textIndex = 0
        patternIndex = 0

        while textIndex < len(text):
            positionItWasChecking = textIndex
            while patternIndex < len(pattern) and text[textIndex] == pattern[patternIndex]:
                textIndex += 1
                patternIndex += 1

            if patternIndex >= len(pattern):
                return True

            textIndex = positionItWasChecking + 1
            patternIndex = 0

        return False