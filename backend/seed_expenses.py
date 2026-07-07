from database import expense_collection, user_collection
from datetime import datetime, timedelta
from random import randint, choice, random

# =====================================================
# Get First Registered User
# =====================================================

EMAIL = input("Enter the email of the user to seed: ").strip()

user = user_collection.find_one({"email": EMAIL})

if not user:
    print("❌ User not found.")
    exit()

USER_ID = str(user["_id"])

print(f"✅ Seeding data for: {EMAIL}")

# =====================================================
# Company Details
# =====================================================

company = "NovaAI Technologies"

categories = {
    "Payroll": [
        "Employee Salaries"
    ],

    "Cloud Infrastructure": [
        "AWS EC2",
        "AWS S3",
        "AWS RDS"
    ],

    "AI Infrastructure": [
        "OpenAI API"
    ],

    "Software": [
        "GitHub Enterprise",
        "Slack",
        "Notion",
        "Figma",
        "Jira"
    ],

    "Marketing": [
        "Google Ads",
        "LinkedIn Ads"
    ],

    "Office": [
        "Office Rent",
        "Electricity",
        "Internet"
    ],

    "Recruitment": [
        "LinkedIn Recruiter"
    ],

    "Hardware": [
        "MacBook Pro",
        "Dell Monitor"
    ],

    "Travel": [
        "Client Visit"
    ],

    "Legal": [
        "CA Services"
    ],

    "Misc": [
        "Team Lunch",
        "Office Supplies"
    ]
}

# =====================================================
# Expense Amount Ranges
# =====================================================

amounts = {

    "Payroll": (900000, 1200000),

    "Cloud Infrastructure": (45000, 85000),

    "AI Infrastructure": (18000, 50000),

    "Software": (3000, 15000),

    "Marketing": (20000, 90000),

    "Office": (10000, 70000),

    "Recruitment": (8000, 30000),

    "Hardware": (40000, 250000),

    "Travel": (5000, 35000),

    "Legal": (10000, 60000),

    "Misc": (1000, 12000)
}

# =====================================================
# Expense Descriptions
# =====================================================

descriptions = {

    "Employee Salaries": "Monthly payroll for employees",

    "AWS EC2": "Cloud compute charges",

    "AWS S3": "Cloud object storage charges",

    "AWS RDS": "Managed database hosting",

    "OpenAI API": "LLM API usage charges",

    "GitHub Enterprise": "Developer collaboration platform",

    "Slack": "Business communication platform",

    "Notion": "Documentation and knowledge base",

    "Figma": "UI/UX design collaboration",

    "Jira": "Project management platform",

    "Google Ads": "Digital marketing campaign",

    "LinkedIn Ads": "Hiring and branding campaign",

    "Office Rent": "Monthly office rental",

    "Electricity": "Monthly electricity bill",

    "Internet": "Business broadband services",

    "LinkedIn Recruiter": "Recruitment platform subscription",

    "MacBook Pro": "Engineering laptop purchase",

    "Dell Monitor": "Office monitor purchase",

    "Client Visit": "Business travel expenses",

    "CA Services": "Accounting and compliance",

    "Team Lunch": "Employee engagement activity",

    "Office Supplies": "Stationery and office essentials"
}

# =====================================================
# Generate Startup Expense History
# =====================================================

expenses = []

today = datetime.today()

for day in range(180):

    current_date = today - timedelta(days=179 - day)

    for category in categories:

        # Daily recurring infrastructure costs
        if category in ["Cloud Infrastructure", "AI Infrastructure"]:

            count = randint(1, 3)

        # Monthly recurring expenses
        elif category in ["Payroll", "Office"]:

            if current_date.day != 1:
                continue

            count = randint(2, 4)

        # Weekly expenses
        elif category in ["Marketing", "Travel", "Recruitment"]:

            if current_date.weekday() != 0:
                continue

            count = randint(1, 2)

        # Random operational expenses
        else:

            count = randint(0, 2)

        for _ in range(count):

            title = choice(categories[category])

            low, high = amounts[category]

            amount = randint(low, high)

            # Simulate gradual company growth (25% over 6 months)
            growth = day / 180

            amount *= (1 + growth * 0.25)

            # Random fluctuation ±10%
            amount *= (0.9 + random() * 0.2)

            expenses.append({

                "user_id": USER_ID,

                "title": title,

                "category": category,

                "amount": round(amount, 2),

                "date": current_date.strftime("%Y-%m-%d"),

                "description": descriptions.get(title, "")
            })

# =====================================================
# Inject Intentional Anomalies
# =====================================================

anomalies = [

    ("MacBook Pro", "Hardware", 3400000),

    ("AWS EC2", "Cloud Infrastructure", 680000),

    ("OpenAI API", "AI Infrastructure", 420000),

    ("Google Ads", "Marketing", 550000),

    ("Office Rent", "Office", 1800000),

    ("GitHub Enterprise", "Software", 320000)

]

for i, anomaly in enumerate(anomalies):

    expenses.append({

        "user_id": USER_ID,

        "title": anomaly[0],

        "category": anomaly[1],

        "amount": anomaly[2],

        "date": (today - timedelta(days=25 + i)).strftime("%Y-%m-%d"),

        "description": "Intentional anomaly for ML detection"
    })

# =====================================================
# Reset Previous Demo Data
# =====================================================

deleted = expense_collection.delete_many({
    "user_id": USER_ID
})

print(f"🗑 Deleted {deleted.deleted_count} previous expenses")

# =====================================================
# Insert New Dataset
# =====================================================

expense_collection.insert_many(expenses)

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 50)
print("📊 SmartExpense AI - Demo Dataset Generated")
print("=" * 50)
print(f"Company        : {company}")
print(f"User ID        : {USER_ID}")
print(f"Records Inserted : {len(expenses)}")
print(f"Duration       : 180 Days")
print("Dataset Type   : AI Startup Operational Expenses")
print("Status         : SUCCESS ✅")
print("=" * 50)