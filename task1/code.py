print("STUDENT PERFORMANCE TREND ANALYSIS")

name = input("Enter student name: ")

marks1 = float(input("Enter marks in Test 1: "))
marks2 = float(input("Enter marks in Test 2: "))
marks3 = float(input("Enter marks in Test 3: "))

average = (marks1 + marks2 + marks3) / 3

print("\n----- PERFORMANCE REPORT -----")
print("Student Name:", name)
print("Test 1 Marks:", marks1)
print("Test 2 Marks:", marks2)
print("Test 3 Marks:", marks3)
print("Average Marks:", round(average, 2))

if marks3 > marks1:
    print("Performance Trend: Improving")
elif marks3 < marks1:
    print("Performance Trend: Declining")
else:
    print("Performance Trend: Stable")

if average >= 75:
    print("Overall Result: Excellent")
elif average >= 50:
    print("Overall Result: Good")
else:
    print("Overall Result: Needs Improvement")
