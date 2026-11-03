
# Smart Hostel Resource Monitoring System

# Utility rates
ELECTRICITY_RATE = 8       # Rs per kWh
WATER_RATE = 0.05          # Rs per litre

# Consumption thresholds
ELECTRICITY_LIMIT = 100    # kWh
WATER_LIMIT = 1000         # Litres

# Hostel details
hostel = {}

floors = int(input("Enter number of floors: "))

# Input room-wise consumption
for floor in range(1, floors + 1):

    rooms = int(input(f"\nEnter number of rooms on Floor {floor}: "))

    hostel[floor] = []

    for room in range(1, rooms + 1):

        print(f"\nFloor {floor} - Room {room}")

        electricity = float(
            input("Enter electricity consumption (kWh): ")
        )

        water = float(
            input("Enter water consumption (litres): ")
        )

        # Calculate charges
        electricity_bill = electricity * ELECTRICITY_RATE
        water_bill = water * WATER_RATE

        total_bill = electricity_bill + water_bill

        # Check threshold violations
        violations = []

        if electricity > ELECTRICITY_LIMIT:
            violations.append("High Electricity")

        if water > WATER_LIMIT:
            violations.append("High Water")

        hostel[floor].append({
            "room": room,
            "electricity": electricity,
            "water": water,
            "electricity_bill": electricity_bill,
            "water_bill": water_bill,
            "total_bill": total_bill,
            "violations": violations
        })

# Display room-wise report
print("\n========== ROOM-WISE REPORT ==========")

for floor, rooms in hostel.items():

    print(f"\nFloor {floor}")

    for data in rooms:

        print(f"\nRoom {data['room']}")
        print("Electricity:", data["electricity"], "kWh")
        print("Water:", data["water"], "Litres")
        print("Electricity Bill: Rs.", data["electricity_bill"])
        print("Water Bill: Rs.", data["water_bill"])
        print("Total Bill: Rs.", data["total_bill"])

        if data["violations"]:
            print("ALERT:", ", ".join(data["violations"]))
        else:
            print("Status: Normal")

# Floor-wise comparison
print("\n========== FLOOR-WISE ANALYSIS ==========")

floor_totals = {}

for floor, rooms in hostel.items():

    total_electricity = sum(
        room["electricity"] for room in rooms
    )

    total_water = sum(
        room["water"] for room in rooms
    )

    total_amount = sum(
        room["total_bill"] for room in rooms
    )

    floor_totals[floor] = {
        "electricity": total_electricity,
        "water": total_water,
        "amount": total_amount
    }

    print(f"\nFloor {floor}")
    print("Total Electricity:", total_electricity, "kWh")
    print("Total Water:", total_water, "Litres")
    print("Total Charges: Rs.", total_amount)

# Identify highest consuming floor
highest_electricity = max(
    floor_totals,
    key=lambda x: floor_totals[x]["electricity"]
)

highest_water = max(
    floor_totals,
    key=lambda x: floor_totals[x]["water"]
)

print("\n========== FINAL SUMMARY ==========")

print("Highest Electricity Consumption: Floor",
      highest_electricity)

print("Highest Water Consumption: Floor",
      highest_water)

grand_total = sum(
    data["amount"] for data in floor_totals.values()
)

print("Total Hostel Bill: Rs.", grand_total)

print("\nMonitoring Completed Successfully!")

