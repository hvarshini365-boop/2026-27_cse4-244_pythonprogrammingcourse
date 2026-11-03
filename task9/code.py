
# Manufacturing Quality Control Matrix

# Input quality threshold
threshold = float(input("Enter acceptable defect threshold (%): "))

# Input number of products
n = int(input("Enter number of products: "))

# Store batch details
quality_matrix = []

for i in range(n):
    product = input("\nEnter product name: ")
    batches = int(input("Enter number of batches: "))

    for j in range(batches):
        print("\nProduct:", product)
        print("Batch:", j + 1)

        production = int(input("Enter production quantity: "))
        defective = int(input("Enter defective units: "))

        # Validate quantities
        if production <= 0 or defective < 0 or defective > production:
            print("Invalid batch data!")
            continue

        # Calculate defect percentage
        defect_percentage = (defective / production) * 100

        # Check quality threshold
        if defect_percentage > threshold:
            status = "Poor Quality"
        else:
            status = "Acceptable Quality"

        # Store results
        quality_matrix.append([
            product,
            j + 1,
            production,
            defective,
            defect_percentage,
            status
        ])

# Display quality control matrix
print("\n========== QUALITY CONTROL MATRIX ==========")

print("{:<12} {:<8} {:<12} {:<12} {:<12} {}".format(
    "Product", "Batch", "Production",
    "Defective", "Defect %", "Status"
))

for record in quality_matrix:
    print("{:<12} {:<8} {:<12} {:<12} {:<12.2f} {}".format(
        record[0], record[1], record[2],
        record[3], record[4], record[5]
    ))

# Identify batches exceeding threshold
print("\nBatches Exceeding Quality Threshold:")

found = False

for record in quality_matrix:
    if record[4] > threshold:
        print("Product:", record[0],
              "| Batch:", record[1],
              "| Defect:", round(record[4], 2), "%")
        found = True

if not found:
    print("No batches exceed the quality threshold.")

print("\nQuality analysis completed.")

