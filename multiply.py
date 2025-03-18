def multiply_numbers(num1: float, num2: float) -> float:
    """Returns the product of two numbers."""
    return num1 * num2

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = multiply_numbers(num1, num2)
        print(f"✅ The product is: {result}")
    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
