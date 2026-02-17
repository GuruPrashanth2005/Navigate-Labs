import sys

if len(sys.argv) < 2:
    print("No configuration provided")
    sys.exit()

config_value = sys.argv[1]
print("Configuration Value:", config_value)
