

print("Swimming Pool Entry Checker")

age = int(input("Enter your age: "))
swim = input("Can you swim? (yes/no): ")
adult = input("Is an adult with you? (yes/no): ")

if age < 4:
    print("Use the splash pool.")
elif age < 12:
    print("Use the main pool with an adult.")
elif age < 18:
    print("Use the main pool if you can swim.")
else:
    print("You can use all pools.")

if swim == "yes" and adult == "yes":
    print("You can use the deep pool.")

if swim == "no" or age < 12:
    print("Stay in the shallow end.")

if adult == "no":
    print("Find an adult.")

print("Have a safe swim!")
