# Map function in python applies a given function to each item of an iterable(like a list, tuple, etc) and returns a map object (which is an iterator)


z, x, c = map(int, input().split())
if c > x or c > z :
    print("PASS")

else:
    print("FAIL")


