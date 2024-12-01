import turtle
import tkinter as TK


directions = "v>v<vvv<<vv^v<v>vv>v<<<^^^^^<<^<[...]"
t1 = turtle.Turtle() 
t2 = turtle.Turtle() 
t1.color("red") 
t2.color("green") 
t1._tracer(0, 0)
t2._tracer(0, 0)

visited_coords = [(0.00,0.00)]  # Count the initial home delivery as a visited place

for i, d in enumerate(directions):
    if i % 2 == 0:
        if d == "^":
            t1.setheading(90)
            t1.forward(5)
            visited_coords.append(t1.position())
        elif d == "v":
            t1.setheading(270)
            t1.forward(5)
            visited_coords.append(t1.position())
        elif d == ">":
            t1.setheading(0)
            t1.forward(5)
            visited_coords.append(t1.position())
        elif d == "<":
            t1.setheading(180)
            t1.forward(5)
            visited_coords.append(t1.position())
    else:
        if d == "^":
            t2.setheading(90)
            t2.forward(5)
            visited_coords.append(t2.position())
        elif d == "v":
            t2.setheading(270)
            t2.forward(5)
            visited_coords.append(t2.position())
        elif d == ">":
            t2.setheading(0)
            t2.forward(5)
            visited_coords.append(t2.position())
        elif d == "<":
            t2.setheading(180)
            t2.forward(5)
            visited_coords.append(t2.position())

turtle.done()


# Get a set of the visited houses to make it distinct
unique_houses = set(visited_coords)

# This ends up with negative zero coordinates, e.g. (-0.00, 120.00) which is 
# the same graphically as (0.00, 120.00) but counts as another value, so we wind
# up with duplicative values- so let's cut the negative zeros out of our visited
# locations. Tuples are immutable but lists aren't, so we convert.


unique_houses_list = []
for u in unique_houses:
    lst = list(u)
    # We're only interested in getting the decimal place to the second value
    unique_houses_list.append(("{0:.2f}".format(lst[0]), "{0:.2f}".format(lst[1])))

unified_houses_list = []
for zero in unique_houses_list:
    lst = list(zero)
    # For each coordinate, convert a negative zero to a positive zero
    if lst[0] == "-0.00":
        lst[0] = "0.00"
    if lst[1] == "-0.00":
        lst[1] = "0.00"
    unified_houses_list.append((lst[0], lst[1]))

# Now we can call set on the list and get the right amount of deliveries
print("Part Two: {}".format(len(set(unified_houses_list))))