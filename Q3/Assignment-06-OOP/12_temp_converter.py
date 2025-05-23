class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        """Converts Celsius to Fahrenheit"""
        return (c * 9/5) + 32

# Example usage
print(TemperatureConverter.celsius_to_fahrenheit(0))     # 32.0 (freezing point)
print(TemperatureConverter.celsius_to_fahrenheit(100))  # 212.0 (boiling point)
print(TemperatureConverter.celsius_to_fahrenheit(37))   # 98.6 (body temperature)