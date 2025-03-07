from mediator import ChatRoom, User


# Клиентский код
def main():
    chat_room = ChatRoom()

    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    chat_room.register(alice)
    chat_room.register(bob)
    chat_room.register(charlie)

    alice.send("Привет всем!")
    bob.send("Привет, Alice!")
    charlie.send("Здравствуйте!")


if __name__ == "__main__":
    main()
