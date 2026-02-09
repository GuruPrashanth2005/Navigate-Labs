pollution = eval(input("Pollution data (city: [AQI_values]): "))
avg_aqi = {city: sum(values) / len(values) for city, values in pollution.items()}
worst_city = min(avg_aqi, key=avg_aqi.get) if avg_aqi else None
print(f"Average AQI per city: {avg_aqi}")
print(f"Worst air quality: {worst_city} ({avg_aqi[worst_city]:.2f})")