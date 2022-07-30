# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

from src.MessageLogs import MessageLogs

filesPath = '../files/'


class Commands:

    @staticmethod
    def divideTagsFile():  #:d
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return

    @staticmethod
    def chargeFile(nameFile: str):  #:c
        try:
            file = open(filesPath + nameFile, "r", encoding="utf-8").readlines()
            MessageLogs.info("Arquivo aberto com exito!\n")
            return file
        except IOError:
            MessageLogs.error("Arquivo não encontrado!\n")

    @staticmethod
    def outputFilePath(nameFile: str):  #:o
        file = open(filesPath + nameFile, "w", encoding="UTF-8")
        MessageLogs.info(filesPath + nameFile)
        return file

    @staticmethod
    def divideTagsParam():  #:p
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
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
