import os
import svgwrite
import math

out_file = "images/test.svg"
dwg = svgwrite.Drawing(out_file, profile="full")

g_angle = 360 / math.pow((1 + math.sqrt(5)) / 2, 2)
g_ratio = 1 / (1 - g_angle / 360)


def shaped(n_circle, n_points):
    for i in range(3, n_circle + 1):
        cr = circle_radius(i)
        point_rotation = 360 / n_points
        rotation_offset = (i + 1) % 2 * point_rotation / 2

        p1 = [cr, 0]
        p2 = point_on_circle(cr, point_rotation)
        p3 = point_on_circle(circle_radius(i + 1), point_rotation / 2)

        for j in range(0, n_points):
            rotation = point_rotation * j + rotation_offset

            path = dwg.path(
                d="M{},{}".format(p1[0], p1[1]),
                stroke="black",
                fill="none",
                stroke_width=cr / 40,
                transform="rotate({}, {}, {})".format(rotation, 0, 0),
            )
            path.push("A{},{},0,1,0,{},{}".format(cr, cr, p2[0], p2[1]))
            path.push("L{},{}".format(p3[0], p3[1]))
            path.push("L{},{}".format(p1[0], p1[1]))

            dwg.add(path)


def circle_radius(i):
    return math.pow(1.2, i - 1)


def point_on_circle(radius, angle):
    return [
        radius * math.cos(math.radians(angle)),
        radius * math.sin(math.radians(angle)),
    ]


shaped(20, 24)

dwg.save()
os.system("open {}".format(out_file))
