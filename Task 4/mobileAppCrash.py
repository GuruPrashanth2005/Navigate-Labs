reports = eval(input("Crash reports (list of dicts): "))
high_severity = [r for r in reports if r['severity'] == 'HIGH']
crash_count = {}
for r in reports:
    crash_count[r['app_version']] = crash_count.get(r['app_version'], 0) + 1
print(f"High severity reports: {len(high_severity)}")
print(f"Crashes per version: {crash_count}")