# A Function thta takes Temperature Readings in Celsius and converts it to Fahrenheit.
def CelsiustoFah():
    print("Enter the given Temperature reading in Celsius: ")
    Celsius = float(input())
    conversion = ((Celsius * 9) / 5) + 32 
    print(conversion)
CelsiustoFah()

