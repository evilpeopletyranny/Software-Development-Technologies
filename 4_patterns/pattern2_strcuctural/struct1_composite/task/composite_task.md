# Задание

Вы разрабатываете систему для управления организационной структурой крупной компании. Компания состоит из множества
подразделений (департаментов), каждое из которых может содержать других менеджеров, сотрудников и поддепартаментов.
Необходимо создать модель, которая позволит эффективно управлять этой структурой, выполнять операции над любым уровнем
иерархии и легко расширять систему.

## Требования

1. **Определение Интерфейса Компонента:**
    - Создайте интерфейс ```EmployeeComponent```, который будет определять общие методы для всех элементов
      организационной структуры (например, ```show_details()```).
2. **Реализация Листа (Leaf):**
    - Создайте класс ```Employee```, представляющий отдельного сотрудника. Этот класс должен реализовывать
      интерфейс ```EmployeeComponent``` и содержать информацию о сотруднике (например, имя, должность, зарплата).
3. **Реализация Композита (Composite):**
    - Создайте класс ```Department```, представляющий подразделение компании. Этот класс должен также реализовывать
      интерфейс ```EmployeeComponent``` и содержать список дочерних компонентов (```Employee``` и
      другие ```Department```).
4. **Дополнительные Функции:**
    - Реализуйте методы для добавления и удаления компонентов (```add```, ```remove```) в классе Department.
    - Реализуйте метод для подсчета общей зарплаты в подразделении и во всей организации.

Для проверки используйте модуль [main.py](main.py)

### Время 15-20 минут