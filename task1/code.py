print("STUDENT PERFORMANCE TREND ANALYSIS")

name = input("Enter student name: ")

n = int(input("Enter number of subjects: "))

total_average = 0
weak_subjects = 0

for i in range(n):
    print("\nSubject", i + 1)

    subject = input("Enter subject name: ")

    test1 = float(input("Enter Test 1 marks: "))
    test2 = float(input("Enter Test 2 marks: "))
    test3 = float(input("Enter Test 3 marks: "))

    average = (test1 + test2 + test3) / 3
    total_average += average

    print("Average marks:", round(average, 2))

    if test3 > test1:
        print("Performance: Improved")
    elif test3 < test1:
        print("Performance: Declined")
    else:
        print("Performance: No Change")

    if test1 < 40 and test2 < 40 and test3 < 40:
        print("Weak Subject:", subject)
        weak_subjects += 1

overall_average = total_average / n

print("\n----- FINAL PERFORMANCE REPORT -----")
print("Student Name:", name)
print("Overall Average:", round(overall_average, 2))
print("Weak Subjects:", weak_subjects)

if overall_average >= 75:
    print("Student Classification: Excellent")
elif overall_average >= 60:
    print("Student Classification: Good")
elif overall_average >= 40:
    print("Student Classification: Average")
else:
    print("Student Classification: Needs Improvement")
