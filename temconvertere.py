def temp_converter():
    print("--- Temperature Converter ---")
    celsius = float(input("Celsius e temperature koto? "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C mane holo {fahrenheit}°F. Gorom koto dekhle?")

temp_converter()
