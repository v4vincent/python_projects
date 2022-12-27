import random

# List of names
names = ['Nicole', 'Vincent', 'Charlie', 'Clarence', 'Carlo', 'Mom', 'Dad', 'Eliza']

# Dictionary to store the random numbers for each name
name_to_number = {}

# Assign a random number to each name
for name in names:
  name_to_number[name] = random.randint(1, 9)

# Print out the name and corresponding random number for each name
for name, number in name_to_number.items():
  print(f'{name}: {number}')
