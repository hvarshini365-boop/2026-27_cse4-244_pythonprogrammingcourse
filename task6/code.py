
# Smart Campus Incident and Maintenance Prioritization System

# Severity scores
severity_scores = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4
}

# Location importance scores
location_scores = {
    "classroom": 2,
    "library": 2,
    "laboratory": 3,
    "hostel": 3,
    "electrical room": 4,
    "other": 1
}

# Function to calculate priority
def calculate_priority(severity, location, frequency):
    score = (
        severity_scores[severity] * 5 +
        location_scores.get(location, 1) * 3 +
        frequency * 2
    )
    return score

# Function to classify priority
def classify_priority(score):
    if score >= 35:
        return "Critical"
    elif score >= 25:
        return "High"
    elif score >= 15:
        return "Medium"
    else:
        return "Low"


# Main program
incidents = []

n = int(input("Enter number of maintenance reports: "))

for i in range(n):
    print("\nEnter details for Incident", i + 1)

    description = input("Incident description: ")
    severity = input(
        "Severity (Low/Medium/High/Critical): "
    ).strip().lower()

    location = input(
        "Location (Classroom/Library/Laboratory/"
        "Hostel/Electrical Room/Other): "
    ).strip().lower()

    frequency = int(
        input("Number of times reported: ")
    )

    if severity not in severity_scores:
        print("Invalid severity! Using Medium.")
        severity = "medium"

    if frequency < 0:
        print("Invalid frequency! Using 0.")
        frequency = 0

    score = calculate_priority(
        severity, location, frequency
    )

    priority = classify_priority(score)

    incidents.append({
        "description": description,
        "severity": severity,
        "location": location,
        "frequency": frequency,
        "score": score,
        "priority": priority
    })


# Sort incidents by priority score
incidents.sort(
    key=lambda x: x["score"],
    reverse=True
)

# Display ranked incidents
print("\n========== INCIDENT PRIORITY RANKING ==========")

for rank, incident in enumerate(incidents, start=1):
    print(f"\nRank: {rank}")
    print("Description:", incident["description"])
    print("Severity:", incident["severity"].title())
    print("Location:", incident["location"].title())
    print("Frequency:", incident["frequency"])
    print("Priority Score:", incident["score"])
    print("Priority Level:", incident["priority"])


# Generate priority summary
summary = {
    "Critical": 0,
    "High": 0,
    "Medium": 0,
    "Low": 0
}

for incident in incidents:
    summary[incident["priority"]] += 1

print("\n========== PRIORITY SUMMARY ==========")
print("Total Incidents:", len(incidents))

for level, count in summary.items():
    print(level, "Priority:", count)

if incidents:
    print("\nMost Urgent Issue:",
          incidents[0]["description"])
    print("Recommended Action:",
          "Attend to the highest-ranked incident first.")

print("\nMaintenance prioritization completed.")

