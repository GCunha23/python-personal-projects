"""
Author: Gonçalo Cunha (GitHub: GCunha23)
Date Created: 20/03/2026
Last Modified: 20/03/2026

Description:
This is a BMI calculator.
"""

mass = float(input("Enter your current weight in kilos (Format: xx.x): "))
height = float(input("Enter your current height in meters (Format: x.xx): "))
bmi = mass / (height ** 2)

print(bmi)