messages = eval(input("Messages (list): "))
seen = set()
cleaned = [m for m in messages if m and not (m in seen or seen.add(m))]
print(f"Cleaned: {cleaned}")