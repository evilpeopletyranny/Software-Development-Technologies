from engine_facad import *


def main():
    DEFAULT_COOLING_TEMP = 90
    MAX_ALLOWED_TEMP = 50

    # Управление двигателем "вручную"
    print("Manual engine operations:")
    # Создаем компоненты двигателя
    fuel_injector = FuelInjector()
    air_flow_controller = AirFlowController()
    starter = Starter()
    cooling_controller = CoolingController()
    catalytic_converter = CatalyticConverter()

    # Правильная последовательность действий для включения двигателя
    air_flow_controller.take_air()
    fuel_injector.on()
    fuel_injector.inject()
    starter.start()
    cooling_controller.set_temperature_upper_limit(DEFAULT_COOLING_TEMP)
    cooling_controller.run()
    catalytic_converter.on()

    print("\n-------------------------\n")

    # Правильная последовательность действий для выключения двигателя
    fuel_injector.off()
    catalytic_converter.off()
    cooling_controller.cool(MAX_ALLOWED_TEMP)
    cooling_controller.stop()
    air_flow_controller.off()

    print("\n-------------------------\n")

    # Использование паттерна Фасад для управления двигателем
    print("Using CarEngineFacade:")
    engine_facade = CarEngineFacade()

    print("Starting engine via facade:")
    engine_facade.start_engine()

    print("\nStopping engine via facade:")
    engine_facade.stop_engine()


if __name__ == "__main__":
    main()
