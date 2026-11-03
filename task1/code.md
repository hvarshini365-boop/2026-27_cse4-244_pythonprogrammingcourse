# University Scholarship Allocation System Using Python

## 1. Problem Statement

Design and develop a University Scholarship Allocation System using Python to evaluate and rank students based on their academic performance and financial background.

The system should consider the following criteria:

1. Aggregate Marks: The student must obtain at least 75% aggregate marks.
2. Subject-wise Minimum Marks: The student must score at least 60 marks in each subject.
3. Attendance: The student must have at least 75% attendance.
4. Family Income: The annual family income must not exceed ₹3,00,000.

The system should:

- Accept student details as input.
- Check whether each student satisfies all eligibility conditions.
- Rank eligible students based on aggregate marks.
- Resolve ties using predefined rules:
  1. Higher aggregate marks.
  2. Higher attendance percentage.
  3. Lower annual family income.
  4. Higher total subject marks.
- Display the eligible students in ranked order.
- Display rejected students with their reasons for rejection.

## 2. Algorithm

Step 1: Start the program.

Step 2: Read the number of students.

Step 3: For each student, input:

- Student name
- Roll number
- Marks in each subject
- Attendance percentage
- Annual family income

Step 4: Calculate aggregate percentage.

$$
Aggregate = \frac{Total\ Marks}{Maximum\ Marks}\times100
$$

Step 5: Check eligibility conditions:

- Aggregate percentage ≥ 75%.
- Each subject mark ≥ 60.
- Attendance ≥ 75%.
- Annual family income ≤ ₹3,00,000.

Step 6: If all conditions are satisfied, add the student to the eligible list.

Step 7: Otherwise, display the reason for rejection.

Step 8: Sort eligible students using the following priority:

1. Aggregate percentage in descending order.
2. Attendance percentage in descending order.
3. Annual family income in ascending order.
4. Total subject marks in descending order.

Step 9: Assign ranks to eligible students.

Step 10: Display the scholarship allocation results.

Step 11: Stop the program.

## 3. Flowchart

3.2 Algorithms - IB Questionbank | RevisionDojo

