"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
<<<<<<< HEAD

def get_temperaturn():
    temps = (23, 21, 25, 23, 24, 22.2, 21)
    return temps

def analyze_temps(temp_list):
    avg = sum(temp_list) / len(temp_list)
    high = max(temp_list)
    low = min(temp_list)
    return avg, high, low

def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week:")
    print(f"Average: {avg}c")
    print(f"High: {high}c")
    print(f"Low: {low}c")

=======
    
>>>>>>> upstream/main
