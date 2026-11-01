
import re

print("PASSWORD POLICY VALIDATION ENGINE")
print("----------------------------------")

password = input("Enter your password: ")

errors = []


if len(password) < 8:
    errors.append("Password must contain at least 8 characters.")


if not re.search(r"[A-Z]", password):
    errors.append("At least one uppercase letter is required.")

if not re.search(r"[a-z]", password):
    errors.append("At least one lowercase letter is required.")

if not re.search(r"[0-9]", password):
    errors.append("At least one digit is required.")

if not re.search(r"[^A-Za-z0-9]", password):
    errors.append("At least one special character is required.")


if re.search(r"(.)\1\1", password):
    errors.append("Password must not contain 3 or more consecutive identical characters.")


prohibited = ["password", "admin", "123456"]

for word in prohibited:
    if word in password.lower():
        errors.append("Password contains prohibited substring: " + word)


print("\nPASSWORD VALIDATION REPORT")
print("----------------------------------")

if len(errors) == 0:
    print("Status: VALID")
    print("All password security conditions satisfied!")

else:
    print("Status: INVALID")
    print("\nFailed Conditions:")

    for i, error in enumerate(errors, 1):
        print(str(i) + ".", error)

print("\nThank you!")

