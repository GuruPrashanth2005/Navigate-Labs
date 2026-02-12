from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send_notification(self):
        pass
class Email(Notification):
    def send_notification(self):
        return "Sending via Email"
class SMS(Notification):
    def send_notification(self):
        return "Sending via SMS"
email = Email()
sms = SMS()
print(email.send_notification())
print(sms.send_notification())
