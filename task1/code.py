
# University Scholarship Allocation System

AGGREGATE_MIN = 75
SUBJECT_MIN = 60
ATTENDANCE_MIN = 75
INCOME_MAX = 250000


def check_eligibility(student):
    reasons = []

    if student["aggregate"] < AGGREGATE_MIN:
        reasons.append("Aggregate marks below 75%")

    if any(mark < SUBJECT_MIN for mark in student["subjects"]):
        reasons.append("A subject score is below 60%")

    if student["attendance"] < ATTENDANCE_MIN:
        reasons.append("Attendance below 75%")

    if student["income"] > INCOME_MAX:
        reasons.append("Family income exceeds Rs. 2,50,000")

    return reasons


def rank_key(student):
    # Higher aggregate first, higher attendance first,
    # lower income first, then alphabetical name.
    return (
        -student["aggregate"],
        -student["attendance"],
        student["income"],
        student["name"].casefold()
    )


def main():
    students = []

    n = int(input("Enter number of applicants: "))
    scholarships = int(input("Enter number of scholarships: "))
    subject_count = int(input("Enter number of subjects: "))

    if n < 0 or scholarships < 0 or subject_count <= 0:
        print("Invalid input.")
        return

    for i in range(n):
        print(f"\nApplicant {i + 1}")

        name = input("Name: ").strip()
        aggregate = float(input("Aggregate marks (%): "))

        subjects = []
        for j in range(subject_count):
            mark = float(input(f"Subject {j + 1} marks (%): "))
            subjects.append(mark)

        attendance = float(input("Attendance (%): "))
        income = float(input("Annual family income (Rs.): "))

        student = {
            "name": name,
            "aggregate": aggregate,
            "subjects": subjects,
            "attendance": attendance,
            "income": income
        }

        student["reasons"] = check_eligibility(student)
        students.append(student)

    eligible = [
        s for s in students if not s["reasons"]
    ]

    rejected = [
        s for s in students if s["reasons"]
    ]

    eligible.sort(key=rank_key)

    winners = eligible[:scholarships]

    print("\n===== ELIGIBLE STUDENTS: RANKING =====")

    if not eligible:
        print("No eligible applicants.")
    else:
        for rank, student in enumerate(eligible, start=1):
            print(
                f"{rank}. {student['name']} | "
                f"Aggregate: {student['aggregate']:.2f}% | "
                f"Attendance: {student['attendance']:.2f}% | "
                f"Income: Rs. {student['income']:.2f}"
            )

    print("\n===== SCHOLARSHIP RECIPIENTS =====")

    if not winners:
        print("No scholarships allocated.")
    else:
        for rank, student in enumerate(winners, start=1):
            print(f"{rank}. {student['name']}")

    print("\n===== INELIGIBLE APPLICANTS =====")

    if not rejected:
        print("No rejected applicants.")
    else:
        for student in rejected:
            print(f"{student['name']}: "
                  + "; ".join(student["reasons"]))

    print(
        f"\nScholarships allocated: {len(winners)}"
        f" out of {scholarships}"
    )


if __name__ == "__main__":
    main()

