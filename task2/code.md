ATM TRANSACTION SEQUENCE SIMULATION


1. Problem Statement:

Develop a Python program to process a sequence of deposits and withdrawals in a simulated bank account. The program should maintain the account balance, enforce withdrawal limits, reject invalid transactions, and generate a transaction summary.

2.Algorithm:

1. Start the program.
2. Input the initial account balance.
3. Input the withdrawal limit.
4. Input the sequence of deposit and withdrawal transactions.
5. Initialize the successful and rejected transaction counters to zero.
6. Process each transaction in the sequence.
7. If the transaction is a deposit, check whether the amount is greater than zero.
8. If the deposit amount is valid, add it to the account balance and increase the successful transaction counter. Otherwise, reject it and increase the rejected transaction counter.
9. If the transaction is a withdrawal, check whether the amount is positive, does not exceed the withdrawal limit, and is within the available balance.
10. If the withdrawal is valid, subtract the amount from the account balance and increase the successful transaction counter. Otherwise, reject it and increase the rejected transaction counter.
11. Repeat until all transactions have been processed.
12. Display the successful transactions, rejected transactions, and final account balance.
13. Stop the program.

14. 
