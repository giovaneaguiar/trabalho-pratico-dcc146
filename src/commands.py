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
        except IOError:
            MessageLogs.info("Arquivo não encontrado!\n")
            return file

    @staticmethod
    def outputFilePath():  #:o
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return

    @staticmethod
    def divideTagsParam():  #:p
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return

    @staticmethod
    def listAutoInMemory():  #:a
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return

    @staticmethod
    def listValidTags():    #:l
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return

    @staticmethod
    def quit():     #:q
        MessageLogs.info("Saindo do programa!")
        exit()

    @staticmethod
    def saveTags():     #:s
        MessageLogs.warning("Esta funcionalidade ainda não foi implementada!")
        return
