import random as r

class Sensor:
    """Base sensor class."""
    def __init__(self, name: str) -> None:
        self.name = name

    def read(self) -> float:
        return 0.0  # to overwrite...


class TemperatureSensor(Sensor):
    """Simulated temperature sensor."""
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def read(self) -> float:  # overwritten sensor.read()
        return round(r.uniform(20.0, 30.0), 2)


class LightSensor(Sensor):
    """Simulated light sensor."""
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def read(self) -> float:
        return round(r.uniform(0, 100), 2)



