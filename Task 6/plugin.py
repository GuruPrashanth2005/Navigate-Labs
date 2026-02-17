class Plugin:
    def execute(self):
        pass


class LoggerPlugin(Plugin):
    def execute(self):
        print("Logging Enabled")


class AuthPlugin(Plugin):
    def execute(self):
        print("Authentication Enabled")


plugins = [LoggerPlugin(), AuthPlugin()]

for p in plugins:
    p.execute()
