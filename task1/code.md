1.	Problem Statement:
The aim of this project is to analyze a student's performance in three tests. The program accepts the student's name and marks in three tests, calculates the average marks, identifies the performance trend as improving, declining, or stable, and displays the overall result.

2.Algorithm:

Step 1: Start the program.

Step 2: Enter the student's name.

Step 3: Enter marks in Test 1, Test 2, and Test 3.

Step 4: Calculate the average marks.

Step 5: Display the student's name, marks, and average.

Step 6: Compare Test 3 marks with Test 1 marks.

Step 7: Display Improving, Declining, or Stable.

Step 8: Classify the result as Excellent, Good, or Needs Improvement.

Step 9: Stop the program

``` mermaid
flowchart TD
    A([START]) --> B[/Input marks for Test 1, Test 2, Test 3/]
    B --> C[Calculate average marks]
    C --> D[Compare marks of all tests]
    D --> E{Are marks increasing?}
    E -- Yes --> F[Display Improving Performance]
    E -- No --> G{Are marks decreasing?}
    G -- Yes --> H[Display Declining Performance]
    G -- No --> I[Display Stable Performance]
    F --> J[Display Average Marks]
    H --> J
    I --> J
    J --> K([END])

```



   

4.Sample input:

Enter marks for Test 1: 60

Enter marks for Test 2: 70

Enter marks for Test 3: 80

5.Sample output:

Student Performance Trend Analysis

Test 1 Marks: 60

Test 2 Marks: 70

Test 3 Marks: 80

Average Marks: 70.0

Performance Trend: Improving



