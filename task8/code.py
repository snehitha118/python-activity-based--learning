
print("UNIVERSITY HOSTEL ROOM ALLOCATION SYSTEM")
print("----------------------------------------")

try:
    students = []
    rooms = []

  
    n = int(input("Enter number of students: "))

    if n <= 0:
        raise ValueError("Number of students must be positive.")

    print("\nENTER STUDENT DETAILS")

    student_ids = set()

    for i in range(n):
        print("\nStudent", i + 1)

        sid = input("Enter Student ID: ").strip()

        if not sid or sid in student_ids:
            print("Duplicate or invalid Student ID!")
            continue

        name = input("Enter Student Name: ").strip()
        gender = input("Enter Gender (Male/Female): ").strip().lower()
        group = input("Enter Group ID: ").strip()

        if not name or not group or gender not in ["male", "female"]:
            print("Invalid student details!")
            continue

        student_ids.add(sid)

        students.append({
            "id": sid,
            "name": name,
            "gender": gender,
            "group": group,
            "allocated": False
        })


    r = int(input("\nEnter number of rooms: "))

    if r <= 0:
        raise ValueError("Number of rooms must be positive.")

    print("\nENTER ROOM DETAILS")

    room_numbers = set()

    for i in range(r):
        print("\nRoom", i + 1)

        number = input("Enter Room Number: ").strip()

        if not number or number in room_numbers:
            print("Duplicate or invalid room number!")
            continue

        capacity = int(input("Enter Room Capacity: "))
        gender = input(
            "Enter Eligible Gender (Male/Female): "
        ).strip().lower()

        if capacity <= 0 or gender not in ["male", "female"]:
            print("Invalid room details!")
            continue

        room_numbers.add(number)

        rooms.append({
            "number": number,
            "capacity": capacity,
            "gender": gender,
            "allocated": []
        })

 
    groups = {}

    for student in students:
        groups.setdefault(student["group"], []).append(student)

    for group_name, members in groups.items():

        if all(s["allocated"] for s in members):
            continue

      
        genders = set(s["gender"] for s in members)

        if len(genders) != 1:
            continue

        required_gender = members[0]["gender"]
        required_capacity = len(members)

      
        for room in rooms:

            available = (
                room["capacity"] - len(room["allocated"])
            )

            if (room["gender"] == required_gender
                    and available >= required_capacity):

                for student in members:
                    if student["allocated"]:
                        print(
                            "Warning: Duplicate assignment prevented:",
                            student["id"]
                        )
                        break

                else:
                    for student in members:
                        room["allocated"].append(student)
                        student["allocated"] = True

                break

  
    print("\n\nHOSTEL ROOM ALLOCATION REPORT")
    print("=" * 50)

    for room in rooms:
        print("\nRoom Number:", room["number"])
        print("Eligible Gender:", room["gender"].capitalize())
        print("Room Capacity:", room["capacity"])

        print("Allocated Students:")

        if room["allocated"]:
            for student in room["allocated"]:
                print(
                    student["id"], "-", student["name"],
                    "(Group", student["group"] + ")"
                )
        else:
            print("No students allocated")

        vacancies = room["capacity"] - len(room["allocated"])
        print("Available Vacancies:", vacancies)

  
    unallocated = [
        s for s in students if not s["allocated"]
    ]

    allocated_count = len(students) - len(unallocated)

    print("\n" + "=" * 50)
    print("TOTAL STUDENTS:", len(students))
    print("ALLOCATED STUDENTS:", allocated_count)
    print("UNALLOCATED STUDENTS:", len(unallocated))

    print("\nUNALLOCATED STUDENT DETAILS:")

    if unallocated:
        for student in unallocated:
            print(
                student["id"], "-", student["name"],
                "(Group", student["group"] + ")"
            )
    else:
        print("All students received rooms.")

    print("\nTOTAL AVAILABLE VACANCIES:",
          sum(room["capacity"] - len(room["allocated"])
              for room in rooms))

    print("\nHOSTEL ALLOCATION COMPLETED!")
    print("Thank You!")

except ValueError as e:
    print("\nInvalid Input:", e)

