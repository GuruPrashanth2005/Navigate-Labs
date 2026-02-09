device_logs = eval(input("Device status logs (device_id: [status]): "))
went_off = [d for d, statuses in device_logs.items() if 'OFF' in statuses]
always_on = [d for d, statuses in device_logs.items() if all(s == 'ON' for s in statuses)]
print(f"Devices that went OFF: {went_off if went_off else 'None'}")
print(f"Always ON: {always_on if always_on else 'None'}")