import math

# Function to get coordinates from the user for each point
def get_coordinates(num_sides):
    coordinates = {}
    for i in range(num_sides):
        point = input(f"Enter the coordinates for point {chr(65+i)} (format: x,y): ")
        x, y = map(float, point.split(','))
        coordinates[chr(65+i)] = (x, y)
    return coordinates

# Function to calculate the area of the polygon
def find_area(coordinates):
    area = 0
    n = len(coordinates)

    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]

        area += (x1 * y2 - x2 * y1)

    return abs(area) / 2

# Get the number of sides from the user
num_sides = int(input("Enter the number of sides of the polygon: "))

# Get the coordinates for each point from the user
coordinates = get_coordinates(num_sides)

# Calculate and print the area of the polygon
area = find_area(list(coordinates.values()))
print(f"The area of the polygon is: {area}")
