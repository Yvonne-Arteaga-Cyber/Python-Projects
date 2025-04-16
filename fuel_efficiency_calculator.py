odometer_initial = int(input("Please enter the starting odometer reading: "))

print("Please enter your odometer reading and gallons of gas used on each leg of the trip.")
print("When you have entered data for all the legs, then enter -1 for any of them.")

mpg = []
total_distance = 0
total_gallon = 0

while 1:
    odometer_new = int(input("Enter odometer reading: "))
    gallon_used = int(input("Enter gallons used: "))

    if odometer_new == -1 or gallon_used == -1:
        break

    distance = odometer_new - odometer_initial
    mpg_val = distance / gallon_used
    mpg.append(mpg_val)

    odometer_initial = odometer_new
    total_distance += distance
    total_gallon += gallon_used

for i in range(len(mpg)):
    print(f"The mpg for leg {i+1} of the journey is: ", "{0:.2f}".format(mpg[i]))

print("The total mpg for this trip is: ", "{0:.2f}".format(total_distance / total_gallon))
