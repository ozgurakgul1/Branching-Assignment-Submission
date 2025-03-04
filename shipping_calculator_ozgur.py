# Express Shipping Cost Estimator
# Developer: Michael Chen
# Version: 1.0.3

# Show program introduction
print("Welcome to Package Express. Please follow the instructions below.")

# Input validation for package weight
parcel_weight = float(input("Please enter the package weight:\n"))

# Maximum weight check
if parcel_weight > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()

# Gather package dimensions
parcel_width = float(input("Please enter the package width:\n"))
parcel_height = float(input("Please enter the package height:\n"))
parcel_length = float(input("Please enter the package length:\n"))

# Calculate combined dimensions
combined_size = parcel_width + parcel_height + parcel_length

# Maximum size check
if combined_size > 50:
    print("Package too big to be shipped via Package Express.")
    exit()

# Calculate shipping rate
# Rate formula: (width * height * length * weight) / 100
shipping_rate = (parcel_width * parcel_height * parcel_length * parcel_weight) / 100

# Output the shipping cost
print(f"Your estimated total for shipping this package is: ${shipping_rate:.2f}")
print("Thank you!") 