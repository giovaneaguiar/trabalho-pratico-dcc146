# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

import os.path
from src.MessageLogs import MessageLogs

previousPath = os.path.abspath(os.path.dirname(__file__))


class Commands:
    __tagsInput = []  # Array com todas as tags da entrada especificada em sentido ocidental
    __tagsInput2 = []  # Array com todas as tags da entrada especificada em sentido oriental
    outputFileForSplitTags = None

    def divideTagsFile(self, string: str, automatons):  #:d
        file = self.chargeFile(string)
        outputFile = open(self.outputFileForSplitTags, 'w', encoding='utf-8') if self.outputFileForSplitTags else None
        outputIndex = 1
        for line in file:
            print("Entrada " + str(outputIndex) + ": " + line)
            self.divideTagsParam(self, line, automatons, outputFile)
            outputIndex = outputIndex + 1
        return

    @staticmethod
    def chargeFile(nameFile: str):  #:c
        filesPath = os.path.join(previousPath, '..', 'files/input', nameFile)
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
    def outputFilePath(self, nameFile: str):  #:o
        self.outputFileForSplitTags = os.path.join(previousPath, '..', 'files/output', nameFile)
        MessageLogs.success("Caminho de saída para a divisão de tags especificado com sucesso!")
        return

    def divideTagsParam(self, string: str, automatons, outputFile):  #:p
        self.__tagsInput.clear()
        self.__tagsInput2.clear()
        way1 = self.__divideTags(self, string, automatons, 1)
        way2 = self.__divideTags(self, string, automatons, 0)
        # Verifica qual caminho obteve o melhor resultado
        if way1 and way2:
            if self.__tagsInput.__len__() << self.__tagsInput2.__len__():
                outputFile.write(" ".join(self.__tagsInput) + "\n") if outputFile else print(" ".join(self.__tagsInput))
            else:
                outputFile.write(" ".join(self.__tagsInput2) + "\n") if outputFile else print(" ".join(self.__tagsInput2))
        elif way1:
            outputFile.write(" ".join(self.__tagsInput) + "\n") if outputFile else print(" ".join(self.__tagsInput))
        elif way2:
            outputFile.write(" ".join(self.__tagsInput2) + "\n") if outputFile else print(" ".join(self.__tagsInput2))
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
        if len(tags):
            for tag in tags:
                print(tag + ": " + tags[tag])
        else:
            MessageLogs.warning("Nenhuma Tag foi validada ainda!")
        return

    @staticmethod
    def quit():  #:q
        MessageLogs.info("Saindo do programa!")
        exit()

    @staticmethod
    def saveTagsInFile(tags, fileInputName):  #:s
        filesPath = os.path.join(previousPath, '..', 'files/output', fileInputName)
        file = open(filesPath, "w", encoding="UTF-8")
        if len(tags):
            for tag in tags:
                file.write(tag + ": " + tags[tag] + '\n')
            file.close()
            MessageLogs.success("Tags salvas no arquivo " + fileInputName + " com sucesso!")
            return
        else:
            MessageLogs.warning("Nenhuma Tag foi validada ainda!")

    # ------------------- Fim dos comandos -------------------
    #
    # ------------------ Métodos auxiliares ------------------

    # way = 1 percorre a entrada especificada em sentido ocidental
    # se way != 1, percorre a entrada especificada em sentido oriental
    def __divideTags(self, string: str, automatons, way: int):
        firstChar = 0
        lastChar = len(string)
        foundAutomaton = False
        recognized = ""  # String que guarda o automato encontrado, para verificar a ambiguidade dos automatos
        while lastChar >= firstChar:
            # Testa se a entrada é reconhecida por algum automato
            for automaton in automatons:
                if automaton.analyzeString(string[firstChar:lastChar]):
                    if not foundAutomaton:
                        recognized = automaton.getTagName()
                        if way == 1:
                            self.__tagsInput.append(recognized)
                        else:
                            self.__tagsInput2.insert(0, recognized)
                        foundAutomaton = True
                    else:
                        MessageLogs.warning(f"Sobreposição na definição das Tags "
                                            f"{ recognized } e { automaton.getTagName() }")

            # Se nenhum automato reconhecer o texto, o caractere final ou inicial eh retirado
            if not foundAutomaton:
                if way == 1:
                    lastChar = lastChar - 1
                else:
                    firstChar = firstChar + 1
                if lastChar == firstChar:
                    return False
            # Se algum automato reconhecer o texto, começa de novo com o restante do texto
            else:
                if lastChar == firstChar:
                    break
                else:
                    foundAutomaton = False
                    if way == 1:
                        firstChar = lastChar
                        lastChar = len(string)
                    else:
                        lastChar = firstChar
                        firstChar = 0
        return True
