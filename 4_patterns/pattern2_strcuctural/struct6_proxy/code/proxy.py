from abc import ABC, abstractmethod
import time


# Интерфейс сервиса
class DataService(ABC):
    @abstractmethod
    def fetch_data(self, parameter: str) -> str:
        pass


# Реальная реализация сервиса
class DataServiceImpl(DataService):
    def fetch_data(self, parameter: str) -> str:
        self.simulate_expensive_operation()
        return f"Data for {parameter}"

    def simulate_expensive_operation(self):
        print("Fetching data from external source...")
        time.sleep(3)  # Симуляция задержки 3 секунды


# Прокси с кэшированием, который инициализирует реальный сервис внутри себя
class CachingDataServiceProxy(DataService):
    def __init__(self):
        self.real_data_service = DataServiceImpl()  # Создаем реальный сервис внутри прокси
        self.cache = {}

    def fetch_data(self, parameter: str) -> str:
        if parameter in self.cache:
            print(f"Returning cached data for: {parameter}")
            return self.cache[parameter]
        print(f"No cache found for: {parameter}. Fetching data...")
        data = self.real_data_service.fetch_data(parameter)
        self.cache[parameter] = data
        return data
