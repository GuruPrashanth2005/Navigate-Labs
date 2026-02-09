passengers = eval(input("Passenger counts per stop (list): "))
max_stop = passengers.index(max(passengers)) + 1
avg = sum(passengers) / len(passengers)
below_avg = [i + 1 for i, p in enumerate(passengers) if p < avg]
print(f"Stop with max passengers: Stop {max_stop}")
print(f"Stops below average: {below_avg}")