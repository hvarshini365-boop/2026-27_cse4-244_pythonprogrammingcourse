
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

