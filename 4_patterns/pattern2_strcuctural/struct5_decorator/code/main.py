from decorator import SimpleMessage, EncryptedMessageDecorator, TimestampedMessageDecorator


def main():
    # Создание простого сообщения
    simple_message = SimpleMessage("Hello, World!")
    print("Simple Message:", simple_message.get_content())

    # Добавление шифрования
    encrypted_message = EncryptedMessageDecorator(simple_message)
    print("Encrypted Message:", encrypted_message.get_content())

    # Добавление временной метки
    timestamped_message = TimestampedMessageDecorator(simple_message)
    print("Timestamped Message:", timestamped_message.get_content())

    # Комбинирование декораторов: сначала шифрование, затем добавление метки
    encrypted_timestamped_message = TimestampedMessageDecorator(encrypted_message)
    print("Encrypted & Timestamped Message:", encrypted_timestamped_message.get_content())


if __name__ == "__main__":
    main()
