import os
import svgwrite
import math
import random
import argparse
from svgwrite import rgb

# Article this is from
# https://pdfs.semanticscholar.org/42a8/8a9d598fc051ecce86f508ad63e842944a81.pdf?_ga=2.196276580.997108618.1594162811-122912770.1594162811

parser = argparse.ArgumentParser(description="Pretty geometries")
parser.add_argument(
    "-s",
    "--shape",
    dest="shape",
    action="store",
    help="the general shape to create - (circle, diamond, cube, flower, triangle, spiral)",
)
parser.add_argument(
    "-l",
    "--label",
    dest="label",
    action="store_true",
    help="adds index numbers to the points",
)
parser.add_argument(
    "-m", "--math", dest="math", action="store_true", help="prints the maths"
)
parser.add_argument(
    "-p",
    "--points",
    dest="n",
    action="store",
    help="number of points to use",
    default=300,
    type=int,
)

args = parser.parse_args()

"""
Tangents but circles are overlapping - not sure whats going on
print(wut(21,z,x)) == print(wut(5,z,x)) 
mult = 100
r0 = 1*mult
x = 0.61803398875
z = 1.027422
zrad = z
rad0 = 0.2840076665365131*mult
"""

"""
Harmony
print(wut(13,z,x)) == print(wut(8,z,x)) == rad0
mult = 100
r0 = 1*mult
x = 0.61803398875
z = 1.027422
zrad = z
rad0 = 0.2039746541988191*mult
"""

g_angle = 360 / math.pow((1 + math.sqrt(5)) / 2, 2)
g_ratio = 1 - g_angle / 360
out_file = "images/test.svg"


def main():
    if args.shape:
        dwg = svgwrite.Drawing(out_file, profile="full")

        if args.shape == "circle":
            # 13 and 8 parastichy
            phyllo_tangent(
                dwg=dwg, n=args.n, z=1.02742392, radius=0.2039746541988191, growth=10
            )
        elif args.shape == "diamond":
            phyllo_diamond(dwg=dwg, n=args.n, z=1.02742392, growth=5)
        elif args.shape == "cube":
            phyllo_cube(dwg=dwg, n=args.n, z=1.02742392, growth=5)
        elif args.shape == "triangle":
            phyllo_triangle(dwg=dwg, n=args.n, z=1.02742392, growth=5)
        elif args.shape == "flower":
            phyllo_flower(dwg=dwg, n=args.n, z=1.02742392, growth=5)
        elif args.shape == "spiral":
            phyllo_spiral(dwg=dwg, n=args.n, z=1.02742392, growth=10)
        elif args.shape == "test":
            phyllo_test(dwg=dwg, n=args.n, z=1.02742392, growth=10)
        else:
            print("Shape unknown")
            exit()

        if args.label:
            print_labels(dwg=dwg, n=300, z=1.02742392, growth=5)

        dwg.save()

        os.system("open {}".format(out_file))
    else:
        print("Gimme a shape to make... or use --help (-h)")
        exit()

    if args.math:
        print(f_mzx(13, 1.02742392, g_ratio))
        print(f_mzx(8, 1.02742392, g_ratio))


def print_labels(dwg, z, growth, n):
    for i in reversed(range(0, n)):
        coord = phyllo_center(z, growth, i)
        dwg.add(dwg.text(text=str(i), insert=coord))


def phyllo_test(dwg, z, growth, n):
    for i in reversed(range(0, n)):
        coord = phyllo_center(z, growth, i)
        coord1 = phyllo_center(z, growth, i + 1)
        coord2 = phyllo_center(z, growth, i + 2)
        coord3 = phyllo_center(z, growth, i + 3)
        coord5 = phyllo_center(z, growth, i + 5)
        coord8 = phyllo_center(z, growth, i + 8)
        coord13 = phyllo_center(z, growth, i + 13)
        coord21 = phyllo_center(z, growth, i + 21)

        path = dwg.path(
            d="M{},{}".format(coord[0], coord[1]),
            stroke="black",
            fill="none",
            stroke_width=stroke_width(coord, coord),
        )
        add_arc_to_path(path, coord13, coord, 1)
        add_arc_to_path(path, coord5, coord13, 1)
        dwg.add(path)


def phyllo_spiral(dwg, z, growth, n):
    for i in reversed(range(0, n)):
        coord = phyllo_center(z, growth, i)
        coord1 = phyllo_center(z, growth, i + 1)
        coord2 = phyllo_center(z, growth, i + 2)
        coord3 = phyllo_center(z, growth, i + 3)
        coord5 = phyllo_center(z, growth, i + 5)
        coord8 = phyllo_center(z, growth, i + 8)
        coord13 = phyllo_center(z, growth, i + 13)
        coord21 = phyllo_center(z, growth, i + 21)

        # 5,8,13 makes the best pattern
        # add_arc(dwg, coord1, coord)
        # add_arc(dwg, coord, coord2)
        # add_arc(dwg, coord3, coord)
        # add_arc(dwg, coord, coord5)
        # add_arc(dwg, coord8, coord)
        # add_arc(dwg, coord, coord13)
        # add_arc(dwg, coord21, coord)

        path = dwg.path(
            d="M{},{}".format(coord[0], coord[1]),
            stroke="black",
            fill="blue",
            stroke_width=stroke_width(coord, coord),
        )
        add_arc_to_path(path, coord8, coord, 0)
        add_arc_to_path(path, coord13, coord8, 1)
        add_arc_to_path(path, coord, coord13, 0)
        dwg.add(path)


