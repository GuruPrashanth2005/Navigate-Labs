import sys

if sys.version_info < (3,8):
    sys.exit("Unsupported")
print("Supported")
