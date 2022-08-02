# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036


class Edge(object):
    __symbol = None
    __destinyNode = None

    def __init__(self, symbol: str, destinyNode):
        self.__symbol = symbol
        self.__destinyNode = destinyNode

    def getSymbol(self):
        return self.__symbol

    def getDestinyNode(self):
        return self.__destinyNode
