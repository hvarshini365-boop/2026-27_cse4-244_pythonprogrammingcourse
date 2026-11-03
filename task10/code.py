
# SMART CAMPUS MANAGEMENT SYSTEM

students = []
attendance = []
marks = []
events = []
resources = []

# Function to add student details
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    year = input("Enter Year: ")

    student = [roll, name, dept, year]
    students.append(student)

    print("Student record added successfully!")


# Function to record attendance
def record_attendance():
    roll = input("Enter Roll Number: ")
    total = int(input("Enter Total Working Days: "))
    present = int(input("Enter Present Days: "))

    if total <= 0 or present < 0 or present > total:
        print("Invalid attendance details!")
        return

    percentage = (present / total) * 100

    attendance.append([roll, total, present, percentage])

    print("Attendance recorded successfully!")
    print("Attendance Percentage:", round(percentage, 2), "%")


# Function to enter marks
def enter_marks():
    roll = input("Enter Roll Number: ")

    subject_marks = []

    n = int(input("Enter Number of Subjects: "))

    if n <= 0:
        print("Invalid number of subjects!")
        return

    for i in range(n):
        mark = float(input("Enter mark for subject " + str(i + 1) + ": "))

        if mark < 0 or mark > 100:
            print("Invalid mark! Enter between 0 and 100.")
            return

        subject_marks.append(mark)

    total = sum(subject_marks)
    average = total / n

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    marks.append([roll, subject_marks, total, average, grade])

    print("Marks recorded successfully!")
    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)


# Function for event registration
def event_registration():
    roll = input("Enter Roll Number: ")
    event_name = input("Enter Event Name: ")

    events.append([roll, event_name])

    print("Event registration successful!")


# Function for resource allocation
def allocate_resource():
    roll = input("Enter Roll Number: ")
    resource = input("Enter Resource Name: ")
    time = input("Enter Allocation Time: ")

    # Tuple creation
    allocation = (roll, resource, time)

    resources.append(allocation)

    print("Resource allocated successfully!")


# Function to display student records
def display_students():
    print("\n--- STUDENT RECORDS ---")

    if not students:
        print("No student records available.")
        return

    for student in students:
        roll, name, dept, year = student
        print("Roll No:", roll,
              "| Name:", name,
              "| Department:", dept,
              "| Year:", year)


# Function to generate summary report
def summary_report():
    print("\n========== CAMPUS SUMMARY REPORT ==========")

    print("\nSTUDENT DETAILS:")
    for student in students:
        print(student)

    print("\nATTENDANCE DETAILS:")
    for record in attendance:
        roll, total, present, percentage = record
        print("Roll:", roll,
              "Present:", present,
              "/", total,
              "Percentage:", round(percentage, 2), "%")

    print("\nMARKS DETAILS:")
    for record in marks:
        roll, subject_marks, total, average, grade = record
        print("Roll:", roll,
              "Marks:", subject_marks,
              "Total:", total,
              "Average:", round(average, 2),
              "Grade:", grade)

    print("\nEVENT REGISTRATIONS:")
    for event in events:
        print("Roll:", event[0],
              "Event:", event[1])

    print("\nRESOURCE ALLOCATIONS:")
    for resource in resources:
        roll, name, time = resource
        print("Roll:", roll,
              "Resource:", name,
              "Time:", time)

    print("\n===========================================")


# Main menu-driven program
while True:

    print("\n====== SMART CAMPUS MANAGEMENT SYSTEM ======")
    print("1. Add Student Records")
    print("2. Record Attendance")
    print("3. Enter Student Marks")
    print("4. Event Registration")
    print("5. Resource Allocation")
    print("6. Display Student Records")
    print("7. Campus Summary Report")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        record_attendance()

    elif choice == "3":
        enter_marks()

    elif choice == "4":
        event_registration()

    elif choice == "5":
        allocate_resource()

    elif choice == "6":
        display_students()

    elif choice == "7":
        summary_report()

    elif choice == "8":
        print("Thank you for using Smart Campus Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")

