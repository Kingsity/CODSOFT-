def basic_calculator():
    print("Welcome to the Basic Calculator!")
    print("You can perform calculations using the following operations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  × : Multiplication")
    print("  ÷ : Division")
    print("Type 'exit' to quit at any time.")

    while True:
        expression = input("\nEnter your calculation: ").replace(" ", "")

        # Exit condition
        if expression.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        # Replace '*' with '×' for multiplication consistency
        expression = expression.replace('*', '×')

        # Parse the expression
        try:
            if '+' in expression:
                num1, num2 = expression.split('+')
                operator = '+'
            elif '-' in expression:
                num1, num2 = expression.split('-')
                operator = '-'
            elif '×' in expression:
                num1, num2 = expression.split('×')
                operator = '×'
            elif '÷' in expression or '/' in expression:
                num1, num2 = expression.replace('/', '÷').split('÷')
                operator = '÷'
            else:
                print("Error: Invalid expression. Please use +, -, ×, or ÷.")
                continue

            # Convert inputs to float
            num1 = float(num1)
            num2 = float(num2)

            # Perform the calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '×':
                result = num1 * num2
            elif operator == '÷':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2

            print(f"Result: {result}")
        
        except ValueError:
            print("Error: Please enter a valid mathematical expression.")

        # Confirmation prompt
        continue_prompt = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if continue_prompt != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

# Run the calculator
basic_calculator()