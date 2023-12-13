#!/usr/bin/python3
import decimal
import math

bob = dict(name="Bob Smith", age=42, pay=30000, job="dev")

if "height" not in bob:
    print("missing height, adding")
    bob["height"] = 100

# Sort the keys
for key in sorted(bob):
    print(key, "=>", bob[key])

d = decimal.Decimal(math.pi, decimal.Context(prec=3))
print(d)
