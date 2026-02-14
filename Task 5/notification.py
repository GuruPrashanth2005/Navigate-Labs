class Notification:
    def send(self, message):
        pass

class Email(Notification):
    def send(self, message):
        print("Email sent:", message)

class SMS(Notification):
    def send(self, message):
        print("SMS sent:", message)

n = Email()
n.send("Hello")
