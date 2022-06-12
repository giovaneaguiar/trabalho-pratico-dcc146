# Augusto Castilho - 201876044
# Caio Azevedo -
# Giovane Machado -
# Matheus Rubio - 201876036

def warning():
    print("\n[WARNING] Esta funcionalidade ainda não foi implementada!\n")
    return


path = '../files/'


class Commands:

    @staticmethod
    def error():
        print("\n[ERROR] Erro de sintaxe!\n")
        return

    @staticmethod
    def twoPointsD():
        warning()
        return

    @staticmethod
    def twoPointsC(nameFile: str):
        try:
            file = open(path + nameFile, "r", encoding="utf-8").readlines()
            print("[INFO]Arquivo aberto com exito!\n")
        except IOError:
            print("[INFO]Arquivo não encontrado!\n")
            return file

        # print("Dados do arquivo")
        # for line in file:
        #     line = line.rstrip("\n")
        #     print(line)

    @staticmethod
    def twoPointsO():
        warning()
        return

    @staticmethod
    def twoPointsP():
        warning()
        return

    @staticmethod
    def twoPointsA():
        warning()
        return

    @staticmethod
    def twoPointsL():
        warning()
        return

    @staticmethod
    def twoPointsQ():
        print("[INFO]Saindo do programa!")
        exit()

    @staticmethod
    def twoPointsS():
        warning()
        return
