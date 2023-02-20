import random

start_hour = 10
end_hour = 15
duration = 2

# Convert hours to minutes
start_minute = start_hour * 60
end_minute = end_hour * 60

# Calculate the range of minutes
range_minutes = end_minute - start_minute - (duration * 60)

# Select a random minute within the range
random_minute = random.randint(0, range_minutes)

# Calculate the hour and minute of the selected time
selected_minute = start_minute + random_minute
selected_hour = selected_minute // 60
selected_minute = selected_minute % 60

print(f"Selected time: {selected_hour}:{selected_minute:02}")
