import re

email = input("Enter the email content:\n")

risk_score = 0
warnings = []

# Check for urgent or threatening language
urgent_words = [
    "urgent", "immediately", "act now", "verify now",
    "account suspended", "account blocked", "final warning"
]

for word in urgent_words:
    if word.lower() in email.lower():
        risk_score += 1
        warnings.append(f"Suspicious urgent phrase: '{word}'")

# Check for links
links = re.findall(r"https?://\S+|www\.\S+", email)

if links:
    risk_score += 2
    warnings.append("Email contains a link.")

# Check for sensitive information requests
sensitive_words = [
    "password", "otp", "pin", "credit card",
    "debit card", "bank account", "cvv",
    "login details", "account number"
]

for word in sensitive_words:
    if word.lower() in email.lower():
        risk_score += 2
        warnings.append(f"Sensitive information requested: '{word}'")

# Determine risk level
if risk_score >= 5:
    risk_level = "HIGH RISK"
elif risk_score >= 2:
    risk_level = "MEDIUM RISK"
else:
    risk_level = "LOW RISK"

print("\nEmail Risk Level:", risk_level)

if warnings:
    print("\nWarnings:")
    for warning in warnings:
        print("-", warning)
else:
    print("No suspicious patterns detected.")