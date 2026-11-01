STUDENT PERFORMANCE TREND ANALYSIS

1.Problem statement:

Develop a Python program to analyze student performance by comparing their assessment scores across multiple examinations. The program should calculate the improvement or decline in marks, identify consistently weak subjects, and classify students based on their performance criteria.


2. Algorithm:

Start the program.

Enter the student's name.

Enter the number of subjects.

Enter subject names and marks for three examinations.

Calculate the average marks for each subject.

Compare marks between the first and third examinations.

Calculate the improvement or decline in marks.

Identify subjects with consistently low marks.

Calculate the overall average percentage.

Classify the student based on the overall percentage.

Display the performance analysis.

Stop the program.

``` mermaid
3.Flowchart:
    A([START]) --> B[/Enter student name/]
    B --> C[/Enter number of subjects/]
    C --> D[Initialize total average and weak subjects]
    D --> E[/Enter subject name and marks in 3 tests/]
    E --> F[Calculate subject average]
    F --> G{Test 3 > Test 1?}
    G -- Yes --> H[Display Improved]
    G -- No --> I{Test 3 < Test 1?}
    I -- Yes --> J[Display Declined]
    I -- No --> K[Display No Change]
    H --> L{All 3 marks below 40?}
    J --> L
    K --> L
    L -- Yes --> M[Identify weak subject]
    L -- No --> N[Continue]
    M --> N
    N --> O{More subjects?}
    O -- Yes --> E
    O -- No --> P[Calculate overall average]
    P --> Q{Average >= 75?}
    Q -- Yes --> R[Excellent]
    Q -- No --> S{Average >= 60?}
    S -- Yes --> T[Good]
    S -- No --> U{Average >= 40?}
    U -- Yes --> V[Average]
    U -- No --> W[Needs Improvement]
    R --> X[Display final performance report]
    T --> X
    V --> X
    W --> X
    X --> Y([END])

```

4.Sample input:

Enter student name: Sita
Enter number of subjects: 2

Subject 1
Enter subject name: Python
Enter Test 1 marks: 50
Enter Test 2 marks: 65
Enter Test 3 marks: 80

Subject 2
Enter subject name: Maths
Enter Test 1 marks: 30
Enter Test 2 marks: 25
Enter Test 3 marks: 20

5.Sample output:

STUDENT PERFORMANCE TREND ANALYSIS

Average marks: 65.0
Performance: Improved

Average marks: 25.0
Performance: Declined
Weak Subject: Maths

----- FINAL PERFORMANCE REPORT -----
Student Name: Sita
Overall Average: 45.0
Weak Subjects: 1
Student Classification: Average

