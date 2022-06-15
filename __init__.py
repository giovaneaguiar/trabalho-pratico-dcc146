# Augusto Castilho - 201876044
# Caio Azevedo - 201876017
# Giovane Machado - 201876019
# Matheus Rubio - 201876036

from src.MessageLogs import MessageLogs
from Commands import Commands
from Tags import Tags


def menu():
    MessageLogs.info("Para utilização do programa, utilize as seguintes instruções ou defina uma TAG:")
    print("\t\033[1m:d\033[0m - realiza a divisão em tags da string do arquivo informado")
    print("\t\033[1m:c\033[0m - carrega um arquivo com definições de tags")
    print("\t\033[1m:o\033[0m - especifica o caminho do arquivo de saída para a divisão em tags")
    print("\t\033[1m:p\033[0m - realiza a divisão em tags da entrada informada")
    print("\t\033[1m:a\033[0m - Lista as definições formais dos autômatos em memória")
    print("\t\033[1m:l\033[0m - Lista as definições de tag válidas")
    print("\t\033[1m:q\033[0m - sair do programa")
    print("\t\033[1m:s\033[0m - salvar as tags\n")
    return input("Digite a operação desejada: ")


if __name__ == "__main__":
    print("\n\033[1m------Aspectos Teóricos da Computação(DCC146) - Trabalho Prático------\033[0m\n")

    tags = Tags()

    while True:
        userInput = menu()
        optionSelected = userInput.split()[0].upper()  # recebe apenas a primeira palavra passada, que é o comando

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
                Commands.listValidTags()
            case ':Q':
                Commands.quit()
            case ':S':
                contentInput = userInput.split()[1]
                Commands.saveTags()
            case default:
                if ': ' in userInput:
                    newTag = userInput.split(': ', 1)
                    if tags.validateTag(newTag):
                        tags.addNewTag(newTag)
                else:
                    MessageLogs.error("Tag ou Comando inválido")
