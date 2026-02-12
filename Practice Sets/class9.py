class Notification:
    def send_notification(self, message):
        print("Sending notification")

class Email(Notification):
    def send_notification(self, message):
        print("Sending EMAIL:", message)

class SMS(Notification):
    def send_notification(self, message):
        print("Sending SMS:", message)

n1 = Email()
n2 = SMS()
n1.send_notification("Hello via Email!")
n2.send_notification("Hello via SMS!")