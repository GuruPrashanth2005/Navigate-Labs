delays = eval(input("Flight delays (flight_id: [delay_minutes]): "))
avg_delay = {f: sum(d) / len(d) for f, d in delays.items()}
max_flight = max(avg_delay, key=avg_delay.get) if avg_delay else None
print(f"Average delay per flight: {avg_delay}")
print(f"Highest average: {max_flight} ({avg_delay[max_flight]:.2f} min)")