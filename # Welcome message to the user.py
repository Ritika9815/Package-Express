# Welcome message to the user
print("Welcome to Package Express. Please follow the instructions below.")

# Prompting user for package weight
weight = float(input("Please enter the package weight: "))

# Check if the weight exceeds the limit
if weight > 50:
    # Display an error message and exit if the package is too heavy
    print("Package too heavy to be shipped via Package Express. Have a good day.")
else:
    # Prompting user for package dimensions
    width = float(input("Please enter the package width: "))
    height = float(input("Please enter the package height: "))
    length = float(input("Please enter the package length: "))

    # Check if the total dimensions exceed the limit
    if width + height + length > 50:
        # Display an error message and exit if the package is too large
        print("Package too big to be shipped via Package Express.")
    else:
        # Calculate the shipping cost
        volume = width * height * length
        quote = (volume * weight) / 100

        # Display the calculated quote to the user
        print(f"Your estimated total for shipping this package is: ${quote:.2f}")
        print("Thank you!")
