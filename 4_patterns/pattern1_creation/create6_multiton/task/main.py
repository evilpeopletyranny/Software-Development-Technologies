def main():
    pass
    # # Получение фабрик для разных типов логгеров
    # auth_factory1 = LoggerFactoryMultiton.get_factory(LoggerType.AUTHENTICATION)
    # auth_factory2 = LoggerFactoryMultiton.get_factory(LoggerType.AUTHENTICATION)
    #
    # payment_factory1 = LoggerFactoryMultiton.get_factory(LoggerType.PAYMENT)
    # payment_factory2 = LoggerFactoryMultiton.get_factory(LoggerType.PAYMENT)
    #
    # notification_factory1 = LoggerFactoryMultiton.get_factory(LoggerType.NOTIFICATION)
    # notification_factory2 = LoggerFactoryMultiton.get_factory(LoggerType.NOTIFICATION)
    #
    # # Проверка, что для каждого типа логгера создаётся только одна фабрика
    # print("Проверка экземпляров фабрик:")
    # print("auth_factory1 == auth_factory2:", auth_factory1 is auth_factory2)
    # print("payment_factory1 == payment_factory2:", payment_factory1 is payment_factory2)
    # print("notification_factory1 == notification_factory2:", notification_factory1 is notification_factory2)
    #
    # print("\nСоздание логгеров через фабрики:")
    # auth_logger = auth_factory1.create_logger()
    # payment_logger = payment_factory1.create_logger()
    # notification_logger = notification_factory1.create_logger()
    #
    # # Запись логов
    # auth_logger.log("Пользователь успешно аутентифицирован.")
    # payment_logger.log("Платёж обработан успешно.")
    # notification_logger.log("Уведомление отправлено пользователю.")


if __name__ == "__main__":
    main()