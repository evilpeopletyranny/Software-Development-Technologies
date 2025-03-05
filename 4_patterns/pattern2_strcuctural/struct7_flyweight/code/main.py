from flyweight import CharacterFlyweightFactory, CharacterContext


# Клиентский код (аналог FlyweightPatternMain.java)
def main():
    text = "HELLO HELLO"
    font = "Arial"
    size = 12

    x = 0
    y = 0

    for c in text:
        flyweight = CharacterFlyweightFactory.get_character(c, font, size)
        context = CharacterContext(x, y)
        flyweight.display(context)
        x += 10  # увеличение позиции по оси X

    print("Total Flyweight objects created:", CharacterFlyweightFactory.get_flyweight_count())


if __name__ == "__main__":
    main()
