# requests input for city_flight
city_flight = input("Enter the city your flying to: ")
# requests input for num_nights
while True:
    try:
        num_nights = int(input("Enter the number of nights you're staying: "))
        break
    except ValueError:
        print("Please enter a valid integer for the number of nights.")

# requests input for rental_days
while True:
    try:
        rental_days = int(input("Enter the number of days you would like to rent the vehicle: "))
        break
    except ValueError:
        print("Please enter a valid integer for the number of rental days.")

# calculate the total cost for the number of nights at the hotel
def hotel_cost(num_nights):
    cost_per_night = int(10)
    hotel_total = num_nights * cost_per_night 
    return hotel_total

#calcuate the cost of the flight
def plane_cost(city_flight):
    city_flight = city_flight.lower()
    while True:
        if city_flight == "new york":
            flight_cost = int(75)
        elif city_flight == "los angeles":
            flight_cost = int(100)
        elif city_flight == "london":
            flight_cost = int(50)
            return flight_cost
        else:
            print(f"Sorry, we currently do not offer flights to {city_flight}."
            "Please enter a valid city from New York, Los Angeles or London")
            city_flight = input("Please enter a valid city from New York, Los Angeles or London: ")
            return False  # Return False for invalid city names

# calculate the cost of the total days renting the vehicle
def car_rental(rental_days):
    daily_rental_cost = int(15)
    rental_total = rental_days * daily_rental_cost
    return rental_total

# calucate the total cost of the holiday
def holiday_cost():

    hotel_total = hotel_cost(num_nights)
    flight_total = plane_cost(city_flight)
    rental_total = car_rental(rental_days)

    total_cost = hotel_total + flight_total + rental_total

    print(f"Your flight to {city_flight} will cost £{flight_total},"
           f" your stay at the hotel will come to £{hotel_total}"
          f" and the cost of the rental care comes to £{rental_total}."
          f"\n This comes to a total of £{total_cost}")


holiday_cost()







