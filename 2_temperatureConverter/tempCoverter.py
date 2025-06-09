ogTemp = int(input("Enter initial Temperature: "))
unit = input("Enter original unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
conv = input("Convert to new unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
if unit == 'C':
    if conv == 'F':
        newTemp = 9/5 * ogTemp + 32
    elif conv == 'K':
        newTemp = ogTemp + 273.15
    else:
        newTemp = ogTemp
elif unit == 'F':
    if conv == 'C':
        newTemp = (ogTemp - 32) * 5/9
    elif conv == 'K':
        newTemp = (ogTemp - 32) * 5/9 + 273.15
    else:
        newTemp = ogTemp
elif unit == 'K':
    if conv == 'C':
        newTemp = ogTemp - 273.15
    elif conv == 'F':
        newTemp = (ogTemp - 273.15) * 9/5 + 32
    else:
        newTemp = ogTemp
else:
    print("Invalid unit")

newTemp = round(newTemp, 2)
print(ogTemp, unit, "is", newTemp, conv)