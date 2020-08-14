str = input("Enter your day: ")
week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
week.append("superday")
print("Your Weekday is: " + week[int(str)-1])
print("\n")

def say_hi():
    print("Hello World")

say_hi()