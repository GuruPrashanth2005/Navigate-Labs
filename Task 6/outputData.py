import os

folder = "output_data"

if not os.path.exists(folder):
    os.makedirs(folder)

print("Folder Ready")
