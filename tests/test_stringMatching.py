import unittest
from app.stringMatchingTemplate import StringMatchingAlgorithmTemplate
from app.stringMatchingNaive import StringMatchingNaive
from app.kmp import KnuthMorrisPratt
from app.bmh import BoyerMooreHorspool

class TestStringMatching(unittest.TestCase):
    __TEXTO = "Vestidos de farrapos, sujos, semiesfomeados, agressivos, soltando palavrões e fumando pontas de cigarro, eram, em verdade, os donos da cidade, os que a conheciam totalmente, os que totalmente a amavam, os seus poetas. (Jorge Amado, Capitães da Areia)"

    def test_naive(self):
        self.__stringMatchingTest(StringMatchingNaive)

    def test_bmh(self):
        self.__stringMatchingTest(BoyerMooreHorspool)

    def test_kmp(self):
        self.__stringMatchingTest(KnuthMorrisPratt)

    def __stringMatchingTest(self, algorithmClass:StringMatchingAlgorithmTemplate):
        self.__stringMatchingStart(algorithmClass)
        self.__stringMatchingEnd(algorithmClass)
        self.__stringMatchingMiddle(algorithmClass)
        self.__noStringMathcing(algorithmClass)

    def __stringMatchingStart(self, algorithmClass:StringMatchingAlgorithmTemplate):
        self.assertTrue(algorithmClass.hasPattern(self.__TEXTO,"Vestidos de farrapos" ))

    def __stringMatchingEnd(self, algorithmClass:StringMatchingAlgorithmTemplate):
        self.assertTrue(algorithmClass.hasPattern(self.__TEXTO,"da Areia)" ))

    def __stringMatchingMiddle(self, algorithmClass:StringMatchingAlgorithmTemplate):
        self.assertTrue(algorithmClass.hasPattern(self.__TEXTO, " agressivos, soltando palavrões"))

    def __noStringMathcing(self, algorithmClass:StringMatchingAlgorithmTemplate):
        self.assertFalse(algorithmClass.hasPattern(self.__TEXTO, "soltando balões"))
