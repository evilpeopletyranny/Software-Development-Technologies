from engine import *


class CarEngineFacade:
    DEFAULT_COOLING_TEMP = 90
    MAX_ALLOWED_TEMP = 50

    def __init__(self):
        self.fuel_injector = FuelInjector()
        self.air_flow_controller = AirFlowController()
        self.starter = Starter()
        self.cooling_controller = CoolingController()
        self.catalytic_converter = CatalyticConverter()

    def start_engine(self):
        self.fuel_injector.on()
        self.air_flow_controller.take_air()
        # В оригинальном коде fuelInjector.on() вызывается дважды.
        self.fuel_injector.on()
        self.fuel_injector.inject()
        self.starter.start()
        self.cooling_controller.set_temperature_upper_limit(self.DEFAULT_COOLING_TEMP)
        self.cooling_controller.run()
        self.catalytic_converter.on()

    def stop_engine(self):
        self.fuel_injector.off()
        self.catalytic_converter.off()
        self.cooling_controller.cool(self.MAX_ALLOWED_TEMP)
        self.cooling_controller.stop()
        self.air_flow_controller.off()
