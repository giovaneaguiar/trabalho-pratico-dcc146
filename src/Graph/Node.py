# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

from src.Graph.Edge import Edge


class Node(object):
    __transitions = []
    __name = None

    def __init__(self, name: str):
        self.__name = name
        self.__transitions = []

    def addTransition(self, symbol: str, node):
        self.__transitions.append(Edge(symbol, node))

    def getName(self):
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getTransitions(self):
        return self.__transitions

    def getTransition(self, symbol: str):
        for transition in self.__transitions:
            if transition.getSymbol() == symbol:
                return transition
        return None

    def removeTransition(self, transition):
        self.__transitions.remove(transition)

    def checkTransitions(self, symbol: str):

        # Verifica se existe uma transicao que consome o simbolo,
        # se sim retorna o no destino,
        # se nao retorna False

        for transition in self.getTransitions():
            if transition.getSymbol() == symbol:
                return transition.getDestinyNode()

        return False
