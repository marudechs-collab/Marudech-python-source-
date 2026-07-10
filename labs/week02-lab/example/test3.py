print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

#input
second = int(input("second:"))

#process
hour = second // 3600
second_remain = second % 3600

minute = second_remain // 60
second_remain = second % 60

#output
print(second,"seconds =",hour,"hour",minute,"mimute",second_remain,"second")