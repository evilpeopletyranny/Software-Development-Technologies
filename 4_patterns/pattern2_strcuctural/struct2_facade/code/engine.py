class TemperatureSensor:
    def get_temperature(self):
        print("Temperature Sensor get temperature")


class Starter:
    def start(self):
        print("Start!!!")


class Radiator:
    def on(self):
        print("Radiator on.")

    def off(self):
        print("Radiator off.")

    def set_speed(self):
        print("Radiator set speed.")


class FuelPump:
    def pump(self):
        print("FuelPump pump")


class FuelInjector:
    def __init__(self):
        self.fuel_pump = FuelPump()

    def on(self):
        print("Fuel Injector on.")

    def off(self):
        print("Fuel Injector off.")

    def inject(self):
        print("Fuel Injector inject")
        self.fuel_pump.pump()


class CoolingController:
    def __init__(self):
        self.radiator = Radiator()
        self.temperature_sensor = TemperatureSensor()

    def set_temperature_upper_limit(self, temp):
        print(f"Cooling Controller set temperature upper limit {temp}")
        self.temperature_sensor.get_temperature()

    def run(self):
        print("Cooling Controller run.")
        self.radiator.on()

    def cool(self, cool):
        print(f"Cooling Controller cool{cool}")

    def stop(self):
        print("Cooling Controller stop.")


class CatalyticConverter:
    def on(self):
        print("CatalyticConverter on")

    def off(self):
        print("CatalyticConverter off")


class AirFlowMeter:
    def get_measurement(self):
        print("AirFlowMeter get measurement")


class AirFlowController:
    def __init__(self):
        self.air_flow_meter = AirFlowMeter()

    def take_air(self):
        print("AirFlowController take air.")
        self.air_flow_meter.get_measurement()

    def off(self):
        print("AirFlowController off.")
