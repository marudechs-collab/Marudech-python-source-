# Example 3: Mathematical function
def calculate_triangle_area(height, width):
    """Calculates and displays triangle area"""
    area = 0.5 * height * width
    print(f"triangle with height {height} and width {width}")
    print(f"Area = {height} × {width} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)

print("----------------------------------------------------------------")

def calculate_circle_area(r):
    """Calculates and displays circle area"""
    area = 3.14 * r**2
    print(f"Radius = {r}")
    print(f"Area = 3.14 * r**2 = {area}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5) # = r
calculate_circle_area(10) # = r

print("----------------------------------------------------------------")