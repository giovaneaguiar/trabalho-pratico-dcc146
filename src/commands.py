# Augusto Castilho - 201876044
# Caio Azevedo -
# Giovane Machado -
# Matheus Rubio - 201876036

from email.message import Message
from src.MessageLogs import MessageLogs

path = '../files/'


class Commands:

    @staticmethod
    def divideTagsFile():  #:d
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return

    @staticmethod
    def chargeFile(nameFile: str):  #:c
        try:
            file = open(path + nameFile, "r", encoding="utf-8").readlines()
            MessageLogs.info("Arquivo aberto com exito!\n")
            return file
        except IOError:
            MessageLogs.error("Arquivo não encontrado!\n")

    @staticmethod
    def outputFilePath(nameFile: str):  #:o
        file = open(path + nameFile, "w", encoding="UTF-8")
        MessageLogs.info(path+nameFile)
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
    def listValidTags():  #:l
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return

    @staticmethod
    def quit():  #:q
        MessageLogs.info("Saindo do programa!")
        exit()

    @staticmethod
    def saveTags():  #:s
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return
