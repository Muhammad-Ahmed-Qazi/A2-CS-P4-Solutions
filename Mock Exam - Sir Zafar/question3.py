# 3a
class SmartDevice:
    # PRIVATE name : STRING
    # PRIVATE type : STRING
    # PRIVATE serial_number : STRING
    # PRIVATE setup_year : STRING
    # PRIVATE is_on : BOOLEAN

    def __init__(self, name, type, serial_number, setup_year, is_on):
        self.__name = name
        self.__type = type
        self.__serial_number = serial_number
        self.__setup_year = setup_year
        self.__is_on = is_on
    
    def GetName(self): return self.__name
    def SetName(self, name): self.__name = name

    def GetType(self): return self.__type
    def SetType(self, type): self.__type = type

    def GetSerialNum(self): return self.__serial_number
    def SetSerialNum(self, serial_number): self.__serial_number = serial_number

    def GetSetupYear(self): return self.__setup_year
    def SetSetupYear(self, setup_year): self.__setup_year = setup_year

    def GetStatus(self): return self.__is_on
    def SetStatus(self, is_on): self.__is_on = is_on

    def is_device_on(self):
        if self.__is_on:
            print("Device is on.")
        else:
            print("Device is off.")
    
    def get_age_in_years(self):
        return 2024 - int(self.__setup_year)
    
    def turn_on(self): self.__is_on = True
    def turn_off(self): self.__is_on = False

# 3b
class SmartLight(SmartDevice):
    # PRIVATE brightness : INTEGER

    def __init__(self, name, type, serial_number, setup_year, is_on, brightness):
        super().__init__(name, type, serial_number, setup_year, is_on)
        self.__brightness = brightness
    
    def GetBrightness(self): return self.__brightness

    def set_brightness(self, brightness): self.__brightness = brightness

class SmartThermostat(SmartDevice):
    # PRIVATE temperature : INTEGER

    def __init__(self, name, type, serial_number, setup_year, is_on, temperature):
        super().__init__(name, type, serial_number, setup_year, is_on)
        self.__temperature = temperature

    def GetTemperature(self): return self.__temperature
    
    def set_temperature(self, temperature): self.__temperature = temperature

    def suggest_temperature(self, season):
        if season.lower() == "winter": self.__temperature = 20
        elif season.lower() == "summer": self.__temperature = 25
        else:
            self.__temperature = 22

# 2c
SmartLightObj = SmartLight("Living Room Light", "light", "LR001", "2024", False, 0)
SmartLightObj.turn_on()
SmartLightObj.set_brightness(75)
SmartLightObj.set_brightness(50)
SmartLightObj.turn_off()

SmartThermostatObj = SmartThermostat("Main Thermostat", "thermostat", "MT001", "2024", True, 68)
SmartThermostatObj.set_temperature(70)
SmartThermostatObj.suggest_temperature("winter")

SmartLightObj = SmartLight("Living Room Light", "light", "LR002", "2024", False, 0)
SmartThermostatObj = SmartThermostat("Home Thermostat", "thermostat", "HT0010", "2024", True, 68)

print("Morning 7:00 AM")
SmartLightObj.turn_on()
SmartLightObj.set_brightness(60)
SmartThermostatObj.set_temperature(70)
print(f"Light is {SmartLightObj.is_device_on()} and set to {SmartLightObj.GetBrightness}% brightness.")
print(f"Thermostat is {SmartThermostatObj.is_device_on()} and set to {SmartThermostatObj.GetTemperature()}F temperature.")

print("Day 9:00 AM to 5:00 PM")
SmartLightObj.turn_off()
SmartThermostatObj.set_temperature(68)
print(f"Light is {SmartLightObj.is_device_on()} and set to {SmartLightObj.GetBrightness}% brightness.")
print(f"Thermostat is {SmartThermostatObj.is_device_on()} and set to {SmartThermostatObj.GetTemperature()}F temperature.")

print("Evening 6:00 PM")
SmartLightObj.turn_on()
SmartLightObj.set_brightness(70)
SmartThermostatObj.set_temperature(72)
print(f"Light is {SmartLightObj.is_device_on()} and set to {SmartLightObj.GetBrightness}% brightness.")
print(f"Thermostat is {SmartThermostatObj.is_device_on()} and set to {SmartThermostatObj.GetTemperature()}F temperature.")

print("Night 10:00 PM")
SmartLightObj.turn_off()
SmartThermostatObj.set_temperature(65)
print(f"Light is {SmartLightObj.is_device_on()} and set to {SmartLightObj.GetBrightness}% brightness.")
print(f"Thermostat is {SmartThermostatObj.is_device_on()} and set to {SmartThermostatObj.GetTemperature()}F temperature.")