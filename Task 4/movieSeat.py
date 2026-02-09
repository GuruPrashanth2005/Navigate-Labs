bookings = eval(input("Bookings (show_time: set([seat_numbers])): "))
all_seats = set().union(*bookings.values()) if bookings else set()
fully_booked = [t for t, seats in bookings.items() if len(seats) == len(all_seats)]
common_seats = set(bookings[next(iter(bookings))]).intersection(*bookings.values()) if bookings and len(bookings) > 1 else (set(bookings[next(iter(bookings))]) if bookings else set())
print(f"Fully booked: {fully_booked if fully_booked else 'None'}")
print(f"Booked in every show: {common_seats if common_seats else 'None'}")