def phyllo_triangle(dwg, z, growth, n):
    for i in reversed(range(0, n)):
        coord = phyllo_center(z, growth, i)
        coord5 = phyllo_center(z, growth, i + 5)
        coord8 = phyllo_center(z, growth, i + 8)
        coord13 = phyllo_center(z, growth, i + 13)

        add_line(dwg, coord, coord5)
        add_line(dwg, coord, coord8)
        add_line(dwg, coord, coord13)


def phyllo_diamond(dwg, z, growth, n):
    for i in reversed(range(0, n)):
        coord = phyllo_center(z, growth, i)
        coord8 = phyllo_center(z, growth, i + 8)
        coord13 = phyllo_center(z, growth, i + 13)

        add_line(dwg, coord, coord8)
        add_line(dwg, coord, coord13)


def phyllo_cube(dwg, z, growth, n):
    for i in reversed(range(0, n)):
        coord = phyllo_center(z, growth, i)
        coord5 = phyllo_center(z, growth, i + 5)
        coord8 = phyllo_center(z, growth, i + 8)
        coord13 = phyllo_center(z, growth, i + 13)

        if i % 3 == 0:
            add_line(dwg, coord, coord5)
            add_line(dwg, coord, coord8)
            add_line(dwg, coord, coord13)
        elif i % 3 == 1:
            add_line(dwg, coord, coord5)
            add_line(dwg, coord, coord8)
        else:
            add_line(dwg, coord, coord13)


def phyllo_flower(dwg, z, growth, n):
    for i in reversed(range(0, n)):
        coord = phyllo_center(z, growth, i)
        coord8 = phyllo_center(z, growth, i + 8)
        coord13 = phyllo_center(z, growth, i + 13)

        if i % 3 == 0:
            add_line(dwg, coord, coord8)
            add_line(dwg, coord, coord13)
        elif i % 3 == 2:
            add_line(dwg, coord, coord8)
        else:
            add_line(dwg, coord, coord13)


def add_line(dwg, c1, c2):
    path = dwg.path(
        d="M{},{}L{},{}".format(c1[0], c1[1], c2[0], c2[1]),
        stroke="black",
        fill="none",
        stroke_width=stroke_width(c1, c2),
    )
    dwg.add(path)


def add_arc(dwg, c1, c2):
    r1 = math.sqrt(math.pow(c1[0], 2) + math.pow(c1[1], 2))
    r2 = math.sqrt(math.pow(c2[0], 2) + math.pow(c2[1], 2))
    path = dwg.path(
        d="M{},{}".format(c2[0], c2[1]),
        stroke="black",
        fill="none",
        stroke_width=stroke_width(c1, c2),
    )
    r0 = (r1 + r2) / 2  # this seems to line up the arcs no idea why
    path.push("A{},{},0,0,0,{},{}".format(r0, r0, c1[0], c1[1]))
    dwg.add(path)


def add_arc_to_path(path, c1, c2, invert):
    r1 = math.sqrt(math.pow(c1[0], 2) + math.pow(c1[1], 2))
    r2 = math.sqrt(math.pow(c2[0], 2) + math.pow(c2[1], 2))
    r0 = (r1 + r2) / 2  # this seems to line up the arcs no idea why
    path.push("A{},{},0,0,{},{},{}".format(r0 * 2, r0 * 2, invert, c1[0], c1[1]))


def stroke_width(c1, c2):
    return math.sqrt(math.pow(c1[0], 2) + math.pow(c1[1], 2)) / 50


def phyllo_center(z, growth, index):
    x = g_ratio
    r = growth * math.pow(z, index)
    theta = 2 * math.pi * index * x
    cx = r * math.cos(theta)
    cy = r * math.sin(theta)
    return [cx, cy]


# creates tangential circles in a phyllotaxis arrangement
def phyllo_tangent(dwg, z, radius, growth, n):
    rad0 = radius * growth
    r0 = 1 * growth
    x = g_ratio
    zrad = z

    for i in reversed(range(0, n)):
        rad = rad0 * math.pow(zrad, i)
        r = r0 * math.pow(z, i)
        theta = 2 * math.pi * i * x
        cx = r * math.cos(theta)
        cy = r * math.sin(theta)
        circle(dwg, i, n, cx, cy, rad, rad / growth)
        # inner_shape(dwg, cx, cy, rad, theta, rad/growth)


# cx, cy = center of circle
# index = the index of this point in all points
# total = total points
def circle(dwg, index, total, cx, cy, rad, line_width):
    circle = dwg.circle(
        center=(cx, cy),
        r=rad,
        stroke="#000",
        # ignore RED
        # GREEN different for each 8-parastichy
        # BLUE gradient inside to outside
        # fill=rgb(255,index%8/8*155 + 80,index/total*205 + 40),
        # close to random looking, still pretty
        # fill=rgb(255,index%8/8*95 + 80,index%13/13*95 + 80),
        fill="none",
        stroke_width=4,
        # stroke_width=line_width
    )
    dwg.add(circle)


