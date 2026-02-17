import sys

required_version = (3, 8)

if sys.version_info < required_version:
    print("Python version not supported")
    sys.exit()

print("Environment Supported")
