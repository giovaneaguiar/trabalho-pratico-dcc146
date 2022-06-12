# Augusto Castilho - 201876044
# Caio Azevedo -
# Giovane Machado -
# Matheus Rubio - 201876036

from commands import Commands


def menu():
    print("[INFO]Para utilização do programa, utilize as seguintes instruções:")
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

    command = menu()
    commands = Commands()

    while True:
        match command:
            case ':d':
                commands.twoPointsD()
            case ':c':
                nameFile = input("Nome do arquivo a ser lido: ")
                file = commands.twoPointsC(nameFile)
            case ':o':
                commands.twoPointsO()
            case ':p':
                commands.twoPointsP()
            case ':a':
                commands.twoPointsA()
            case ':l':
                commands.twoPointsL()
            case ':q':
                commands.twoPointsQ()
            case ':s':
                commands.twoPointsS()
            case default:
                commands.error()

        commands = menu()
