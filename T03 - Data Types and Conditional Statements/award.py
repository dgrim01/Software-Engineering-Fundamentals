#asks the user to enter the minutes taken for each of the 3 events
swimming = int(input("Enter the minutes taken for swimming: "))
cycling = int(input("Enter the minutes taken for cycling: "))
running = int(input("Enter the minutes taken for running: "))
#the sum of time taken for each event in the triathalon
total_time = swimming + cycling + running
#Displays the total time to complete the triathalon
print(f"Total Time: {total_time} minutes ")

if total_time <= 100:
    print(" Qualifying criteria: Within the qualifying time")
    print("Award: Provincial colours")
elif total_time >= 101 and total_time <= 105:
    print(" Qualifying criteria: Within five minutes of the qualifying time")
    print("Award: Provincial half colours")
elif total_time >= 106 and total_time <= 110:
    print(" Qualifying criteria: Within ten minutes of the qualifying time")
    print("Award: Provincial scroll")
elif total_time >= 111:
    print(" Qualifying criteria: More than then minutes off the qualifying time")
    print("Award: No award")
else:
    print("No qualifying criteria met")

