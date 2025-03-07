from strategy import *
from editor import TextEditor


def main():
    text = "Hello, Strategy Pattern in Python!"

    # Используем стратегию верхнего регистра
    editor = TextEditor(UpperCaseStrategy())
    print("UpperCase:", editor.publish_text(text))

    # Смена стратегии на нижний регистр
    editor.set_strategy(LowerCaseStrategy())
    print("LowerCase:", editor.publish_text(text))

    # Смена стратегии на заглавные буквы каждого слова
    editor.set_strategy(TitleCaseStrategy())
    print("TitleCase:", editor.publish_text(text))


if __name__ == "__main__":
    main()
