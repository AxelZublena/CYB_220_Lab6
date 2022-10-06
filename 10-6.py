# 10.6
try:
    num1 = int(input("Provide the first number: "))
    num2 = int(input("Provide the second number: "))
    
    print(f"{num1} + {num2} = {num1 + num2}")
except ValueError:
    print("Only numbers are accepted.")
