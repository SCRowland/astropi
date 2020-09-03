from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# throwaway first measurement
sense.get_pressure()
sense.get_temperature()
sense.get_humidity()

pressure = sense.get_pressure()
temp = sense.get_temperature()
humidity = sense.get_humidity()

print(f"Pressure: {pressure}, Temp: {temp}, Humidity: {humidity}")
sense.show_message("Hello world")