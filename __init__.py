# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

from src.Commands import Commands
from src.MessageLogs import MessageLogs
from src.Tag import Tag

if __name__ == "__main__":
    print("\n\033[1m------Aspectos Teóricos da Computação(DCC146) - Trabalho Prático------\033[0m\n")

    tags = {}  # Array com as tags criadas durante a execução da aplicação.

    while True:
        userInput = input()
        try:
            optionSelected = userInput.split()[0].upper()  # recebe apenas a primeira palavra passada, que é o comando
        except:
            optionSelected = ""

        match optionSelected:
            case ':D':
                contentInput = userInput.split()[1]  # recebe apenas a segunda palavra passada, que é o conteudo
                Commands.divideTagsFile()
            case ':C':
                contentInput = userInput.split()[1]
                file = Commands.chargeFile(contentInput)
            case ':O':
                contentInput = userInput.split()[1]
                Commands.outputFilePath(contentInput)
            case ':P':
                contentInput = userInput.split()[1]
                Commands.divideTagsParam()
            case ':A':
                Commands.listAutoInMemory()
            case ':L':
                Commands.listValidTags(tags)
            case ':Q':
                Commands.quit()
            case ':S':
                contentInput = userInput.split()[1]
                Commands.saveTags()
            case default:
                if ': ' in userInput:
                    newTag = userInput.split(': ', 1)

                    if Tag.validateTag(newTag):
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
                    else:
                        MessageLogs.error("Formato da tag inválido!")

                else:
                    MessageLogs.error("Tag ou Comando inválido")
