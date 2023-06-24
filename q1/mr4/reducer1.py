#!/usr/bin/python
import sys

# Initialize variables to keep track of the current color and count
current_color = None
current_count = 0

# Iterate over the lines of the standard input
for line in sys.stdin:
    color, count = line.strip().split("\t")
    count = int(count)
    # Check if the color is the same as the current color
    if color == current_color:
        current_count += count
    else:
        # If the color is different, emit the current color and count
        if current_color:
            print("{0}\t{1}".format(current_color,current_count))
        # Update the current color and count
        current_color = color
        current_count = count

# Emit the last color and count
if current_color:
    print("{0}\t{1}".format(current_color,current_count))
