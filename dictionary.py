
class Dictionary:
    def __init__(self, dizionario):
        self.dizionario=dizionario
        pass

    def loadDictionary(self,path):
        file = open(path, "r")
        f = file.readlines()
        for i in range(0, len(f)):
            parola = f[i].strip()
            self.dizionario.append(parola)

        return self.dizionario

    def printAll(self):
        for parola in self.dizionario:
            print(parola)

    @property
    def ritorna_dizionario(self):
        return self.dizionario


