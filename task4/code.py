print("SMART PARKING FEE MANAGEMENT")

vehicle = input("Enter vehicle category (bike/car): ").lower()

entry = int(input("Enter entry hour (0-23): "))
exit_time = int(input("Enter exit hour (0-23): "))

if entry < 0 or entry > 23 or exit_time < 0 or exit_time > 23:
    print("Invalid time input")

elif exit_time == entry:
    print("Parking duration cannot be zero")

elif vehicle not in ["bike", "car"]:
    print("Invalid vehicle category")

else:
    if exit_time < entry:
        duration = (24 - entry) + exit_time
    else:
        duration = exit_time - entry

    print("Parking Duration:", duration, "hours")

    if vehicle == "bike":
        fee = duration * 10
        daily_limit = 200

    else:
        fee = duration * 20
        daily_limit = 400

    if fee > daily_limit:
        fee = daily_limit

    print("Vehicle Category:", vehicle)
    print("Total Parking Fee: Rs.", fee)

print("Thank you!")
