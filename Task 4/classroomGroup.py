n = int(input("Number of students: "))
preferences = {input(f"Student {i+1}: "): set(input("Preferences: ").split(", ")) for i in range(n)}
mutual = [(s1, s2) for s1 in preferences for s2 in preferences[s1] if s1 in preferences.get(s2, set()) and s1 < s2]
all_students = set(preferences.keys())
chosen_students = set().union(*preferences.values())
isolated = all_students - chosen_students
print(f"Mutual preferences: {mutual if mutual else 'None'}")
print(f"Isolated students: {isolated if isolated else 'None'}")