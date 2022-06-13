# Augusto Castilho - 201876044
# Caio Azevedo -
# Giovane Machado - 201876019
# Matheus Rubio - 201876036
from email.message import Message
from src.MessageLogs import MessageLogs


class Tags:
    __tags = {}

    def validateTag(self, tag):
        tagName = tag[0].upper()
        tagValue = tag[1]

        if tagName in self.__tags:
            MessageLogs.error(f'A Tag {tagName} informada já existe!')
            return False
        if ' ' in tagName or ' ' in tagValue:
            MessageLogs.error(f'Formato da tag inválido!')
            return False

        return True

    def addNewTag(self, newTag):
        MessageLogs.success('TAG VÁLIDA!')
