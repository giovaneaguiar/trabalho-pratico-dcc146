# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

import os.path
from src.MessageLogs import MessageLogs

previousPath = os.path.abspath(os.path.dirname(__file__))


class Commands:

    __tagsInput = []  # Array com todas as tags da entrada especificada

    def divideTagsFile(self, string: str, automatons):  #:d
        file = self.chargeFile(string)
        for line in file:
            self.__tagsInput.clear()
            if self.__divideTags(line, automatons):
                print(" ".join(self.__tagsInput))
            else:
                MessageLogs.error("A entrada não pode ser completamente reconhecida!")
        return

    @staticmethod
    def chargeFile(nameFile: str):  #:c
        filesPath = os.path.join(previousPath, '..', 'files', nameFile)
        try:
            file = open(filesPath, 'r', encoding='utf-8').readlines()
            MessageLogs.info("Arquivo aberto com exito!\n")
            return file
        except IOError:
            MessageLogs.error("Arquivo não encontrado!\n")

    @staticmethod
    def outputFilePath(nameFile: str):  #:o
        filesPath = os.path.join(previousPath, '..', 'files', nameFile)
        file = open(filesPath, "w", encoding="UTF-8")
        MessageLogs.info(filesPath)
        return file

    def divideTagsParam(self, string: str, automatons):  #:p
        self.__tagsInput.clear()
        if self.__divideTags(string, automatons):
            print(" ".join(self.__tagsInput))
        else:
            MessageLogs.error("A entrada não pode ser completamente reconhecida!")
        return

    @staticmethod
    def listAutoInMemory():  #:a
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return

    @staticmethod
    def listValidTags(tags):  #:l
        if len(tags) >= 1:
            for tag in tags:
                print(tag + ": " + tags[tag])
        else:
            MessageLogs.info("Nenhuma Tag foi validada ainda")
        return

    @staticmethod
    def quit():  #:q
        MessageLogs.info("Saindo do programa!")
        exit()

    @staticmethod
    def saveTags():  #:s
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return

    # ------------------- Fim dos comandos -------------------
    #
    # ------------------ Métodos auxiliares ------------------

    def __divideTags(self, string: str, automatons):
        firstChar = 0
        lastChar = len(string)
        foundAutomaton = False
        while lastChar >= firstChar:
            # Testa se a entrada é reconhecida por algum automato
            # Se não for, então retira o último elemento e testa de novo
            for automaton in automatons:
                if automaton.analyzeString(string[firstChar:lastChar]):
                    self.__tagsInput.append(automaton.getTagName())
                    firstChar = lastChar
                    lastChar = len(string)
                    foundAutomaton = True
                    break  # Para de procurar os automatos

            # Se nenhum automato reconhecer o texto, o caractere final eh retirado
            if not foundAutomaton:
                lastChar = lastChar - 1
                if lastChar == firstChar:
                    return False
            else:
                if lastChar == firstChar:
                    break
        return True
