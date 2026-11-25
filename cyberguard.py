

print("=== CYBERGUARD SECURITY SYSTEM ===")


username = input("Enter username: ")

failed_attempts_text = input("Enter failed login attempts: ")

account_status = input("Enter account status (Active/Inactive): ")

password = input("Enter password: ")

risk_weight_text = input("Enter threat weight multiplier (e.g. 1.5): ")


failed_attempts = int(failed_attempts_text)

risk_weight = float(risk_weight_text)


is_active = account_status.lower() == "active"

is_weak_password = len(password) < 10 or 
password.lower() == "password123" or password.lower() == "mypassword123" or password.lower() == "hello123"

# Calculate a float threat score using assignment and arithmetic operators
threat_score = failed_attempts * 15.0
threat_score = threat_score * risk_weight

if is_weak_password:
    threat_score = threat_score + 20.0
else:
    threat_score = threat_score + 0.0

# Determine threat level and warnings using if and else
if not is_active:
    threat_level = "Account inactive"
    status_note = "Warning: Account is inactive. Block login access and verify account status."
else:
    if failed_attempts >= 5:
        threat_level = "High threat"
        status_note = "Critical brute-force warning: High number of failed login attempts detected."
    else:
        if failed_attempts == 0:
            threat_level = "Low threat"
            status_note = "No failed login attempts and no critical threat."
        else:
            threat_level = "Medium threat"
            status_note = "Moderate failed login attempts detected; monitor account activity."

if is_weak_password:
    password_note = "Weak password detected: Use at least 10 characters and avoid common passwords."
else:
    password_note = "Password length and strength check passed."


print("--- CYBERGUARD SECURITY REPORT ---")
print("Username: " + username)
print("Account Active: " + str(is_active))
print("Failed Login Attempts: " + str(failed_attempts))
print("Threat Score: " + str(threat_score))
print("Threat Level: " + threat_level)
print("Activity Assessment: " + status_note)
print("Password Assessment: " + password_note)
print("Data Type of Threat Score: " + str(type(threat_score)))
