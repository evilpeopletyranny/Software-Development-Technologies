# Задание

В этом задании вам предстоит реализовать паттерн проектирования **"Мультитон" (Multiton)** для управления различными
экземплярами логгеров, предназначенными для разных модулей приложения: **Authentication**, **Payment** и **Notification
**. Каждый
логгер будет отвечать за запись логов, связанных с определённым модулем. Паттерн Мультитон позволит вам контролировать
количество экземпляров логгеров, обеспечивая, что для каждого модуля существует только один логгер.

## Требования

1. Создать перечисление ```LoggerType```: Содержит значения: ```AUTHENTICATION```, ```PAYMENT```, ```NOTIFICATION```.
2. Создать интерфейс ```Logger```: Метод: ```log(message:str)```.
3. Создать классы ```AuthenticationLogger```, ```PaymentLogger``` и ```NotificationLogger```, реализующие
   интерфейс ```Logger```:
    - Каждый класс должен иметь конструктор без параметров.
    - Метод ```log(message:str)``` должен выводить сообщение в формате: ```[Module] Message```, где ```Module``` —
      имя соответствующего модуля.
4. Создать интерфейс ```LoggerFactory```: Метод: ```Logger createLogger();.```
5. Создать классы ```AuthenticationLoggerFactory```, ```PaymentLoggerFactory``` и ```NotificationLoggerFactory```,
   реализующие интерфейс ```LoggerFactory```.
6. Создать класс ```LoggerFactoryMultiton```, реализующий паттерн Мультитон:
    - Использует ```map<LoggerType, LoggerFactory>``` для хранения экземпляров фабрик.
    - Предоставляет статический метод ```get_instance(type: LoggerType)```, возвращающий соответствующую фабрику

## Дополнительно

**Важно!!!** Соблюдайте нейминг классов - для проверки.

Считайте, что соблюдение предписанных именований тоже часть задания :)

## Проверка

Для проверки раскоментируйте содержимое функции ```main``` в [main.py](main.py). Если всё работает без
ошибок - вы молодец!

_Незабудьте заимпортировать необходимые классы._

## Время: 15-20 минут