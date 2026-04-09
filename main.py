from Sensor import TemperatureSensor, LightSensor

temp = TemperatureSensor("Temp1")
light = LightSensor("Light1")

print(f"Temp: {temp.read()} °C")
print(f"Light: {light.read()} %")
