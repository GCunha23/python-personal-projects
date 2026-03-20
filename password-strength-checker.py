"""
Author: Gonçalo Cunha (GitHub: GCunha23)
Date Created: 17/01/2025
Last Modified: 20/01/2025

Description:
This is a password strength checker.
"""

# Title

print(r"""
+===============================================+
|  ______                                   _   |
|  | ___ \                                 | |  |
|  | |_/ /_ _ ___ _____      _____  _ __ __| |  |
|  |  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` |  |
|  | | | (_| \__ \__ \\ V  V / (_) | | | (_| |  |
|  \_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  |
|                                               |
|                                               |
|    _____ _                        _   _       |
|   /  ___| |                      | | | |      |
|   \ `--.| |_ _ __ ___ _ __   __ _| |_| |__    |
|    `--. \ __| '__/ _ \ '_ \ / _` | __| '_ \   |
|   /\__/ / |_| | |  __/ | | | (_| | |_| | | |  |
|   \____/ \__|_|  \___|_| |_|\__, |\__|_| |_|  |
|                              __/ |            |
|                             |___/             |
|      _____ _               _                  |
|     /  __ \ |             | |                 |
|     | /  \/ |__   ___  ___| | _____ _ __      |
|     | |   | '_ \ / _ \/ __| |/ / _ \ '__|     |
|     | \__/\ | | |  __/ (__|   <  __/ |        |
|      \____/_| |_|\___|\___|_|\_\___|_|        |
|                                               |
+===============================================+
""")

# Ask for user input - Password

passwd = input("Enter a password you would like to check: ")
print()

# Check password length and display output

if len(passwd) >= 12:
    print("- Your password has atleast 12 characters.")
else:
    print("- Your password has less than 12 characters.")

# Define False variables for checks

upperCaseFound = False
lowerCaseFound = False
numericFound = False
specialFound = False

# Perform checks for upper case letters, lower case letters, numbers, and special characters

for char in passwd:
    if char.isupper():
        upperCaseFound = True
    if char.islower():
        lowerCaseFound = True
    if char.isdigit():
        numericFound = True
    if not char.isalnum():
        specialFound = True
    # Stop early if all conditions are satisfied
    if upperCaseFound and lowerCaseFound and numericFound and specialFound:
        break

# Generate check output

print("- Contains atleast 1 uppercase letter:", upperCaseFound)
print("- Contains atleast 1 lowercase letter:", lowerCaseFound)
print("- Contains atleast 1 number:", numericFound)
print("- Contains atleast 1 special character:", specialFound)

# Separator

print()
print("======================================")
print()

# Giving user advice, based on check output

if len(passwd) < 12:
    print("- Try having atleast 12 characters in your password.")

if upperCaseFound == False:
    print("- Try adding atleast 1 upper case letter to your password.")

if lowerCaseFound == False:
    print("- Try adding atleast 1 lower case letter to your password!")

if numericFound == False:
    print("- Try adding atleast 1 number to your password!")

if specialFound == False:
    print("- Try adding atleast 1 special character to your password!")

if len(passwd) >= 12 and upperCaseFound == True and lowerCaseFound == True and numericFound == True and specialFound == True:
    print("Your password is very strong!")

print()