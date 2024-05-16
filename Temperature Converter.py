def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Get user input
celsius = float(input("Enter temperature in Celsius: "))

# Convert temperatures
fahrenheit = celsius_to_fahrenheit(celsius)
kelvin = celsius_to_kelvin(celsius)

# Display the results
print(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")
print(f"Temperature in Kelvin: {kelvin:.2f} K")
