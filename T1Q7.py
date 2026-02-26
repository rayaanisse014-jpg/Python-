distance = float(input('Distance from home to uni (km): '))
Speed_to_uni = float(input('Speed from home to uni (km/h): '))
Speed_to_home = float(input('Speed from uni to home (km/h): '))

# Calculate the time taken to get to uni / and the time taken to get home.
time_to_uni = distance / Speed_to_uni
time_to_home = distance / Speed_to_home

# Calculate the total travel time, which is the sum of the two time values you just calculated.
total_time = time_to_uni + time_to_home

# Calculate the total distance, which is twice the distance from home to uni
total_distance = 2 * distance

# Calculate the average speed, by dividing the distance by the time.
average_speed = total_distance / total_time

# Display the average speed, with two decimal places.
print(f"The average speed for the round trip was {average_speed:.2f} km/h.")