[revisiondojo.com](<https://www.revisiondojo.com/ib/ib-digital-society/3-2-algorithms/questionbank?utm_source=chatgpt.com>)

Flowchart explanation:

- Start the program.
- Enter student details.
- Calculate aggregate marks.
- Check academic, attendance, and income eligibility.
- If eligible, add the student to the eligible list.
- Otherwise, record the rejection reason.
- Sort eligible students based on tie-breaking rules.
- Display student ranks and results.
- End the program.

## 4. Python Source Code

python

```python

# University Scholarship Allocation System

students = []
eligible_students = []
rejected_students = []

# Scholarship eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 300000

# Number of students
n = int(input("Enter number of students: "))

# Input student details
for i in range(n):
    print("\nEnter details of Student", i + 1)

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    marks = []
    for j in range(3):
        mark = int(input(f"Enter marks in Subject {j + 1}: "))
        marks.append(mark)

    attendance = float(input("Enter Attendance Percentage: "))
    income = float(input("Enter Annual Family Income: "))

    total = sum(marks)
    aggregate = (total / 300) * 100

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks,
        "total": total,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income
    }

    # Eligibility checking
    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate below 75%")

    if min(marks) < MIN_SUBJECT_MARK:
        reasons.append("Subject mark below 60")

    if attendance < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if income > MAX_INCOME:
        reasons.append("Family income exceeds Rs. 300000")

    if len(reasons) == 0:
        eligible_students.append(student)
    else:
        student["reason"] = reasons
        rejected_students.append(student)


# Ranking eligible students
# Priority:
# 1. Higher aggregate
# 2. Higher attendance
# 3. Lower family income
# 4. Higher total marks

eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        -s["total"]
    )
)

# Display eligible students
print("\n========== SCHOLARSHIP ELIGIBLE STUDENTS ==========")

if eligible_students:
    print("Rank  Roll No  Name  Aggregate  Attendance  Income")

    for rank, s in enumerate(eligible_students, start=1):
        print(
            rank,
            s["roll_no"],
            s["name"],
            f"{s['aggregate']:.2f}%",
            f"{s['attendance']}%",
            s["income"]
        )
else:
    print("No eligible students found.")

# Display rejected students
print("\n========== REJECTED STUDENTS ==========")

if rejected_students:
    for s in rejected_students:
        print("\nName:", s["name"])
        print("Roll Number:", s["roll_no"])
        print("Reason(s):", ", ".join(s["reason"]))
else:
    print("No rejected students.")

print("\nScholarship allocation process completed.")
```

## 5. Sample Input

Consider the following sample data with three subjects, each carrying 100 marks.

text

```text
Enter number of students: 5

Enter details of Student 1
Enter Roll Number: 101
Enter Student Name: Arun
Enter marks in Subject 1: 90
Enter marks in Subject 2: 85
Enter marks in Subject 3: 95
Enter Attendance Percentage: 90
Enter Annual Family Income: 200000

Enter details of Student 2
Enter Roll Number: 102
Enter Student Name: Banu
Enter marks in Subject 1: 80
Enter marks in Subject 2: 85
Enter marks in Subject 3: 90
Enter Attendance Percentage: 95
Enter Annual Family Income: 250000

Enter details of Student 3
Enter Roll Number: 103
Enter Student Name: Charan
Enter marks in Subject 1: 55
Enter marks in Subject 2: 85
Enter marks in Subject 3: 90
Enter Attendance Percentage: 90
Enter Annual Family Income: 200000

Enter details of Student 4
Enter Roll Number: 104
Enter Student Name: Divya
Enter marks in Subject 1: 75
Enter marks in Subject 2: 80
Enter marks in Subject 3: 85
Enter Attendance Percentage: 70
Enter Annual Family Income: 180000

Enter details of Student 5
Enter Roll Number: 105
Enter Student Name: Ezhil
Enter marks in Subject 1: 85
Enter marks in Subject 2: 90
Enter marks in Subject 3: 95
Enter Attendance Percentage: 92
Enter Annual Family Income: 400000
```

## 6. Sample Output

text

```text
========== SCHOLARSHIP ELIGIBLE STUDENTS ==========

Rank  Roll No  Name   Aggregate  Attendance  Income

1     101      Arun   90.00%     90%         200000
2     102      Banu   85.00%     95%         250000

========== REJECTED STUDENTS ==========

Name: Charan
Roll Number: 103
Reason(s): Subject mark below 60

Name: Divya
Roll Number: 104
Reason(s): Attendance below 75%

Name: Ezhil
Roll Number: 105
Reason(s): Family income exceeds Rs. 300000

Scholarship allocation process completed.
```

## 7. Mermaid Flowchart Code

The following Mermaid code represents the complete scholarship allocation process.

mermaid

```mermaid

flowchart TD
    A([Start]) --> B[/Enter Number of Students/]
    B --> C[/Enter Student Details:<br/>Name, Roll Number,<br/>Subject Marks, Attendance,<br/>Family Income/]
    C --> D[Calculate Total and Aggregate Marks]

    D --> E{Aggregate >= 75%?}
    E -- No --> R[Reject Student]
    E -- Yes --> F{All Subject Marks >= 60?}

    F -- No --> R
    F -- Yes --> G{Attendance >= 75%?}

    G -- No --> R
    G -- Yes --> H{Family Income <= 300000?}

    H -- No --> R
    H -- Yes --> I[Add Student to Eligible List]

    R --> J{More Students?}
    I --> J

    J -- Yes --> C
    J -- No --> K[Sort Eligible Students]

    K --> L[Rank by Aggregate Marks]
    L --> M[Resolve Ties Using Attendance,<br/>Income and Total Marks]

    M --> N[/Display Eligible Students<br/>with Ranks/]
    N --> O[/Display Rejected Students<br/>with Reasons/]

    O --> P([End])
```

## 8. Expected Result

The University Scholarship Allocation System successfully evaluates students based on academic marks, subject-wise minimum scores, attendance percentage, and family income.

- Eligible students are selected automatically.
- Ineligible students are rejected with appropriate reasons.
- Eligible students are ranked according to academic performance.
- Ties are resolved using attendance, family income, and total marks.

Conclusion: Thus, the University Scholarship Allocation System is implemented successfully using Python. It provides a simple, transparent, and efficient method for selecting and ranking scholarship applicants.
