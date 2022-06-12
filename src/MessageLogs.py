# Augusto Castilho - 201876044
# Caio Azevedo -
# Giovane Machado -
# Matheus Rubio - 201876036
class MessageLogs:
    @staticmethod
    def warning(message):
        print("\n \U0001f7e1 [WARNING] " + message)
        return
    def info(message):
        print("\n \U0001f535 [INFO] " + message)
        return
    def error(message):
        print("\n \U0001f534 [ERROR] " + message)
        return
    def success(message):
        print("\n \u2705 [SUCCESS] " + message)
        return