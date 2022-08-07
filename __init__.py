# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

from src.Commands import Commands
from src.MessageLogs import MessageLogs
from src.Tag import Tag
from src.Converter import Converter


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
    automatons = Converter()

    twoParamCommands = [':D', ':C', ':O', ':P', ':S']

    while True:
        userInput = input()
        try:
            optionSelected = userInput.split()[0].upper()  # recebe apenas a primeira palavra passada, que é o comando
        except:
            optionSelected = ""
        if optionSelected in twoParamCommands:
            try:
                contentInput = userInput[3:]  # recebe apenas a segunda palavra passada, que é o conteudo
            except:
                MessageLogs.error("Este comando requer dois parâmetros.")

        match optionSelected:
            case ':D':
                # Se o arquivo não for encontrado, continua a aplicação
                try:
                    Commands.divideTagsFile(Commands, contentInput, automatons.getAutomatons())
                except Exception as e:
                    MessageLogs.error("Erro ao dividir as tags com arquivo de entrada! " + str(e))

            case ':C':
                try:
                    file = Commands.chargeFile(contentInput)
                    for line in file:
                        newTag = line.split(': ', 1)
                        if Tag.validateTag(newTag):
                            addTag(newTag)
                            automatons.addAutomaton(newTag[0].upper(), newTag[1])
                        else:
                            MessageLogs.error("Formato da tag inválido!")
                except Exception as e:
                    MessageLogs.error("Erro ao carregar um arquivo com as definições de tag! " + str(e))

            case ':O':
                try:
                    Commands.outputFilePath(Commands, contentInput)
                except Exception as e:
                    MessageLogs.error("Erro ao setar arquivo de saída para divisão de tags! " + str(e))

            case ':P':
                try:
                    outputFile = open(Commands.outputFileForSplitTags, 'w', encoding='utf-8') if Commands.outputFileForSplitTags else None
                    Commands.divideTagsParam(Commands, contentInput, automatons.getAutomatons(), outputFile)
                except Exception as e:
                    MessageLogs.error("Erro ao dividir as tags com a entrada via terminal! " + str(e))

            case ':A':
                try:
                    Commands.listAutoInMemory(automatons.getAutomatons())
                except Exception as e:
                    MessageLogs.error("Erro ao listar as definições formais dos autômatos em memória! " + str(e))

            case ':L':
                try:
                    Commands.listValidTags(tags)
                except Exception as e:
                    MessageLogs.error("Erro ao listar as tags válidas! " + str(e))

            case ':Q':
                Commands.quit()

            case ':S':
                try:
                    Commands.saveTagsInFile(tags, contentInput)
                except Exception as e:
                    MessageLogs.error("Erro ao salvar as tags em um arquivo! " + str(e))

            case default:
                if ': ' in userInput:
                    newTag = userInput.split(': ', 1)
                    if Tag.validateTag(newTag):
                        addTag(newTag)
                        automatons.addAutomaton(newTag[0].upper(), newTag[1])
                    else:
                        MessageLogs.error("Formato da tag inválido!")
                else:
                    MessageLogs.error("Tag ou Comando inválido")
