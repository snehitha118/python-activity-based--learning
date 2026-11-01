Problem Statement:

Develop a Python program to evaluate a shopping basket containing multiple products and their quantities. The program should calculate the total cost of products, apply discount conditions, compare the final amount with a fixed budget, and determine which purchases must be reduced to remain within the given budget.

Algorithm: 

1. Start the program.
2. Input the total shopping budget.
3. Input the number of products.
4. Initialize the total cost to zero.
5. Create an empty list to store product details.
6. Repeat the following steps for each product:
   - Input the product name.
   - Input the product price.
   - Input the product quantity.
   - Calculate the product cost by multiplying price and quantity.
   - Add the product cost to the total cost.
   - Store the product details in a list.
7. Check whether the total cost is greater than the budget.
8. If the total cost is within the budget, display the shopping details.
9. Otherwise, calculate the excess amount and determine the purchases that can be reduced.

10. ```   mermaid

11. flowchart TD
    A([START]) --> B[/Enter shopping budget/]
    B --> C[/Enter number of products/]
    C --> D[Initialize total cost = 0]
    D --> E[/Enter product name, price and quantity/]
    E --> F[Calculate product cost]
    F --> G[Add product cost to total]
    G --> H{More products?}
    H -- Yes --> E
    H -- No --> I{Total cost >= 2000?}
    I -- Yes --> J[Apply 10 percent discount]
    I -- No --> K[No discount]
    J --> L[Calculate final amount]
    K --> L
    L --> M{Final amount > budget?}
    M -- No --> N[Display shopping details]
    M -- Yes --> O[Reduce product quantities]
    O --> P[Recalculate total and discount]
    P --> M
    N --> Q[Display final cost and remaining budget]
    Q --> R([END])

    ```

    Sample input:

    Enter your shopping budget: 3000
Enter number of products: 3

Product 1
Enter product name: Shoes
Enter product price: 1500
Enter quantity: 1

Product 2
Enter product name: Bag
Enter product price: 1000
Enter quantity: 2

Product 3
Enter product name: Bottle
Enter product price: 300
Enter quantity: 2

Sample output:

MULTI-PRODUCT SHOPPING BUDGET CONSTRAINT

----- SHOPPING DETAILS -----

Shoes Quantity: 1
Bag Quantity: 2
Bottle Quantity: 2

Total Cost: 4100
Discount: 410
Final Amount: 3690

Budget exceeded! Reducing purchases...

----- ADJUSTED SHOPPING LIST -----

Shoes Quantity: 1
Bag Quantity: 1
Bottle Quantity: 0

Final Amount: 2250
Remaining Budget: 750
Thank you for shopping!

    Sample input:
   
