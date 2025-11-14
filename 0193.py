class TemperatureChecker:
    def __init__(self, current_temp):
        self.current_temp = current_temp
        
    def check_temperature(self):
        if self.current_temp > 30:
            print(f"{self.current_temp}°C: Hot weather! Stay hydrated.")
        elif self.current_temp > 20:
            print(f"{self.current_temp}°C: Pleasant weather! Enjoy outdoors.")
        elif self.current_temp > 10:
            print(f"{self.current_temp}°C: Cool weather! Wear jacket.")
        else:
            print(f"{self.current_temp}°C: Cold weather! Stay warm.")
            
# Test
temp1 = TemperatureChecker(25)
temp2 = TemperatureChecker(5)
temp1.check_temperature()
temp2.check_temperature()