# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

from src.Automaton import Automaton
from src.Graph.Node import Node
from src.MessageLogs import MessageLogs


class Converter(object):
    __automatons = []

    def addAutomaton(self, tagName: str, expression: str):
        name = 0
        stack = []
        previousChar = ''
        alphabet = []

        # Percorre a tag e constroi o AFN-Lambda
        for char in expression:
            auxInitialState = None
            auxFinalState = None
            automaton = None
            auxStack1 = None
            auxStack2 = None

            if previousChar == '\\':
                automaton = Automaton()
                auxInitialState = Node('q' + str(name))
                automaton.addInitialState(auxInitialState)
                automaton.addState(auxInitialState)
                name = name + 1
                auxFinalState = Node('q' + str(name))
                name = name + 1
                automaton.addFinalState(auxFinalState)
                automaton.addState(auxFinalState)
                auxInitialState.addTransition(char, auxFinalState)
                stack.append(automaton)
                previousChar = ''
                if char not in alphabet:
                    alphabet.append(char)

            else:
                if char == '.' or char == '+':
                    if len(stack) < 2:
                        MessageLogs.error('Erro ao converter ER para AFD')
                        return False
                    else:
                        if char == '+':
                            auxStack1 = stack.pop()
                            auxStack2 = stack.pop()
                            automaton = Automaton()
                            auxInitialState = Node('q' + str(name))
                            name = name + 1
                            auxFinalState = Node('q' + str(name))
                            name = name + 1
                            auxInitialState.addTransition('λ', auxStack1.getInitialStates()[0])
                            auxInitialState.addTransition('λ', auxStack2.getInitialStates()[0])
                            auxStack1.getFinalStates()[0].addTransition('λ', auxFinalState)
                            auxStack2.getFinalStates()[0].addTransition('λ', auxFinalState)
                            automaton.addInitialState(auxInitialState)
                            automaton.addFinalState(auxFinalState)
                            automaton.addState(auxInitialState)
                            automaton.addState(auxFinalState)
                            for state1 in auxStack1.getStates():
                                automaton.addState(state1)
                            for state2 in auxStack2.getStates():
                                automaton.addState(state2)
                            del auxStack1
                            del auxStack2
                            stack.append(automaton)
                        else:
                            auxStack1 = stack.pop()
                            auxStack2 = stack.pop()
                            auxStack2.getFinalStates()[0].addTransition('λ', auxStack1.getInitialStates()[0])
                            auxStack2.removeFinalState(auxStack2.getFinalStates()[0])
                            auxStack2.addFinalState(auxStack1.getFinalStates()[0])
                            for state in auxStack1.getStates():
                                auxStack2.addState(state)
                            stack.append(auxStack2)

                elif char == '*':
                    if len(stack) < 1:
                        MessageLogs.error('Erro ao converter ER para AFD')
                        return False
                    else:
                        auxStack1 = stack.pop()
                        auxStack1.getFinalStates()[0].addTransition('λ', auxStack1.getInitialStates()[0])
                        auxStack1.removeFinalState(auxStack1.getFinalStates()[0])
                        auxStack1.addFinalState(auxStack1.getInitialStates()[0])
                        stack.append(auxStack1)

                # Se não for nenhum caractere especial, insere normalmente na pilha
                else:
                    # Cria autômato para um caractere
                    if char != '\\':
                        automaton = Automaton()
                        auxInitialState = Node('q' + str(name))
                        automaton.addInitialState(auxInitialState)
                        automaton.addState(auxInitialState)
                        name = name + 1
                        auxFinalState = Node('q' + str(name))
                        name = name + 1
                        automaton.addFinalState(auxFinalState)
                        automaton.addState(auxFinalState)
                        auxInitialState.addTransition(char, auxFinalState)
                        stack.append(automaton)
                        if char not in alphabet:
                            alphabet.append(char)

                previousChar = char

        # Se sobrou apenas um autômato na pilha
        if len(stack) == 1:
            stack[0].setAlphabet(alphabet)
            afn = self.removeLambda(stack[0])
            stack.clear()
            afd = self.generateAFD(afn)
            # self.printAutomaton(afd)
            afd.setTagName(tagName)
            self.__automatons.append(afd)

    # Retorna um autômato específico
    def getAutomaton(self, indice: int):
        if 0 <= indice < len(self.__automatons):
            return self.__automatons[indice]

    # Retorna todos os autômatos na memória
    def getAutomatons(self):
        return self.__automatons

    # Função auxiliar para descobrir quais nós é possível alcançar com transições lambdas a partir de um nó
    def __reachesWithLambda(self, state, reachLambda):
        if state not in reachLambda:
            reachLambda.append(state)
        for transition in state.getTransitions():
            if transition.getSymbol() == 'λ':
                if transition.getDestinyNode() not in reachLambda:
                    reachLambda.append(transition.getDestinyNode())
                    self.__reachesWithLambda(
                        transition.getDestinyNode(), reachLambda)

    # Função auxiliar para remover todas as transições para um nó (usado quando se vai apagar um nó)
    @staticmethod
    def __removeTransitionToState(automaton, target):
        for state in automaton.getStates():
            willBeRemoved = []
            for transition in state.getTransitions():
                if transition.getDestinyNode() == target:
                    willBeRemoved.append(transition)
            for transition in willBeRemoved:
                state.removeTransition(transition)

    # Função para remover transições lambdas, retornando um AFN
    def removeLambda(self, automaton):
        # Set para armazenar os fechos lambdas
        lambdaClosure = {}
        # auxVetor = []

        # Constroi fecho lambda para cada nó
        for state in automaton.getStates():
            auxVetor = []
            self.__reachesWithLambda(state, auxVetor)
            lambdaClosure[state.getName()] = auxVetor

        # Cria o AFN básico com todos os nós do AFN-Lambda anterior
        afn = Automaton()
        for state in automaton.getStates():
            afn.addState(Node(state.getName()))

        afn.setAlphabet(automaton.getAlphabet())

        # Cria todas as transições do AFN com base no AFN-Lambda e nos fechos lambdas
        for state in afn.getStates():
            auxState = automaton.getStateByName(state.getName())
            for auxTransition in auxState.getTransitions():
                if auxTransition.getSymbol() != 'λ':
                    state.addTransition(
                        auxTransition.getSymbol(),
                        afn.getStateByName(auxTransition.getDestinyNode().getName())
                    )
                    for stateLambda in lambdaClosure[auxTransition.getDestinyNode().getName()]:
                        if stateLambda.getName() != auxTransition.getDestinyNode().getName():
                            state.addTransition(auxTransition.getSymbol(), afn.getStateByName(stateLambda.getName()))

        # Insere os nós Finais no novo AFN
        for finalState in automaton.getFinalStates():
            afn.addFinalState(
                afn.getStateByName(finalState.getName()))

        # Insere os nós Iniciais no novo AFN
        for initialState in automaton.getInitialStates():
            for stateLambda in lambdaClosure[initialState.getName()]:
                afn.addInitialState(
                    afn.getStateByName(stateLambda.getName()))

        # remove estados inuteis
        willBeRemoved = []
        for state in afn.getStates():
            if len(state.getTransitions()) == 0 and state not in afn.getFinalStates():
                if state in afn.getInitialStates():
                    afn.removeInitalState(state)
                self.__removeTransitionToState(afn, state)
                willBeRemoved.append(state)

        for state in willBeRemoved:
            afn.removeState(state)

        # Deleta o AFN-Lambda e retorna o AFN
        del automaton
        return afn

    # Função auxiliar que gera a string dos estados para ser utilizado nos sets dos estados
    @staticmethod
    def __generateStringStates(states):
        stringVector = []
        finalString = "{"
        for state in states:
            stringVector.append(state.getName())
        stringVector = sorted(stringVector)
        for str in stringVector:
            finalString += str + ","
        finalString = finalString.rstrip(',')
        finalString += "}"
        return finalString

    # Função auxiliar para gerar os estados, utilizado na conversão do AFN para AFD
    def __generateTemporaryStates(self, temporaryState, states, alphabet):
        stringStates = self.__generateStringStates(states)
        if stringStates not in temporaryState:
            transitions = {}
            for char in alphabet:
                auxTransitions = []
                for state in states:
                    for transition in state.getTransitions():
                        if transition.getSymbol() == char:
                            auxTransitions.append(transition.getDestinyNode())
                transitions[char] = auxTransitions
            nTransitions = []
            for aux in transitions:
                nTransitions.append(transitions[aux])
            temporaryState[stringStates] = nTransitions

            for nStates in temporaryState[stringStates]:
                if len(nStates) > 0:
                    self.__generateTemporaryStates(temporaryState, nStates, alphabet)

    # Função para criar o AFD a partir de um AFN
    def generateAFD(self, automaton):
        # Set para armazenar os estados
        temporaryStates = {}
        alphabet = automaton.getAlphabet()
        self.__generateTemporaryStates(temporaryStates, automaton.getInitialStates(), alphabet)

        # Cria o AFD básico com base nos estados gerados
        afd = Automaton()
        afd.setAlphabet(alphabet)
        for stateName in temporaryStates:
            afd.addState(Node(stateName))

        # Cria transições
        for state in temporaryStates:
            for i in range(len(alphabet)):
                if len(temporaryStates[state][i]) > 0:
                    afd.getStateByName(state).addTransition(
                        alphabet[i],
                        afd.getStateByName(self.__generateStringStates(temporaryStates[state][i]))
                    )

        # Adiciona o nó Inicial e os nós finais ao AFD
        afd.addInitialState(afd.getStateByName(
            self.__generateStringStates(automaton.getInitialStates())))
        for afdState in afd.getStates():
            for afnState in automaton.getFinalStates():
                if (afnState.getName() + "," in afdState.getName() or
                    afnState.getName() + "}" in afdState.getName()) and \
                        afdState not in afd.getFinalStates():
                    afd.addFinalState(afdState)

        # Renomeia os nós
        name = 0
        for state in afd.getStates():
            state.setName('q' + str(name))
            name = name + 1

        # Deleta o AFN e retorna o AFD
        del automaton
        return afd
