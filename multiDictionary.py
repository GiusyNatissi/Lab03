import time

import dictionary as d
import richWord as rw
import time


class MultiDictionary:

    def __init__(self):
        self.dict=[]
        pass

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        self.carica_dizionario(language)
        ListarichWord=[]
        t1=time.time()
        for word in words:
            parola = rw.RichWord(word)
            if word in self.dict:
                parola.set_corretta(True)
                ListarichWord.append(parola)
            else:
                parola.set_corretta(False)
                ListarichWord.append(parola)
        t2=time.time()
        printMenuFinale("contains", ListarichWord, t2-t1)
        return ListarichWord

    def searchWordLinear(self, words, language):
        self.carica_dizionario(language)
        ListarichWord=[]
        t1=time.time()
        for word in words:
            parola = rw.RichWord(word)
            if self.contiene(word):
                parola.set_corretta(True)
                ListarichWord.append(parola)
            else:
                parola.set_corretta(False)
                ListarichWord.append(parola)
        t2 = time.time()
        printMenuFinale("Linear search", ListarichWord, t2-t1)

    def searchWordDicothomic(self, words, language):
        self.carica_dizionario(language)
        ListarichWord=[]
        t1=time.time()
        for word in words:
            parola = rw.RichWord(word)
            trovata=False
            lista_nuova = self.dict[:] #CREO UNA COPIA DEL DIZIONARIO
            while(trovata==False and len(lista_nuova)>1):
                indice_centrale = len(lista_nuova) // 2
                elemento_centrale = trovaCentrale(lista_nuova)
                if word==elemento_centrale:
                    parola = rw.RichWord(word)
                    parola.set_corretta(True)
                    ListarichWord.append(parola)
                    trovata=True

                elif word>elemento_centrale:
                    lista_nuova = lista_nuova[indice_centrale:]

                elif word<elemento_centrale:
                    lista_nuova = lista_nuova[:indice_centrale]

            if len(lista_nuova)==1:
                if word==lista_nuova[0]:
                    parola.set_corretta(True)
                    ListarichWord.append(parola)
                else:
                    parola.set_corretta(False)
                    ListarichWord.append(parola)
        t2=time.time()
        printMenuFinale("Dicothomic search", ListarichWord, t2-t1)


    def contiene(self, parola):
        for elemento in self.dict:
            if elemento==parola:
                return True
        return False

    def carica_dizionario(self, language):
        dic = d.Dictionary([])
        if language == "italian":
            self.dict = dic.loadDictionary("resources/Italian.txt")
        elif language == "english":
            self.dict = dic.loadDictionary("resources/English.txt")
        elif language == "spanish":
            self.dict = dic.loadDictionary("resources/Spanish.txt")


def printMenuFinale(metodo, ListarichWord, tempo_esecuzione):
    print("-"*30)
    print(f"Using {metodo}")
    for richword in ListarichWord:
        if richword.corretta==False:
            print(richword)
    print(f"Time elapsed {tempo_esecuzione}")


def trovaCentrale(lista):
    indice=len(lista)//2
    return lista[indice]

