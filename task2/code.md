ATM TRANSACTION SIMULATION

Problem Statement: 

Develop a Python program to simulate ATM transactions by processing a sequence of deposits and withdrawals. The program should maintain the account balance, enforce withdrawal limits, reject invalid transactions, and generate a transaction summary showing the number of successful and rejected transactions along with the final account balance.

Algorithm: 


1. Start the program.
2. Input the initial account balance.
3. Input the withdrawal limit.
4. Input the number of transactions.
5. Initialize successful and rejected transaction counters to zero.
6. Repeat the following steps for each transaction:
   - Input the transaction type (deposit or withdrawal).
   - Input the transaction amount.
   - Check whether the amount is greater than zero.
   - If the amount is invalid, reject the transaction.
   - If the transaction type is deposit, add the amount to the account balance.
   - If the transaction type is withdrawal, check the withdrawal limit and available balance.
   - If both conditions are satisfied, subtract the amount from the balance.
   - Otherwise, reject the transaction.
7. Update the successful and rejected transaction counters.
8. Display the final account balance.

9. ``` mermaid

   flowchart TD
    A([START]) --> B[/Input initial balance/]
    B --> C[/Input withdrawal limit/]
    C --> D[/Input number of transactions/]
    D --> E[Initialize counters to zero]
    E --> F[/Input transaction type and amount/]
    F --> G{Is amount greater than zero?}
    G -- No --> H[Reject transaction]
    G -- Yes --> I{Transaction type?}
    I -- Deposit --> J[Add amount to balance]
    I -- Withdrawal --> K{Within withdrawal limit?}
    K -- No --> H
    K -- Yes --> L{Sufficient balance?}
    L -- No --> H
    L -- Yes --> M[Subtract amount from balance]
    J --> N[Increment successful count]
    M --> N
    H --> O[Increment rejected count]
    N --> P{More transactions?}
    O --> P
    P -- Yes --> F
    P -- No --> Q[/Display final balance and counts/]
    Q --> R([END])

   ```

   Sample input:

   Enter initial balance: 10000
Enter withdrawal limit: 5000
Enter number of transactions: 5

Transaction 1
Enter transaction type: deposit
Enter amount: 2000

Transaction 2
Enter transaction type: withdrawal
Enter amount: 1000

Transaction 3
Enter transaction type: withdrawal
Enter amount: 6000

Transaction 4
Enter transaction type: deposit
Enter amount: 0

Transaction 5
Enter transaction type: withdrawal
Enter amount: 500


   Sample output:

   ATM TRANSACTION SIMULATION

Transaction 1
Deposit successful

Transaction 2
Withdrawal successful

Transaction 3
Withdrawal limit exceeded

Transaction 4
Invalid amount

Transaction 5
Withdrawal successful

----- ATM TRANSACTION SUMMARY -----

Final Balance: 10500.0
Successful Transactions: 3
Rejected Transactions: 2

Thank you for using ATM
10. Display the total successful and rejected transactions.
11. Stop the program.
