from abc import ABC,abstractmethod

class Mail(ABC):
    @abstractmethod
    def send(self):
        pass
class Email(Mail):
    def send(self):
        print("Email should be entered")
class SMS(Mail):
    def send(self):
        print("SMS will be sent")
class Whatsapp(Mail):
    def send(self):
        print("HELLO")
e=Email()
s=SMS()
w=Whatsapp()
e.send()
s.send()
w.send()