def inner_shape(dwg, x0, y0, rad, rotation, line_width):
    path = dwg.path(
        d="M{},{}".format(x0, y0),
        stroke="#52802f",
        fill="none",
        stroke_width=line_width,
        transform="rotate({}, {}, {})".format(math.degrees(rotation), x0, y0),
    )
    # inner_smile(path, x0, y0, rad)

    n_circ = 7  # number of concentric circles
    smallest_reduc = 1 / 7  # fraction of size of smallest vs largest circles
    for i in range(0, n_circ):
        reduc = smallest_reduc + i * (1 - smallest_reduc) / n_circ
        concentric_circles(
            dwg, x0 + rad * (1 - reduc), y0, x0, y0, rad * reduc, rotation, line_width
        )

    dwg.add(path)


def concentric_circles(dwg, x0, y0, rx, ry, rad, rotation, line_width):
    circle = dwg.circle(
        center=(x0, y0),
        r=rad,
        stroke="#000",
        fill="none",
        stroke_width=line_width,
        transform="rotate({}, {}, {})".format(math.degrees(rotation), rx, ry),
    )
    dwg.add(circle)


def inner_square(path, x0, y0, rad):
    path.push("M{},{}".format(x0, y0 + rad))
    path.push("L{},{}".format(x0 + rad, y0))
    path.push("L{},{}".format(x0, y0 - rad))
    path.push("L{},{}".format(x0 - rad, y0))
    path.push("L{},{}".format(x0, y0 + rad))


def inner_smile(path, x0, y0, rad):
    path.push("M{},{}".format(x0 + 0.3 * rad, y0 + 0.5 * rad))
    path.push(
        "C{},{} , {},{} , {},{}".format(
            x0 + 0.3 * rad,
            y0 + 0.5 * rad,
            x0 + 0.8 * rad,
            y0,
            x0 + 0.3 * rad,
            y0 - 0.5 * rad,
        )
    )
    path.push("M{},{}".format(x0 - 0.4 * rad, y0 + 0.2 * rad))
    path.push(
        "C{},{} , {},{} , {},{}".format(
            x0 - 0.4 * rad,
            y0 + 0.2 * rad,
            x0 - 0.1 * rad,
            y0 + 0.35 * rad,
            x0 - 0.4 * rad,
            y0 + 0.5 * rad,
        )
    )
    path.push("M{},{}".format(x0 - 0.4 * rad, y0 - 0.2 * rad))
    path.push(
        "C{},{} , {},{} , {},{}".format(
            x0 - 0.4 * rad,
            y0 - 0.2 * rad,
            x0 - 0.1 * rad,
            y0 - 0.35 * rad,
            x0 - 0.4 * rad,
            y0 - 0.5 * rad,
        )
    )


def triangle(path, x0, y0, rad):
    path.push("M {},{}".format(x0, y0 - 2.5 * rad))
    path.push("L {},{}".format(x0, y0 + 2.5 * rad))
    path.push("L {},{}".format(x0 + 5 * rad, y0))
    path.push("L {},{}".format(x0, y0 - 2.5 * rad))


def leaf(path, x0, y0, rad):
    path.push("M {},{}".format(x0, y0 + rad))
    path.push(
        "c {},{} , {},{} , {},{}".format(1 * rad, 2 * rad, 1 * rad, 0, 3 * rad, -rad)
    )
    path.push("M {},{}".format(x0, y0 - rad))
    path.push(
        "c {},{} , {},{} , {},{}".format(1 * rad, -2 * rad, 1 * rad, 0, 3 * rad, rad)
    )
    path.push("M {},{}".format(x0, y0 - rad))
    path.push("L {},{}".format(x0, y0 + rad))
    path.push("L {},{}".format(x0 + 3 * rad, y0))


# The value that is equated between two successive principle convergence
# Use this to try and solve for z given x typically golden ratio and m two consecutive
# fibo numbers
def f_mzx(m, z, x):
    return math.pow(
        math.pow(z, m * 2) - 2 * math.pow(z, m) * math.cos(2 * math.pi * m * x) + 1, 0.5
    ) / (1 + math.pow(z, m))


"""
def pc(numbers):
	if not numbers:
		return 0

	pop = numbers.pop()
	return 1/(pop + pc(numbers))

def extract_qn(xpc, n):
	if n == 0:
		return 1
	if n == 1:
		return xpc[0]

	return xpc[n - 1] * extract_qn(xpc, n - 1) + extract_qn(xpc, n - 2)

def test_pc():
	x_pc = []
	for n in range(1, 100):
		x_pc.append(random.randint(1,10))
	print(x_pc)
	print(pc(x_pc.copy()))
	print(extract_qn(x_pc, 2))
	print(extract_qn(x_pc, 3))
"""

if __name__ == "__main__":
    main()
