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
            if self.__divideTags(self, line, automatons):
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
            i = 0
            while i < file.__len__():
                file[i] = file[i].rstrip('\n')
                i = i + 1
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
        if self.__divideTags(self, string, automatons):
            print(" ".join(self.__tagsInput))
        else:
            MessageLogs.error("A entrada não pode ser completamente reconhecida!")
        return

    @staticmethod
    def listAutoInMemory(automatons):  #:a
        i = 0
        if len(automatons) >= 1:
            for auto in automatons:
                print(auto.formalDefinition(i))
                print(auto.transitionFunc(i))
                i = i + 1
        else:
            MessageLogs.info("Ainda não há autômatos em memória!")
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
        recognized = ""
        while lastChar >= firstChar:
            # Testa se a entrada é reconhecida por algum automato
            for automaton in automatons:
                if automaton.analyzeString(string[firstChar:lastChar]):
                    if not foundAutomaton:
                        recognized = automaton.getTagName()
                        self.__tagsInput.append(recognized)
                        # firstChar = lastChar
                        # lastChar = len(string)
                        foundAutomaton = True
                    else:
                        MessageLogs.warning(f"Sobreposição na definição das Tags: {recognized} e { automaton.getTagName() }")

            # Se nenhum automato reconhecer o texto, o caractere final eh retirado
            if not foundAutomaton:
                lastChar = lastChar - 1
                if lastChar == firstChar:
                    return False
            else:
                if lastChar == firstChar:
                    break
                else:
                    foundAutomaton = False
                    firstChar = lastChar
                    lastChar = len(string)
        return True
