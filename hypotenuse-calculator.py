"""
Author: Gonçalo Cunha (GitHub: GCunha23)
Date Created: 20/03/2026
Last Modified: 20/03/2026

Description:
This is a hypotenuse calculator.
"""

# Pythagorean theorem calculator

a = int(input("Side 'a' size (in cm): "))
b = int(input("Side 'b' size (in cm): "))
c = (a ** 2 + b ** 2) ** 0.5

print(c)