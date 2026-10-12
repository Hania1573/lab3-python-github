# Python calculator:
while True:
    print("\n--- Available Operations ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Check Even or Odd")
    print("6. Calculate Percentage")
    print("7. Exit")
    
    # 1. Ask the user to choose an operation first
    choice = input("Enter the number of your choice (1-7): ")
    
    if choice == '7':
        print("Thank you for using the calculator. Goodbye!")
        break
        
    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid selection. Please choose a valid operation number.")
        continue

    # 2. Accept number inputs after a valid selection is made
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    # 3. Perform only the requested operation
    if choice == '1':
        c = a + b
        print("Result:", a, "+", b, "=", c)
        
    elif choice == '2':
        d = a - b
        print("Result:", a, "-", b, "=", d)
        
    elif choice == '3':
        e = a * b
        print("Result:", a, "*", b, "=", e)
        
    elif choice == '4':
        # Safely checks for division by zero before dividing
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            f = a / b
            print("Result:", a, "/", b, "=", f)
            
    elif choice == '5':
        if a % 2 == 0:
            print(a ,"is even")
        else:
            print(a ,"is odd")
            
        if b % 2 == 0:
            print(b ,"is even")
        else:
            print(b ,"is odd")
            
    elif choice == '6':
        if b == 0:
            print("Error: Cannot calculate percentage when the second number is 0.")
        else:
            percentage = (a / b) * 100
            print("Percentage of", a, "with respect to", b, "is:", percentage, "%")

    # 4. Ask to restart or end the application loop
    restart_choice = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if restart_choice != "yes":
        print("Thank you for using the calculator. Goodbye!")
        break  
  