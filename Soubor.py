import os

class Soubor:
    def __init__(self, path:str):
        self.path = path

    def readFile(self):
        if not os.path.exists(self.path):
            return None

        with open(self.path) as f:
            content = f.read()
        return content

    def readFile2(self):
        try:
            with open(self.path) as f:
                content = f.read()
            return content
        except FileNotFoundError:
            return None

    def printFile(self):
        content = self.readFile2()
        if not content:
            print(f"Soubor s nazvem {self.path} neexistuje")
            return
        print(content)

s = Soubor("text1")
s.printFile()


