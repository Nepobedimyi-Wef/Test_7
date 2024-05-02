#B1
class Message:
    def __init__(self, name):
        self.name = name
    def message(self):
        print(f"{self.name} Hello")

name = input(f"Enter you'r name: ")
message = Message(name)
message.message()
