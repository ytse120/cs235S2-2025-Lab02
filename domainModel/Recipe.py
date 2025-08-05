import datetime

class Recipe:
    def __init__(self, id, name, author, date=datetime.datetime.now().replace(microsecond=0), ingredients=[]):
        self.__id = id
        self._name = name
        self._author = author
        self._ingredients = ingredients
        self._description = ""
        self._instructions = []
        self._cook_time = "TBD"
        self._category = []
        self._createdDate = date

    def __str__(self):
        return "<Recipe " + self._name + " with id: " + str(self.__id) + " was created by " + self._author + " on " + str(self._createdDate) + ">"

    def add_description(self, description):
        self._description = description

    def add_category(self, category):
        if category not in self._category:
            self._category.append(category)
            return True
        return False

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def description(self):
        return self._description

    @property
    def createdDate(self):
        return self._createdDate
