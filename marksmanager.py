
students = {
    "Aman": [85, 90, 78],
    "Riya": [92, 88, 95],
    "Zoya": [70, 65, 80]
}

# Stage 1, 2 and 3: Average, Grade and Topper

while True:
    print("\n1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists.")
        else:
            marks = []

            while len(marks) < 3:
                mark = float(input("Enter marks: "))

                if mark >= 0 and mark <= 100:
                    marks.append(mark)
                else:
                    print("Invalid mark, try again.")

            students[name] = marks
            print("Student added successfully.")

    elif choice == "2":
        for name in students:
            marks = students[name]
            average = sum(marks) / len(marks)
            average = round(average, 2)

            if average >= 85:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 50:
                grade = "C"
            else:
                grade = "F"

            print(name, average, grade)

    elif choice == "3":
        topper = ""
        highest_average = -1

        for name in students:
            average = sum(students[name]) / len(students[name])

            if average > highest_average:
                highest_average = average
                topper = name

        print("Topper:", topper)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")