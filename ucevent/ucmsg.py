# Handle warnings and errors
# Separate module to avoid circular imports
import sys
import fnmatch

quiet = False
debug = None

def debug_msg(x, y):
    if debug and any([fnmatch.fnmatch(x, p) for p in debug.split(",")]):
        print("debug:", x + ": " + str(y), file=sys.stderr)

def warning(x):
    if not quiet:
        print("WARNING:", x, file=sys.stderr)
