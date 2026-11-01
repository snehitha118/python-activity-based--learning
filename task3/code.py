print("MULTI-PRODUCT SHOPPING BUDGET CONSTRAINT")

budget = float(input("Enter your shopping budget: "))
n = int(input("Enter number of products: "))

products = []
total_cost = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    cost = price * quantity
    total_cost += cost

    products.append([name, price, quantity])

print("\n----- SHOPPING DETAILS -----")

for product in products:
    print(product[0], "Quantity:", product[2])

print("Total Cost:", total_cost)

# Apply discount
if total_cost >= 2000:
    discount = total_cost * 0.10
else:
    discount = 0

final_amount = total_cost - discount

print("Discount:", discount)
print("Final Amount:", final_amount)

# Reduce quantities if budget is exceeded
if final_amount > budget:

    print("\nBudget exceeded! Reducing purchases...")

    index = len(products) - 1

    while final_amount > budget and index >= 0:

        while products[index][2] > 0 and final_amount > budget:

            products[index][2] -= 1

            total_cost = 0

            for product in products:
                total_cost += product[1] * product[2]

            if total_cost >= 2000:
                discount = total_cost * 0.10
            else:
                discount = 0

            final_amount = total_cost - discount

        index -= 1

    print("\n----- ADJUSTED SHOPPING LIST -----")

    for product in products:
        print(product[0], "Quantity:", product[2])

    print("Final Amount:", final_amount)

else:
    print("\nShopping is within budget.")

print("Remaining Budget:", budget - final_amount)
print("Thank you for shopping!")
