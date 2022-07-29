# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036
from src.MessageLogs import MessageLogs

stack = []


class Tag:

    def __init__(self, tagName, tagValue):
        self.tagName = tagName
        self.tagValue = tagValue

    @staticmethod
    def validateTag(tag):
        tagName = tag[0].upper()
        tagValue = tag[1]

        if ' ' in tagName:
            return False

        while len(tagValue) > 0:
            match tagValue[0]:
                case '+':
                    if len(stack) >= 2:
                        lastValue = stack.pop(len(stack) - 1)
                        penultValue = stack.pop(len(stack) - 1)
                        newValue = penultValue + "+" + lastValue
                        stack.append(newValue)
                        tagValue = tagValue[1:len(tagValue)]
                    else:
                        stack.clear()
                        return False
                case '.':
                    if len(stack) >= 2:
                        lastValue = stack.pop(len(stack) - 1)
                        penultValue = stack.pop(len(stack) - 1)
                        newValue = penultValue + lastValue
                        stack.append(newValue)
                        tagValue = tagValue[1:len(tagValue)]
                    else:
                        stack.clear()
                        return False
                case '*':
                    if len(stack) >= 1:
                        lastValue = stack.pop(len(stack) - 1)
                        newValue = "(" + lastValue + ")*"
                        stack.append(newValue)
                        tagValue = tagValue[1:len(tagValue)]
                    else:
                        stack.clear()
                        return False
                case ' ':
                    return True
                case default:
                    stack.append(tagValue[0])
                    tagValue = tagValue[1:len(tagValue)]

        print("PILHA FINAL: " + stack[0])

        if len(stack) != 1:
            stack.clear()
            return False

        stack.clear()
        return True
