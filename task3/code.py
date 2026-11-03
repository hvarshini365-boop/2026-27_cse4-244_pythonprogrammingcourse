
# Campus Event Financial Planning System

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input details
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transportation cost: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter number of participants: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Calculate fixed costs
fixed_cost = venue + equipment + transport

# Calculate variable costs
variable_cost = catering + certificate
total_variable_cost = variable_cost * participants

# Calculate total event cost
total_cost = fixed_cost + total_variable_cost

# Calculate sponsorship shortfall
shortfall = max(0, total_cost - sponsorship)

# Calculate participant contribution
remaining_amount = max(0, total_cost - sponsorship)

if participants > 0:
    contribution = remaining_amount / participants
else:
    contribution = 0

# Calculate minimum registrations to break even
# Assume each participant pays the calculated contribution
# and sponsorship is fixed.

if contribution > variable_cost:
    min_participants = fixed_cost / (contribution - variable_cost)
    min_participants = int(min_participants) + (
        int(min_participants) < min_participants
    )
else:
    min_participants = 0

# Display results
print("\n===== EVENT FINANCIAL REPORT =====")
print("Venue Cost:", venue)
print("Equipment Cost:", equipment)
print("Catering Cost:", catering * participants)
print("Transportation Cost:", transport)
print("Certificate Cost:", certificate * participants)

print("Fixed Cost:", fixed_cost)
print("Variable Cost:", total_variable_cost)
print("Total Event Cost:", total_cost)
print("Sponsorship Amount:", sponsorship)
print("Sponsorship Shortfall:", shortfall)

print("Participant Contribution Per Person:", round(contribution, 2))
print("Minimum Registrations Required:", min_participants)

if sponsorship >= total_cost:
    print("Event Status: Fully Sponsored")
elif shortfall > 0:
    print("Event Status: Additional Funding Required")

