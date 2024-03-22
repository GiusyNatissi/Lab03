import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        campi=txtIn.strip().split()
        print("Campi:",campi)
        parole=[]
        for parola in campi:
            parola.lower()
            parola=replaceChars(parola)
            parole.append(parola)
        print("Parole:", parole)
        m=md.MultiDictionary()
        m.searchWord(parole, language)
        m.searchWordLinear(parole, language)
        m.searchWordDicothomic(parole, language)
        pass

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
        chars="\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            text = text.replace(c, "")
        return text
