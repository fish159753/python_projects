"""
File: draw_line.py
Name: Andy Wu
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 30


# Global variable
window = GWindow(title='Draw line')
circle = GOval(SIZE, SIZE)
n = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(circle_or_line)


def circle_or_line(m):
    global n
    global circle
    n += 1
    print(str(n))
    if n % 2 == 1:
        # Click first time
        circle = GOval(SIZE, SIZE, x=m.x-SIZE/2, y=m.y-SIZE/2)
        window.add(circle)
    elif n % 2 == 0:
        # Click second time
        line = GLine(circle.x+SIZE/2, circle.y+SIZE/2, m.x, m.y)
        window.remove(circle)
        window.add(line)


if __name__ == "__main__":
    main()
