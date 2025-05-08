def basic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Undefined"
    
    return {
        "addition": addition,
        "subtraction": subtraction,
        "multiplication": multiplication,
        "division": division
    }

if __name__ == "__main__":
    a = 10
    b = 5
    results = basic_operations(a, b)
    
    for operation, result in results.items():
        print(f"{operation.capitalize()}: {result}")
