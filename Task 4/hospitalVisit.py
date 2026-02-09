visits = eval(input("Patient visits (list of dicts): "))
doctor_visits = {}
for v in visits:
    doctor_visits[v['doctor']] = doctor_visits.get(v['doctor'], 0) + v['visit_count']
max_patient = max(visits, key=lambda v: v['visit_count'])
print(f"Doctor-wise visits: {doctor_visits}")
print(f"Patient with most visits: {max_patient['patient_id']} ({max_patient['visit_count']})")