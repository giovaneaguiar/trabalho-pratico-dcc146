# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

stack = []
charsEscape = ['n', '\\', '*', '.', '+', 'l']


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

                # A fim de definir linguagens (ou tags) com caracteres especiais, que usam os meta-símbolos da linguagem
                # ou a cadeia vazia (λ), serão usados símbolos de escape. Os símbolos de escape são especificados
                # usando o símbolo \ seguido por um caractere.
                case '\\':
                    if tagValue[1] in charsEscape:
                        stack.append(tagValue[0]+tagValue[1])
                        tagValue = tagValue[2:len(tagValue)]
                    else:
                        stack.clear()
                        return False
                case default:
                    stack.append(tagValue[0])
                    tagValue = tagValue[1:len(tagValue)]

        if len(stack) != 1:
            stack.clear()
            return False

        print("Expressão Regular: " + stack[0])

        stack.clear()
        return True
