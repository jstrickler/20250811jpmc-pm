"""
Module documentation...
"""
import sys

def add(x, y):
    return x + y

# this is a wrapper that is used to create the callable cli version of the function
def _cli_add():  # name can be anything
    args = [float(x) for x in sys.argv[1:]]
    result = add(*args)  # call the 'real' function
    print(result)

if __name__ == "__main__":
    # the code in this block (and all the code above) will be run when
    # either
    #    python supercalc.py
    # or 
    #    python -m supercalc
    # is executed, but NOT when imported like
    #    import supercalc
    print(f"Hello from {__file__}")
