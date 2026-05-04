capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
    "UK": "London"
}

print("===== PART 2 =====")

result = capitals.get("India")
if result:
    print(f"The capital of India is {result}")
else:
    print("That capital doesn't exist")

result = capitals.get("Brazil")
if result:
    print(f"The capital of Brazil is {result}")
else:
    print("That capital doesn't exist")

print("\n===== PART 3 =====")

capitals.update({"France": "Paris"})
capitals.update({"Japan": "Tokyo"})
capitals.update({"Canada": "Ottawa"})

capitals.update({"USA": "Washington D.C."})

print(capitals)

print("\n===== PART 4 =====")

capitals.pop("China")
capitals.popitem()

capitals.pop("Russia")

print(capitals)

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
    "UK": "London"
}

print("\n===== PART 5A - All Countries =====")
for key in capitals.keys():
    print(f"Country: {key}")

print("\n===== PART 5B - All Capitals =====")
for value in capitals.values():
    print(value)

print("\n===== PART 5C - Country and Capital =====")
for key, value in capitals.items():
    print(f"{key}: {value}")

print("\n===== PART 6 =====")

capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Canada": "Ottawa",
    "Brazil": "Brasilia"
}

country = input("\nEnter a country name: ")

capital = capitals.get(country)

if capital:
    print(f"The capital of {country} is {capital}")
else:
    print("Sorry, that country is not in the dictionary.")

    answer = input("Would you like to add it? (yes/no): ")

    if answer.lower() == "yes":
        new_capital = input(f"Enter the capital of {country}: ")
        capitals.update({country: new_capital})
        print(f"{country} has been added!")
        print(capitals)
    else:
        print("OK, no changes made.")