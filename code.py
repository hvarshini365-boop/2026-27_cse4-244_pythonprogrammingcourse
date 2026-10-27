
# University Scholarship Allocation System

# Eligibility criteria
MIN_AGGREGATE = 75.0
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75.0
MAX_FAMILY_INCOME = 250000
NUMBER_OF_SUBJECTS = 3


def evaluate_student(student):
    """Check eligibility and calculate aggregate percentage."""

    marks = student["marks"]
    aggregate = sum(marks) / len(marks)
    student["aggregate"] = aggregate

    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate below 75%")

    if any(mark < MIN_SUBJECT_MARKS for mark in marks):
        reasons.append("Subject mark below 60")

    if student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if student["income"] > MAX_FAMILY_INCOME:
        reasons.append("Family income exceeds limit")

    student["eligible"] = len(reasons) == 0
    student["reasons"] = reasons

    return student


def main():
    print("UNIVERSITY SCHOLARSHIP ALLOCATION")
    print("---------------------------------")

    n = int(input("Enter number of applicants: "))
    scholarship_count = int(
        input("Enter number of scholarships available: ")
    )

    if n < 0 or scholarship_count < 0:
        print("Applicant and scholarship counts cannot be negative.")
        return

    students = []

    for i in range(n):
        print(f"\nApplicant {i + 1}")

        name = input("Enter student name: ").strip()
        marks = []

        for j in range(NUMBER_OF_SUBJECTS):
            mark = float(
                input(f"Enter marks for subject {j + 1} (0-100): ")
            )
            if not 0 <= mark <= 100:
                print("Invalid marks. Enter values from 0 to 100.")
                return
            marks.append(mark)

        attendance = float(input("Enter attendance percentage: "))
        income = float(input("Enter annual family income (Rs.): "))

        if not 0 <= attendance <= 100 or income < 0:
            print("Invalid attendance or income.")
            return

        student = {
            "name": name,
            "marks": marks,
            "attendance": attendance,
            "income": income
        }

        students.append(evaluate_student(student))

    # Separate eligible and ineligible applicants
    eligible = [s for s in students if s["eligible"]]
    ineligible = [s for s in students if not s["eligible"]]

    # Tie-breaking priority:
    # 1. Higher aggregate
    # 2. Higher attendance
    # 3. Lower family income
    # 4. Alphabetically earlier name
    eligible.sort(
        key=lambda s: (
            -s["aggregate"],
            -s["attendance"],
            s["income"],
            s["name"].casefold()
        )
    )

    print("\n--- ELIGIBILITY RESULTS ---")

    for student in students:
        status = "Eligible" if student["eligible"] else "Not Eligible"
        print(
            f"{student['name']}: {status}, "
            f"Aggregate = {student['aggregate']:.2f}%"
        )

        if not student["eligible"]:
            print("  Reason:", ", ".join(student["reasons"]))

    print("\n--- SCHOLARSHIP RANKING ---")

    if not eligible:
        print("No eligible applicants.")
    else:
        for rank, student in enumerate(eligible, start=1):
            awarded = rank <= scholarship_count
            result = "Awarded" if awarded else "Not Awarded"

            print(
                f"Rank {rank}: {student['name']} | "
                f"Aggregate: {student['aggregate']:.2f}% | "
                f"Attendance: {student['attendance']:.1f}% | "
                f"Income: Rs.{student['income']:.0f} | "
                f"Scholarship: {result}"
            )

    print("\n--- FINAL SUMMARY ---")
    print("Total applicants:", len(students))
    print("Eligible applicants:", len(eligible))
    print("Ineligible applicants:", len(ineligible))
    print(
        "Scholarships awarded:",
        min(scholarship_count, len(eligible))
    )


if __name__ == "__main__":
    main()

