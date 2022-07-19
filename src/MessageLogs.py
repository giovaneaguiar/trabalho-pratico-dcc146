# Augusto Castilho - 201876044
# Giovane Machado - 201876019
# Matheus Rubio - 201876036
class MessageLogs:
    @staticmethod
    def warning(message: str):
        print("\n \U0001f7e1 [WARNING] " + message)
        return

    @staticmethod
    def info(message: str):
        print("\n \U0001f535 [INFO] " + message)
        return

    @staticmethod
    def error(message: str):
        print("\n \U0001f534 [ERROR] " + message)
        return

    @staticmethod
    def success(message: str):
        print("\n \u2705 [SUCCESS] " + message)
        return
