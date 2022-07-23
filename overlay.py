from dataclasses import dataclass
from tkinter import Tk


@dataclass
class Point:
    x: float
    y: float


points = []

MAP_WIDTH = 50
MAP_HEIGHT = 30
WINDOW_WIDTH = 770
WINDOW_HEIGHT = 450


def left_click(event):
    x = (event.x / WINDOW_WIDTH) * MAP_WIDTH - MAP_WIDTH / 2
    y = -(event.y / WINDOW_HEIGHT) * MAP_HEIGHT + MAP_HEIGHT / 2
    print("Point clicked:\t{}\t{}".format(x, y))
    if len(points) != 0:
        if x < points[-1].x:
            x = points[-1].x
    points.append(Point(x, y))


def build_function():
    function = ""

    for i in range(1, len(points)):
        curr = points[i]
        prev = points[i - 1]

        dx = curr.x - prev.x
        dy = curr.y - prev.y

        EXP = 25
        if dx != 0:
            function += \
                "+1/(1+exp(-{EXP}*(x-({px}))))*({dy}/{dx})*(x-({px}))-1/(1+exp(-{EXP}*(x-({cx}))))*({dy}/{dx})*(x-({cx}))" \
                    .format(EXP=EXP, px=prev.x, cx=curr.x, dx=dx, dy=dy)
        else:
            function += \
                "+1/(1+exp(-{EXP}*(x-({px}))))*({dy})" \
                    .format(EXP=EXP, px=prev.x, dy=dy)

    return function


def right_click(event):
    function = build_function()

    if function != "":
        print("Function:\n{}".format(function))

    if len(points) != 0:
        print("Trajectory cleared")
        points.clear()


if __name__ == '__main__':
    root = Tk()
    root.title('GraphWar Overlay')
    root.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
    root.resizable(False, False)
    root.wait_visibility(root)
    root.wm_attributes('-alpha', 0.25)
    root.attributes('-topmost', 1)

    root.bind("<Button-1>", left_click)
    root.bind("<Button-3>", right_click)

    root.mainloop()
