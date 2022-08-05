# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

from src.Graph.Node import Node


class Automaton(object):
    __initialStates = []
    __finalStates = []
    __states = []
    __alphabet = []
    __tagName = ''

    __currentState = __initialStates

    def __init__(self):
        self.__initialStates = []
        self.__finalStates = []
        self.__states = []
        self.__alphabet = []
        self.__currentState = self.__initialStates

    def getInitialStates(self):
        return self.__initialStates

    def addInitialState(self, state: Node):
        self.__initialStates.append(state)

    def removeInitalState(self, state: Node):
        if state in self.__initialStates:
            self.__initialStates.remove(state)

    def getFinalStates(self):
        return self.__finalStates

    def addFinalState(self, state: Node):
        self.__finalStates.append(state)

    def removeFinalState(self, state: Node):
        if state in self.__finalStates:
            self.__finalStates.remove(state)

    def addState(self, state):
        self.__states.append(state)

    def removeState(self, state):
        self.__states.remove(state)

    def getStates(self):
        return self.__states

    def getStateByName(self, name: str):
        for state in self.__states:
            if state.getName() == name:
                return state
        return None

    def getTagName(self) -> str:
        return self.__tagName

    def setAlphabet(self, alphabet):
        self.__alphabet = alphabet

    def getAlphabet(self):
        return self.__alphabet

    def setCurrentState(self, state: Node):
        self.__currentState = state

    def setTagName(self, tagName: str):
        self.__tagName = tagName

    def reset(self):
        self.__currentState = self.__initialStates

    # Para cada estado inicial verifica se eh possivel chegar em um estado final
    def analyzeString(self, string: str) -> bool:
        for state in self.getInitialStates():
            nextState = state
            i = 0
            while nextState and i < len(string):
                nextState = nextState.checkTransitions(string[i])
                i = i + 1
                # Caso o proximo No seja um no final e todos os simbolos foram processados, o automato reconhece o texto
                if nextState in self.getFinalStates() and i == len(string):
                    return True

        return False

    # Retorna a definição formal de um automato
    def formalDefinition(self, name: int):

        # Estados inicais
        initialStatesDefinition = ""
        for state in self.getInitialStates():
            initialStatesDefinition = initialStatesDefinition + state.getName() + ","
        initialStatesDefinition = initialStatesDefinition[:-1]  # Tira última vírgula

        # demais estados
        allStates = ""
        for state in self.getStates():
            allStates = allStates + state.getName() + ","
        allStates = allStates[:-1]

        # alfabeto
        alphabet = ""
        for symbol in self.__alphabet:
            alphabet = alphabet + symbol + ","
        alphabet = alphabet[:-1]

        # estados finais
        finalStateDefinition = ""
        for state in self.getFinalStates():
            finalStateDefinition = finalStateDefinition + state.getName() + ","
        finalStateDefinition = finalStateDefinition[:-1]

        definition = f'M{name} = ( { {allStates} }, { {alphabet} }, δ{name} , {initialStatesDefinition}, { {finalStateDefinition} }) '

        return definition

    # Retorna a função de transição do autômato
    def transitionFunc(self, name: int):
        definition = f"δ{name}:\n"
        for state in self.getStates():
            for transition in state.getTransitions():
                definition = definition + state.getName() + ': ' + \
                             transition.getSymbol() + ' -> ' + \
                             transition.getDestinyNode().getName() + '\n'
            if len(state.getTransitions()) == 0:
                definition = definition + state.getName() + ": λ\n"

        return definition
