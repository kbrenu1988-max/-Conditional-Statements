temperature = int(input("Enter today's temperature in Celcius:"))

if temperature > 20:
    outfit = " jacket"
    print("It is cold today")
    print("Wear a", outfit)
else:
    outfit = " T-shirt"
    print("It is warm today")
    print("Wear a", outfit)

is_it_raining = input("Is it raining today (yes/no):")
if is_it_raining == "yes":
    print("Bring an umbrella")

wind_speed = int(input("Enter the wind speed in km/h:"))
if wind_speed > 30:
    need_windbreaker = "yes"
    print("It is windy")
    print("Wear a windbreaker over your",outfit)
else:
    need_windbreaker = "no"
    print("It is calm today")
    print("No windbreaker needed over your",outfit)

has_puddles = input("Are there any puddles on the ground (yes/no):")
if has_puddles == "yes":
    shoes = " boots"
    print("The ground is wet")
    print("Wear", shoes)
else:
    shoes = " sneakers"
    print("The ground is dry")
    print("Wear", shoes)

print("")
print("Weather check complete")

print("===== Weather Outfit Picker ====")
print("Temperature: ", temperature)
print("Outfit chosen: ", outfit)
print("Raining: ", is_it_raining)
print("Windbreaker needed: ", need_windbreaker)
print("Shoes chosen: ", shoes)
print("================================")