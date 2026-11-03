# Railway Fare and Reservation Calculator Using Python

## 1. Problem Statement
. Railway Fare and Reservation Calculator: Calculate fares for multiple passengers using distance slabs, travel classes, age-based concessions, reservation fees, and specified cancellation penalties. 


## 2. Algorithm

1. Start the program.
2. Read the number of passengers.
3. Read the journey distance in kilometres.
4. For each passenger:
   - Read passenger name and age.
   - Read the travel class.
   - Calculate the basic fare based on distance.
   - Apply the age-based concession:
     - Children below 5 years: Free basic fare.
     - Children aged 5–11 years: 50% concession.
     - Senior citizens aged 60 and above: 40% concession.
     - Other passengers: No concession.
   - Calculate the reservation fee according to travel class.
   - Calculate the total ticket fare.
   - Ask whether the ticket is cancelled.
   - If cancelled, calculate the cancellation penalty.
   - Otherwise, consider the ticket confirmed.
5. Display the fare details of each passenger.
6. Calculate the total amount for all passengers.
7. Display the final bill.
8. Stop.

## 3. Flowchart

Cấu trúc rẽ nhánh, thuật toán, Tin học 6.

[olm.vn](<https://olm.vn/chu-de/luyen-tap-bai-15-tin-hoc-lop-6-sach-chan-troi-sang-tao-chu-de-6-3479775781?utm_source=chatgpt.com>)

Flowchart explanation:

- Start with passenger and journey details.
- Calculate distance-based fare.
- Apply class charges and age concessions.
- Add reservation fees.
- Check cancellation status.
- Calculate cancellation penalty if applicable.
- Display the final fare details.

## 4. Python Source Code

The following program uses illustrative fare rates and concession rules for an academic project. These are not official Indian Railways rates.

python

```python

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
```

## 5. Sample Input

text

```text
RAILWAY FARE AND RESERVATION CALCULATOR

Enter number of passengers: 3
Enter journey distance (km): 500

Passenger 1
Enter passenger name: Ravi
Enter passenger age: 30
Enter travel class: Sleeper
Cancel ticket? (yes/no): no

Passenger 2
Enter passenger name: Sita
Enter passenger age: 65
Enter travel class: AC3
Cancel ticket? (yes/no): no

Passenger 3
Enter passenger name: Arun
Enter passenger age: 10
Enter travel class: AC2
Cancel ticket? (yes/no): yes
```

## 6. Sample Output

Using the fare rates defined in the program:

Passenger 1 – Ravi

| Description | Amount |
| --- | --- |
| Basic fare | ₹500 |
| Concession | ₹0 |
| Reservation fee | ₹20 |
| Total fare | ₹520 |

Passenger 2 – Sita

| Description | Amount |
| --- | --- |
| Basic fare | ₹1,000 |
| Senior concession (40%) | −₹400 |
| Reservation fee | ₹40 |
| Total fare | ₹640 |

Passenger 3 – Arun

| Description | Amount |
| --- | --- |
| Basic fare | ₹1,500 |
| Child concession (50%) | −₹750 |
| Reservation fee | ₹50 |
| Ticket fare | ₹800 |
| Cancellation penalty (25%) | ₹200 |
| Refund amount | ₹600 |

Final Summary

| Description | Amount |
| --- | --- |
| Confirmed bookings | ₹1,160 |
| Cancellation penalty | ₹200 |
| Total amount collected | ₹1,360 |

Calculation completed

Equivalent console output:

text

```text
========== FINAL SUMMARY ==========

Total Confirmed Booking: Rs. 1160.0
Total Cancellation Penalty: Rs. 200.0
Total Amount Collected: Rs. 1360.0

Thank You! Happy Journey!
```

## 7. Mermaid Flowchart Code

You can copy this code into the [Mermaid Live Editor](<https://mermaid.live/?utm_source=chatgpt.com>) to generate the flowchart.

mermaid

```mermaid

flowchart TD
    A([Start]) --> B[/Enter number of passengers/]
    B --> C[/Enter journey distance/]
    C --> D[/Enter passenger name and age/]
    D --> E[/Select travel class/]

    E --> F[Calculate basic fare]
    F --> G[Calculate age concession]
    G --> H[Calculate reservation fee]
    H --> I[Calculate total ticket fare]

    I --> J{Cancel ticket?}

    J -->|Yes| K[Calculate cancellation penalty]
    K --> L[Calculate refund amount]
    L --> M[Display cancellation details]

    J -->|No| N[Confirm ticket]
    N --> O[Display ticket details]

    M --> P{More passengers?}
    O --> P

    P -->|Yes| D
    P -->|No| Q[Calculate final summary]
    Q --> R[Display total amount]
    R --> S([Stop])
```

## 8. Expected Result

The Railway Fare and Reservation Calculator successfully calculates railway ticket fares for multiple passengers based on distance, travel class, age concessions, reservation charges, and cancellation penalties.

Conclusion: This Python program demonstrates the use of functions, conditional statements, loops, arithmetic operations, and user input to develop a railway reservation and fare calculation system.

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










 
   
      
  




  
