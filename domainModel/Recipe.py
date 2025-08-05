class Recipe:
    def __init__(self, name, author):
        self.__id = "TBD"
        self._name = name
        self._author = author
        self._ingredients = []
        self._description = ""
        self._instructions = []
        self._cook_time = "TBD"
        self._category = []
        self._createdDate = "TBD"

    def __str__(self):
        return "<Recipe " + self._name + " with id: " + str(self.__id) + " was created by " + self._author + " on " + self._createdDate + ">"
