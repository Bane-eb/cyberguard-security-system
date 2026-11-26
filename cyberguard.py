# CyberGuard Account Security Analyzer

print("========================================")
print("      CYBERGUARD SECURITY SYSTEM")


username = input("Enter username: ")
email = input("Enter email address: ")
password = input("Enter password: ")
age = int(input("Enter age: "))
ip_address = input("Enter IP address: ")
failed_attempts = int(input("Enter failed login attempts: "))
status_input = input("Enter account status (Active/Inactive): ")


is_active = status_input.strip().lower() == "active"

risk_score = float(failed_attempts) * 15.5


print("\n--- DATA TYPE VERIFICATION ---")
print("Username type: " + str(type(username)))
print("Email type: " + str(type(email)))
print("Password type: " + str(type(password)))
print("Age type: " + str(type(age)))
print("IP Address type: " + str(type(ip_address)))
print("Failed Attempts type: " + str(type(failed_attempts)))
print("Account Status (Boolean) type: " + str(type(is_active)))
print("Risk Score (Float) type: " + str(type(risk_score)))


is_weak_password = (
    len(password) < 8
    or password.lower() == "password"
    or password.lower() == "password123"
    or password.lower() == "mypassword123"
    or password.lower() == "hello123"
    or password == "12345678"
)

if is_weak_password:
    password_assessment = "WEAK"
    risk_score += 25.0
else:
    password_assessment = "STRONG"

# 4. Account status display string
if is_active:
    account_status_display = "ACTIVE"
else:
    account_status_display = "INACTIVE"


if not is_active:
    threat_detection = "[WARNING] Account is currently INACTIVE.\n[INFO] Login access should remain restricted."
    threat_level = "ACCOUNT INACTIVE"
    recommendation = "Keep account disabled until verified by an administrator."
else:
    if failed_attempts >= 5:
        threat_detection = "[CRITICAL] Multiple failed login attempts!\n[WARNING] Possible brute-force attack detected."
        threat_level = "HIGH"
        recommendation = "Investigate the login activity and secure\nthe account immediately."
    else:
        if failed_attempts > 0 or is_weak_password:
            threat_detection = "[WARNING] Suspicious indicators detected (failed logins or weak password)."
            threat_level = "MEDIUM"
            recommendation = "Enforce a stronger password and monitor recent login attempts."
        else:
            threat_detection = "[OK] No failed login attempts and no critical threat."
            threat_level = "LOW"
            recommendation = "No immediate action required. Continue standard monitoring."


print("\n========================================")
print("          CYBERGUARD SECURITY REPORT")
print("========================================")

print("\nUSER INFORMATION")
print("----------------------------------------")
print("Username: " + username)
print("Email: " + email)
print("Age: " + str(age))
print("IP Address: " + ip_address)
print("Account Status: " + account_status_display)

print("\nSECURITY ANALYSIS")
print("----------------------------------------")
print("Password Assessment: " + password_assessment)
print("Failed Login Attempts: " + str(failed_attempts))
print("Calculated Risk Score: " + str(risk_score))

print("\nTHREAT DETECTION")
print("----------------------------------------")
print(threat_detection)

print("\nFINAL SECURITY STATUS")
print("----------------------------------------")
print("THREAT LEVEL: " + threat_level)

print("\nRECOMMENDATION:")
print(recommendation)

print("\n========================================")
print("          END OF SECURITY REPORT")
print("========================================")
