
# Food Supply Chain Stock Reconciliation System

locations = []

n = int(input("Enter number of locations: "))

for i in range(n):
    print("\nLocation", i + 1)

    name = input("Enter location name: ")
    item = input("Enter food item name: ")

    received = int(input("Quantity received: "))
    distributed = int(input("Quantity distributed: "))
    damaged = int(input("Quantity damaged: "))
    actual = int(input("Actual remaining stock: "))
    minimum = int(input("Minimum required stock: "))

    # Calculate expected stock
    expected = received - distributed - damaged

    # Calculate discrepancy
    discrepancy = actual - expected

    # Calculate replenishment
    replenishment = max(0, minimum - actual)

    # Determine stock status
    if discrepancy == 0:
        status = "Balanced"
    elif discrepancy > 0:
        status = "Excess Stock"
    else:
        status = "Stock Shortage"

    # Store location details
    locations.append({
        "name": name,
        "item": item,
        "received": received,
        "distributed": distributed,
        "damaged": damaged,
        "expected": expected,
        "actual": actual,
        "discrepancy": discrepancy,
        "replenishment": replenishment,
        "status": status
    })

# Display reconciliation report
print("\n========== STOCK RECONCILIATION REPORT ==========")

for loc in locations:
    print("\nLocation:", loc["name"])
    print("Food Item:", loc["item"])
    print("Received:", loc["received"])
    print("Distributed:", loc["distributed"])
    print("Damaged:", loc["damaged"])
    print("Expected Stock:", loc["expected"])
    print("Actual Stock:", loc["actual"])
    print("Discrepancy:", loc["discrepancy"])
    print("Stock Status:", loc["status"])
    print("Replenishment Required:", loc["replenishment"])

# Calculate total replenishment
total_replenishment = sum(
    loc["replenishment"] for loc in locations
)

print("\n========== SUMMARY ==========")
print("Total Locations:", n)
print("Total Replenishment Required:",
      total_replenishment)

print("\nStock reconciliation completed.")

