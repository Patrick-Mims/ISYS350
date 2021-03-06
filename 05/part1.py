#!/usr/bin/python

import financialService as fs

presentValue = int(input("Present Value: "))
interestRate = float(input("Interest Rate (Enter 10% as 0.10): "))
targetFutureValue = int(input("Target Future Value: "))

years = fs.goalSeek(presentValue, interestRate, targetFutureValue)

output = "It will take you a total of {:,.0f} years to reach your target."

print(output.format(years))

print("\nPart B")
prop_value = int(input("Enter property value (2000): "))
prop_life = int(input("Enter property life (10): "))

fs.showDepreciationTable(prop_value, prop_life)
