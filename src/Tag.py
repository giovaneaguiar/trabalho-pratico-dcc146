# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036
from src.MessageLogs import MessageLogs


class Tag:
    def  __init__(self, tagName, tagValue):
        self.tagName =  tagName
        self.tagValue = tagValue

    @staticmethod
    def validateTag(tag):
        tagName = tag[0].upper()
        tagValue = tag[1]

        if ' ' in tagName or ' ' in tagValue:
            MessageLogs.error(f'Formato da tag inválido!')
            return False

        return True
