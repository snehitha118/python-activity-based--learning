
print("EXAMINATION QUESTION DIFFICULTY AND PERFORMANCE ANALYSIS")
print("---------------------------------------------------------")

try:
    students = int(input("Enter number of students: "))
    questions = int(input("Enter number of questions: "))

    if students <= 0 or questions <= 0:
        raise ValueError("Students and questions must be positive.")

    
    key = input("Enter correct answer key: ").upper().strip()

    if len(key) != questions or any(ch not in "ABCD" for ch in key):
        raise ValueError("Answer key must contain exactly "
                         "the required number of A, B, C or D answers.")

    correct = [0] * questions
    incorrect = [0] * questions
    total_correct = 0

 
    for i in range(students):
        answer = input(
            "Enter answers of Student " + str(i + 1) + ": "
        ).upper().strip()

        if len(answer) != questions or any(ch not in "ABCD" for ch in answer):
            raise ValueError("Invalid answer string! "
                             "Enter exactly " + str(questions) +
                             " answers using A, B, C or D.")

  
        for j in range(questions):
            if answer[j] == key[j]:
                correct[j] += 1
                total_correct += 1
            else:
                incorrect[j] += 1

   
    success_rates = []

    print("\nEXAMINATION PERFORMANCE ANALYSIS REPORT")
    print("-" * 65)
    print("Q.No   Correct   Incorrect   Success Rate   Difficulty")
    print("-" * 65)

    easy = 0
    moderate = 0
    difficult = 0

    for i in range(questions):
        rate = (correct[i] / students) * 100
        success_rates.append(rate)

        if rate >= 75:
            level = "Easy"
            easy += 1
        elif rate >= 40:
            level = "Moderate"
            moderate += 1
        else:
            level = "Difficult"
            difficult += 1

        print(
            f"Q{i+1:<5}{correct[i]:<10}{incorrect[i]:<12}"
            f"{rate:<15.2f}{level}"
        )

    print("-" * 65)

   
    maximum = max(incorrect)

    print("\nMOST FREQUENTLY MISSED QUESTIONS:")

    if maximum == 0:
        print("No questions were answered incorrectly.")
    else:
        for i in range(questions):
            if incorrect[i] == maximum:
                print("Q", i + 1, "-", incorrect[i],
                      "incorrect answers")

    
    print("\nDIFFICULTY SUMMARY")
    print("Easy Questions:", easy)
    print("Moderate Questions:", moderate)
    print("Difficult Questions:", difficult)


    total_possible = students * questions
    overall_rate = (total_correct / total_possible) * 100

    print("\nOVERALL PERFORMANCE")
    print("Total Correct Answers:", total_correct)
    print("Total Possible Answers:", total_possible)
    print("Overall Success Rate:", round(overall_rate, 2), "%")

    print("\nThank You!")

except ValueError as e:
    print("\nInvalid Input:", e)

