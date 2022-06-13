# Augusto Castilho - 201876044
# Caio Azevedo -
# Giovane Machado -
# Matheus Rubio - 201876036

from src.MessageLogs import MessageLogs
from src.commands import Commands
from src.tags import Tags


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
    print("\t\033[1mINT\033[0m - Número inteiros")
    print("\t\033[1mSPACE\033[0m - Sequência de espaços em branco")
    print("\t\033[1mVAR\033[0m - Sequência de símbolo alfanuméricos com o primeiro símbolo sendo uma letra")
    print("\t\033[1mEQUALS\033[0m - O símbolo “=”")
    print("\t\033[1mCOMMENT\033[0m - Qualquer sequência contida entra os símbolos “/*” e “*/”\n")
    return input("Digite a operação desejada: ")


if __name__ == "__main__":
    print("\n\033[1m------Aspectos Teóricos da Computação(DCC146) - Trabalho Prático------\033[0m\n")

    commands = Commands()
    tags = Tags()

    while True:
        userInput = menu()
        optionSelected = userInput.split()[0].upper()  # recebe apenas a primeira palavra passada, que é o comando

        match optionSelected:
            case ':D':
                contentInput = userInput.split()[1]  # recebe apenas a segunda palavra passada, que é o conteudo
                commands.divideTagsFile()
            case ':C':
                contentInput = userInput.split()[1]
                file = commands.chargeFile(contentInput)
            case ':O':
                contentInput = userInput.split()[1]
                commands.outputFilePath(contentInput)
            case ':P':
                contentInput = userInput.split()[1]
                commands.divideTagsParam()
            case ':A':
                commands.listAutoInMemory()
            case ':L':
                commands.listValidTags()
            case ':Q':
                commands.quit()
            case ':S':
                contentInput = userInput.split()[1]
                commands.saveTags()
            case 'INT:':
                contentInput = userInput.split()[1]
                valid = tags.validateTag(contentInput)
                if valid is False:
                    MessageLogs.error("A Tag INT já foi definida")
            case default:
                MessageLogs.error("Sintaxe incorreta")

