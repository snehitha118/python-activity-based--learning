
print("SMART CANTEEN ORDER AND STOCK MANAGEMENT")
print("-----------------------------------------")


menu = {
    "idli": {"price": 30, "stock": 20},
    "dosa": {"price": 50, "stock": 15},
    "fried rice": {"price": 80, "stock": 10},
    "burger": {"price": 60, "stock": 12}
}

total_sales = 0
successful_orders = 0
total_customers = 0

try:
    
    print("\nAVAILABLE FOOD MENU")
    print("-----------------------------------------")

    for item, details in menu.items():
        print(item.title(), "- Rs.", details["price"],
              "- Stock:", details["stock"])

    customers = int(input("\nEnter number of customers: "))

    if customers <= 0:
        raise ValueError("Number of customers must be positive.")

    total_customers = customers

   
    for i in range(customers):

        print("\nCUSTOMER", i + 1)
        bill = 0
        has_successful_item = False

        items = int(input("Enter number of items: "))

        if items < 0:
            raise ValueError("Number of items cannot be negative.")

        for j in range(items):

            print("\nItem", j + 1)

            name = input("Enter food item: ").lower().strip()

            if name not in menu:
                print("Invalid food item!")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Invalid quantity! Enter a positive number.")
                continue

            
            if quantity > menu[name]["stock"]:
                print("\nORDER REJECTED!")
                print("Requested quantity:", quantity)
                print("Available stock:", menu[name]["stock"])
                print("Insufficient stock!")
                continue

            
            price = menu[name]["price"]
            cost = price * quantity

            bill += cost
            menu[name]["stock"] -= quantity
            has_successful_item = True

            print("Item:", name.title())
            print("Quantity:", quantity)
            print("Item Cost: Rs.", cost)
            print("Order Successful!")


        print("\nCUSTOMER", i + 1, "BILL")
        print("-----------------------------------------")
        print("Total Bill: Rs.", bill)

        if has_successful_item:
            successful_orders += 1
            total_sales += bill
            print("Order Status: SUCCESSFUL")
        else:
            print("Order Status: UNSUCCESSFUL")

   
    print("\n=========================================")
    print("DAILY SALES SUMMARY")
    print("=========================================")

    print("Total Customers:", total_customers)
    print("Successful Customer Orders:", successful_orders)
    print("Total Daily Sales: Rs.", total_sales)

   
    print("\nREMAINING STOCK")
    print("-----------------------------------------")
    print("Food Item          Remaining Stock")

    for item, details in menu.items():
        print(f"{item.title():<20}{details['stock']}")

    print("\n=========================================")
    print("CANTEEN MANAGEMENT COMPLETED!")
    print("Thank You!")

except ValueError as e:
    print("\nInvalid Input:", e)

