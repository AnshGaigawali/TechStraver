def inches_to_centimeters(inches):
    return format(inches * 2.54,".2f")

def centimeters_to_inches(centimeters):
    return format(centimeters / 2.54,".2f")

def feet_to_meters(feet):
    return format(feet * 0.3048,".2f")

def meters_to_feet(meters):
    return format(meters / 0.3048,".2f")

def yards_to_meters(yards):
    return format(yards * 0.9144,".2f")

def meters_to_yards(meters):
    return format(meters / 0.9144,".2f")

def miles_to_kilometers(miles):
    return format(miles * 1.60934,".2f")

def kilometers_to_miles(kilometers):
    return format(kilometers / 1.60934,".2f")

def repeat():
    print("Do you want to continue? (Yes=1/No=0)")
    return int(input())

print("Welcome to the Unit Converter!")
print("1. Inches to Centimeters")
print("2. Centimeters to Inches")
print("3. Feet to Meters")
print("4. Meters to Feet")
print("5. Yards to Meters")
print("6. Meters to Yards")
print("7. Miles to Kilometers")
print("8. Kilometers to Miles")

r=1
while r==1:
    choice = input("Enter your choice : ")
    if choice == '1':
        inches = float(input("Enter inches: "))
        print("Centimeters:", inches_to_centimeters(inches))
        r=repeat()
    elif choice == '2':
        centimeters = float(input("Enter centimeters: "))
        print("Inches:", centimeters_to_inches(centimeters))
        r=repeat()
    elif choice == '3':
        feet = float(input("Enter feet: "))
        print("Meters:", feet_to_meters(feet))
        r=repeat()
    elif choice == '4':
        meters = float(input("Enter meters: "))
        print("Feet:", meters_to_feet(meters))
        r=repeat()
    elif choice == '5':
        yards = float(input("Enter yards: "))
        print("Meters:", yards_to_meters(yards))
        r=repeat()
    elif choice == '6':
        meters = float(input("Enter meters: "))
        print("Yards:", meters_to_yards(meters))
        r=repeat()        
    elif choice == '7':
        miles = float(input("Enter miles: "))
        print("Kilometers:", miles_to_kilometers(miles))
        r=repeat()
    elif choice == '8':
        kilometers = float(input("Enter kilometers: "))
        print("Miles:", kilometers_to_miles(kilometers))
        r=repeat()
    else:
        print("Invalid choice")
        r=repeat()

