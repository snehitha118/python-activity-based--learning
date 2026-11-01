
print("ADVANCED NUMERIC PATTERN GENERATOR")
print("-----------------------------------")

print("1. Hollow Diamond")
print("2. Symmetric Number Pattern")

choice = input("Enter your choice: ")

try:
    rows = int(input("Enter number of rows: "))

  
    if rows <= 0 or rows % 2 == 0:
        print("\nInvalid dimension!")
        print("Please enter a positive odd integer.")

    elif choice == "1":
        print("\nHOLLOW DIAMOND PATTERN\n")

        
        for i in range(rows // 2 + 1):
            print(" " * (rows // 2 - i), end="")

            if i == 0:
                print("*")
            else:
                print("*" + " " * (2 * i - 1) + "*")

       
        for i in range(rows // 2 - 1, -1, -1):
            print(" " * (rows // 2 - i), end="")

            if i == 0:
                print("*")
            else:
                print("*" + " " * (2 * i - 1) + "*")

    elif choice == "2":
        print("\nSYMMETRIC NUMBER PATTERN\n")

        for i in range(1, rows + 1):
            print("  " * (rows - i), end="")

            
            for j in range(1, i + 1):
                print(j, end=" ")

            
            for j in range(i - 1, 0, -1):
                print(j, end=" ")

            print()

    else:
        print("\nInvalid pattern choice!")
        print("Please select 1 or 2.")

except ValueError:
    print("\nInvalid input! Please enter a valid integer.")
    
print("\nThank you!")

