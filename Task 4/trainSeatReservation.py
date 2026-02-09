reservations = eval(input("Reservations (list of tuples): "))
seats = [s for _, s in reservations]
dup_seats = [s for s in set(seats) if seats.count(s) > 1]
coach_seats = {}
for c, s in reservations:
    if c not in coach_seats:
        coach_seats[c] = set()
    coach_seats[c].add(s)
print(f"Duplicate seats: {dup_seats if dup_seats else 'None'}")
print(f"Seats per coach: {coach_seats}")