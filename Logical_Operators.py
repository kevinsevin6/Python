########   Logical Operators  #######
# AND
high_income = False
GOOD_credit = False

if high_income and GOOD_credit:
    print("Eligible for loan")
else:
    print("No loan:(")

# OR
if high_income or GOOD_credit:
    print("Well I guess")
else:
    print("Definitely not")

# NOT    -   reverses any boolean value
# ex.) If good credit and doesn't have a criminal record
good_CREDIT = True
criminal = False
if good_CREDIT and not criminal:
    print("yes")
else:
    print('no')