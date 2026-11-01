SMART PARKING FEE MANAGEMENT

Problem Statement:

Develop a Python program to calculate parking fees based on vehicle category, entry time, and exit time. The program should calculate parking duration, apply different charges for bikes and cars, handle overnight parking, enforce daily parking limits, and validate time inputs. It should also calculate penalties for invalid parking conditions and display the final parking fee.

Algorithm:

1. Start the program.
2. Input the vehicle category (bike or car).
3. Input the entry hour and exit hour.
4. Validate the entry and exit times (0–23).
5. If the time inputs are invalid, display an error message.
6. If entry and exit times are equal, display that parking duration cannot be zero.
7. Calculate parking duration.
8. If the exit time is earlier than the entry time, consider overnight parking.
9. Calculate parking charges based on vehicle category.
10. Apply the daily parking limit.
11. Calculate the final parking fee.
12. Display the vehicle category, parking duration, and total fee.
13. Stop the program.

```mermaid
flowchart TD
    A([Start]) --> B[Print SMART PARKING FEE MANAGEMENT]
    B --> C[/Enter vehicle category/]
    C --> D[/Enter entry hour and exit hour/]
    D --> E{Entry and exit hours valid?}

    E -->|No| F[Print Invalid time input]
    E -->|Yes| G{Exit time equals entry?}

    G -->|Yes| H[Print Parking duration cannot be zero]
    G -->|No| I{Vehicle is bike or car?}

    I -->|No| J[Print Invalid vehicle category]
    I -->|Yes| K{Exit time less than entry?}

    K -->|Yes| L[Duration = 24 - entry + exit]
    K -->|No| M[Duration = exit - entry]

    L --> N[Print Parking Duration]
    M --> N

    N --> O{Vehicle is bike?}

    O -->|Yes| P[Fee = Duration * 10<br/>Daily limit = 200]
    O -->|No| Q[Fee = Duration * 20<br/>Daily limit = 400]

    P --> R{Fee greater than daily limit?}
    Q --> R

    R -->|Yes| S[Fee = Daily limit]
    R -->|No| T[Keep original fee]

    S --> U[Print Vehicle Category and Total Fee]
    T --> U

    F --> V[Print Thank you]
    H --> V
    J --> V
    U --> V

    V --> W([End])
```



    
Sample input:

SMART PARKING FEE MANAGEMENT

Enter vehicle category (bike/car): car
Enter entry hour (0-23): 20
Enter exit hour (0-23): 5

Sample output:

SMART PARKING FEE MANAGEMENT

Parking Duration: 9 hours
Vehicle Category: car
Total Parking Fee: Rs. 180

Thank you!
