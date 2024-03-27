weight = float(input("Enter weight: "))
unit = input("Is this in lbs or kg? ")

if unit.lower() == 'kg':
    wt_lb = weight * 2.2
    print(f"That is {wt_lb} in lbs")
elif unit.lower() == 'lbs':
    wt_kg = weight * 0.4536
    print(f"That is {wt_kg} in kgs")
else:
    print("Huh?")