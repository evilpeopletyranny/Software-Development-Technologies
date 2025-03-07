from command import Editor, InsertCommand, DeleteCommand


# Клиентский код (аналог Main.java)
def main():
    editor = Editor()

    # Вставка текста "Hello "
    insert_hello = InsertCommand(editor.text_editor, 0, "Hello ")
    editor.execute_command(insert_hello)
    editor.print_text()  # Ожидается: "Hello "

    # Вставка текста "World!" в конец текущего текста
    insert_world = InsertCommand(editor.text_editor, len(editor.text_editor.get_text()), "World!")
    editor.execute_command(insert_world)
    editor.print_text()  # Ожидается: "Hello World!"

    # Удаление "World!" начиная с позиции 6, длиной 6 символов
    delete_world = DeleteCommand(editor.text_editor, 6, 6)
    editor.execute_command(delete_world)
    editor.print_text()  # Ожидается: "Hello "

    # Отмена последнего действия (восстановление "World!")
    editor.undo()
    editor.print_text()  # Ожидается: "Hello World!"

    # Отмена вставки "World!"
    editor.undo()
    editor.print_text()  # Ожидается: "Hello "

    # Отмена вставки "Hello "
    editor.undo()
    editor.print_text()  # Ожидается: ""

    # Попытка отменить еще одну команду
    editor.undo()  # Выведет сообщение, что команд для отмены нет


if __name__ == "__main__":
    main()
