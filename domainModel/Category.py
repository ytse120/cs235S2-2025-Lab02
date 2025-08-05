class Category:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__recipes = []

    def __str__(self):
        return "<Category " + str(self.__id) + ": " + self.__name + ">"

    def __len__(self):
        return len(self.__recipes)

    def print_recipe(self):
        print("Category " + self.__name + " has the following associated recipes: " + str([str(r) for r in self.__recipes]))

    def add_recipe(self, recipe):
        if recipe not in self.__recipes:
            self.__recipes.append(recipe)
            return True
        return False

    def remove_recipe(self, recipe):
        if recipe in self.__recipes:
            self.__recipes.remove(recipe)
            return True
        return False