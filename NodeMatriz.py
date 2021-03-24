# class to store lable and weight values in MatrizEsparsa
class NodeMatriz:

    # class contructor
    def __init__(self, label, peso):
        self.label = label
        self.peso = peso

    # function that returns the lable value
    def getLabel(self):
        return self.label

    # function that returns the weight value
    def getPeso(self):
        return self.peso

    # function that returns a tuple with both values
    def content(self):
        return (self.getLabel(), self.getPeso())