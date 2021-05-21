"""
File: bouncing_ball.py
Name: Andy Wu
-------------------------
TODO: Assign the variable as the switch to avoid the mouse clicking.
      And limit in 3 times for the games.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variable
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
gravity = 0
n = 1
on_off = True


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(jump)


def jump(mouse):
    global n
    global on_off
    if n <= 3:
        # Only play the games for three times.
        if on_off:
            # Turn on the mouseclick.
            on_off = False
            # Suddenly turn off the mouseclick to avoid click the mouse in the game.
            global gravity
            while True:
                gravity += GRAVITY
                # Gravity is increasing.
                ball.move(VX, gravity)
                if ball.y >= window.height:
                    gravity *= -REDUCE
                    # When the ball falling down on the ground, the gravity will turn the direction.
                pause(DELAY)
                if ball.x >= window.width:
                    gravity = 0
                    ball.x = START_X
                    ball.y = START_Y
                    on_off = True
                    n += 1
                    break

if __name__ == "__main__":
    main()
