class Categoru:
    def __init__(self, name):
        self.__id = "TBD"
        self.__name = name
        self.__recipes = []

    def __str__(self):
        return "<Category " + str(self.__id) + ": " + self.__name + ">"

