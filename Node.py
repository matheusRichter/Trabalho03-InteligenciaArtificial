class Node:
    __nome:str = None # variable that stores Node name

    # class constructor
    def __init__(self, nome):
        self.__nome = nome

    # function that returns Node name
    def getNome(self):
        return self.__nome