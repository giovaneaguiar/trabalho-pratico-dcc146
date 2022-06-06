from sys import exit


def openFile(nameFile):
    try:
        file = open(nameFile, "r")
        return file
    except:
        error()


def menu():
    print("Para utilização do programa, utilize as seguintes instruções:")
    print("\t\033[1m:d\033[0m - realiza a divisão em tags da string do arquivo informado")
    print("\t\033[1m:c\033[0m - carrega um arquivo com definições de tags")
    print("\t\033[1m:o\033[0m - especifica o caminho do arquivo de saída para a divisão em tags")
    print("\t\033[1m:p\033[0m - realiza a divisão em tags da entrada informada")
    print("\t\033[1m:a\033[0m - Lista as definições formais dos autômatos em memória")
    print("\t\033[1m:l\033[0m - Lista as definições de tag válidas")
    print("\t\033[1m:q\033[0m - sair do programa")
    print("\t\033[1m:s\033[0m - salvar as tags\n")
    return input("Digite a operação desejada: ")


def warning():
    print("\n[WARNING] Esta funcionalidade ainda não foi implementada!\n")
    return menu()


def error():
    print("\n[ERROR] Erro de sintaxe!\n")
    return menu()


if __name__ == "__main__":
    print("\n\033[1m------Aspectos Teóricos da Computação(DCC146) - Trabalho Prático------\033[0m\n")

    file = openFile(input("Nome do arquivo a ser lido:"))
    print("Arquivo aberto com exito!\n")

    command = menu()

    i = 1
    while i != 0:
        match command:
            case ':d':
                command = warning()
            case ':c':
                command = warning()
            case ':o':
                command = warning()
            case ':p':
                command = warning()
            case ':a':
                command = warning()
            case ':l':
                command = warning()
            case ':q':
                file.close()
                print("Fechando arquivo!")
                print("Saindo do programa!")
                exit()
            case ':s':
                command = warning()
            case default:
                command = error()
