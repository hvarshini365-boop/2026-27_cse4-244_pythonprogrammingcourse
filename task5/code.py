
# Warehouse Inventory Reconciliation System

def inventory_reconciliation():

    inventory = []

    n = int(input("Enter number of products: "))

    for i in range(n):

        print("\nEnter details for Product", i + 1)

        name = input("Product Name: ")

        opening = int(input("Opening Stock: "))
        incoming = int(input("Incoming Quantity: "))
        dispatched = int(input("Dispatched Quantity: "))
        actual_closing = int(input("Actual Closing Stock: "))
        minimum_stock = int(input("Minimum Stock Level: "))

        # Calculate expected closing stock
        expected_closing = opening + incoming - dispatched

        # Calculate discrepancy
        discrepancy = actual_closing - expected_closing

        # Identify stock status
        if discrepancy == 0:
            status = "No Discrepancy"
        elif discrepancy < 0:
            status = "Stock Shortage"
        else:
            status = "Excess Stock"

        # Calculate replenishment requirement
        replenishment = max(0, minimum_stock - actual_closing)

        # Store product information
        inventory.append({
            "name": name,
            "opening": opening,
            "incoming": incoming,
            "dispatched": dispatched,
            "expected": expected_closing,
            "actual": actual_closing,
            "discrepancy": discrepancy,
            "status": status,
            "replenishment": replenishment
        })

    # Display reconciliation report
    print("\n========== WAREHOUSE INVENTORY REPORT ==========")

    print("{:<12} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        "Product", "Opening", "Incoming", "Dispatch",
        "Expected", "Actual"
    ))

    for item in inventory:

        print("{:<12} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            item["name"],
            item["opening"],
            item["incoming"],
            item["dispatched"],
            item["expected"],
            item["actual"]
        ))

    print("\n========== DISCREPANCY REPORT ==========")

    print("{:<12} {:<12} {:<20} {:<15}".format(
        "Product", "Difference", "Status", "Replenishment"
    ))

    for item in inventory:

        print("{:<12} {:<12} {:<20} {:<15}".format(
            item["name"],
            item["discrepancy"],
            item["status"],
            item["replenishment"]
        ))

    print("\nInventory reconciliation completed.")


# Main program
inventory_reconciliation()

