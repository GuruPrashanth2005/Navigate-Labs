readings = eval(input("Sensor readings (list of dicts): "))
if not readings:
    print("No readings")
else:
    first_keys = set(readings[0].keys())
    consistent = all(set(r.keys()) == first_keys for r in readings)
    faulty = [i for i, r in enumerate(readings) if set(r.keys()) != first_keys]
    print(f"Consistent: {consistent}")
    print(f"Faulty indices: {faulty if faulty else 'None'}")