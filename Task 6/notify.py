class Notification:
    def send(self): pass

class Email(Notification):
    def send(self): print("Email sent")

class SMS(Notification):
    def send(self): print("SMS sent")

for n in [Email(), SMS()]:
    n.send()
