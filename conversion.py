# A Function thta takes Temperature Readings in Celsius and converts it to Fahrenheit.
def CelsiustoFah():
    print("Enter the given Temperature reading in Celsius: ")
    Celsius = float(input())
    conversion = ((Celsius * 9) / 5) + 32 
    print(conversion)
CelsiustoFah()


# Defining a function that takes two arguemets and returns their average.
def Average():
    print("Enter Arguement 1: ")
    arguement1 = int(input())
    print("Enter Arguement 2: ")
    arguement2 = int(input())
    averge_of_arg1_arg2 = (arguement1 + arguement2) / 2
    print(f"The Average of {arguement1} and {arguement2} is {averge_of_arg1_arg2}")
Average()
# Note that an Arguement refers to a value that you pass to a Function when calling it.
# Arguements are specified within the parentheses following the Function and it can be of various types.