# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

from src.Commands import Commands
from src.MessageLogs import MessageLogs
from src.Tag import Tag


def addTag(newTag):
    newTagName = newTag[0].upper()
    newTagValue = newTag[1]
    newTag = Tag(newTagName, newTagValue)
    if newTagName in tags:
        MessageLogs.error("Tag já existe!")
        MessageLogs.warning("Deseja sobreescrever a Tag? (s/n)")
        if input() == 's':
            tags[newTag.tagName] = newTag.tagValue
            MessageLogs.success("Tag válida!")
    else:
        tags[newTag.tagName] = newTag.tagValue
        MessageLogs.success("Tag válida!")


if __name__ == "__main__":
    print("\n\033[1m------Aspectos Teóricos da Computação(DCC146) - Trabalho Prático------\033[0m\n")

    tags = {}  # Array com as tags criadas durante a execução da aplicação.
    automatons = {}  # Array com autômatos

    twoParamCommands = [':D', ':C', ':O', ':P', ':S']

    while True:
        userInput = input()
        try:
            optionSelected = userInput.split()[0].upper()  # recebe apenas a primeira palavra passada, que é o comando
        except:
            optionSelected = ""
        if optionSelected in twoParamCommands:
            try:
                contentInput = userInput.split()[1]  # recebe apenas a segunda palavra passada, que é o conteudo
            except:
                MessageLogs.error("Este comando requer dois parâmetros.")

        match optionSelected:
            case ':D':
                # Se o arquivo não for encontrado, continua a aplicação
                try:
                    Commands.divideTagsFile(contentInput, automatons)
                except:
                    pass

            case ':C':
                try:
                    file = Commands.chargeFile(contentInput)
                    for line in file:
                        line = line.rstrip('\n')
                        newTag = line.split(': ', 1)
                        if Tag.validateTag(newTag):
                            addTag(newTag)
                        else:
                            MessageLogs.error("Formato da tag inválido!")
                except:
                    pass

            case ':O':
                try:
                    Commands.outputFilePath(contentInput)
                except:
                    pass

            case ':P':
                Commands.divideTagsParam(contentInput, automatons)

            case ':A':
                Commands.listAutoInMemory()

            case ':L':
                Commands.listValidTags(tags)

            case ':Q':
                Commands.quit()

            case ':S':
                try:
                    Commands.saveTags()
                except:
                    pass

            case default:
                if ': ' in userInput:
                    newTag = userInput.split(': ', 1)
                    if Tag.validateTag(newTag):
                        addTag(newTag)
                    else:
                        MessageLogs.error("Formato da tag inválido!")
                else:
                    MessageLogs.error("Tag ou Comando inválido")
