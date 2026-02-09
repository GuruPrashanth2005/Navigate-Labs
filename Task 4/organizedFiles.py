files = eval(input("Filenames (list): "))
organized = {}
for f in files:
    ext = f.split('.')[-1] if '.' in f else 'no_ext'
    if ext not in organized:
        organized[ext] = []
    organized[ext].append(f)
print(f"Organized: {organized}")