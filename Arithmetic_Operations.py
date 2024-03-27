print(10 + 3)
print(10 / 3)
print(10 // 3)  # turns the floating point number into integer
print(5 // 2)   # rounds down to nearest whole number
print(5 % 2)    # modulus: returns the remainder of the division
print(5 ** 2)   # exponent: 5^2

# Augmented assignment operator
x = 10
x = x + 3    # this is how we can increment a number
print(x)
x += 3
print(
x -= 3
print(x)

# Operator Precedence:  Please Excuse My Dear Aunt Sally
x = 10 + 3 * 2
print(x)  #   =16
x = (10 + 3) * 2 ** 2
print(x)