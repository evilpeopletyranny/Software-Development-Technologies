from proxy import CachingDataServiceProxy


# Клиентский код
def main():
    # Создаем прокси без передачи реального сервиса
    caching_proxy = CachingDataServiceProxy()

    print("First request:")
    data1 = caching_proxy.fetch_data("param1")
    print("Received:", data1, "\n")

    print("Second request:")
    data2 = caching_proxy.fetch_data("param1")
    print("Received:", data2, "\n")

    print("Third request:")
    data3 = caching_proxy.fetch_data("param2")
    print("Received:", data3, "\n")

    print("Fourth request:")
    data4 = caching_proxy.fetch_data("param2")
    print("Received:", data4)


if __name__ == "__main__":
    main()
