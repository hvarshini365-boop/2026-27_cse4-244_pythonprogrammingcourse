

# Railway Fare and Reservation Calculator

def calculate_base_fare(distance, travel_class):

    # Fare rates per kilometre
    rates = {
        "Sleeper": 1.0,
        "AC3": 2.0,
        "AC2": 3.0,
        "AC1": 4.0
    }

    return distance * rates[travel_class]


def calculate_concession(age, fare):

    if age < 5:
        return fare       # Free basic fare

    elif age <= 11:
        return fare * 0.50

    elif age >= 60:
        return fare * 0.40

    else:
        return 0


def calculate_reservation_fee(travel_class):

    fees = {
        "Sleeper": 20,
        "AC3": 40,
        "AC2": 50,
        "AC1": 60
    }

    return fees[travel_class]


def calculate_cancellation_penalty(fare):

    # Illustrative cancellation penalty: 25%
    return fare * 0.25


# Main program

print("RAILWAY FARE AND RESERVATION CALCULATOR")

n = int(input("Enter number of passengers: "))
distance = float(input("Enter journey distance (km): "))

total_booking = 0
total_penalty = 0

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))

    print("Classes: Sleeper, AC3, AC2, AC1")
    travel_class = input("Enter travel class: ").strip()

    travel_class = travel_class.upper()

    # Normalize class names
    if travel_class == "SLEEPER":
        travel_class = "Sleeper"
    elif travel_class == "AC3":
        travel_class = "AC3"
    elif travel_class == "AC2":
        travel_class = "AC2"
    elif travel_class == "AC1":
        travel_class = "AC1"
    else:
        print("Invalid travel class!")
        continue

    # Calculate basic fare
    base_fare = calculate_base_fare(
        distance, travel_class
    )

    # Calculate age concession
    concession = calculate_concession(
        age, base_fare
    )

    # Calculate reservation fee
    reservation_fee = calculate_reservation_fee(
        travel_class
    )

    # Final ticket fare
    ticket_fare = (
        base_fare - concession + reservation_fee
    )

    print("\nCancellation Status")
    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":

        penalty = calculate_cancellation_penalty(
            ticket_fare
        )

        refund = ticket_fare - penalty

        total_penalty += penalty

        print("\n--- Cancellation Details ---")
        print("Passenger:", name)
        print("Ticket Fare: Rs.", round(ticket_fare, 2))
        print("Cancellation Penalty: Rs.",
              round(penalty, 2))
        print("Refund Amount: Rs.", round(refund, 2))

    else:

        penalty = 0
        total_booking += ticket_fare

        print("\n--- Ticket Details ---")
        print("Passenger:", name)
        print("Age:", age)
        print("Travel Class:", travel_class)
        print("Distance:", distance, "km")
        print("Basic Fare: Rs.", round(base_fare, 2))
        print("Age Concession: Rs.",
              round(concession, 2))
        print("Reservation Fee: Rs.",
              round(reservation_fee, 2))
        print("Total Fare: Rs.",
              round(ticket_fare, 2))

print("\n========== FINAL SUMMARY ==========")
print("Total Confirmed Booking: Rs.",
      round(total_booking, 2))
print("Total Cancellation Penalty: Rs.",
      round(total_penalty, 2))
print("Total Amount Collected: Rs.",
      round(total_booking + total_penalty, 2))

print("Thank You! Happy Journey!")

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

