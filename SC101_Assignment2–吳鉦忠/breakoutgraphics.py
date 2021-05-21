"""
File: breakoutgraphics.py
Name: Andy Wu
------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

To deal with the game of the graphics.

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.graphics.gimage import GImage
from campy.gui.events.timer import pause

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
NUM_BOMB = 3
FRAME_RATE = 1000 / 120


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-PADDLE_WIDTH)/2, y=window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - ball_radius*2)/2, y=(window_height - ball_radius*2)/2)
        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = - self.__dx
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        self.begin = False
        self.on_off = True
        onmouseclicked(self.on_off_or_bump)
        # Draw bricks
        for i in range(brick_rows):
            a = i
            i *= (brick_height+brick_spacing)
            for j in range(brick_cols):
                j *= (brick_width+brick_spacing)
                self.brick = GRect(brick_width, brick_height, x=j, y=i+BRICK_OFFSET)
                self.brick.filled = True
                if a % 10 <= 1:
                    self.brick.fill_color = 'black'
                elif 1 < a % 10 <= 3:
                    self.brick.fill_color = 'darkgray'
                elif 3 < a % 10 <= 5:
                    self.brick.fill_color = 'dimgray'
                elif 5 < a % 10 <= 7:
                    self.brick.fill_color = 'gray'
                elif 7 < a % 10 <= 9:
                    self.brick.fill_color = 'lightgray'
                self.window.add(self.brick)

        # Score label
        self.score_speed = 0
        self.score = 0
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = '-20'
        self.window.add(self.score_label, (self.window.width-self.score_label.width)/2, self.score_label.height)

        # Life label
        self.life_label = GLabel('Life: ')
        self.life_label.font = '-20'
        self.window.add(self.life_label, 0, self.score_label.height)

        # Bomb
        self.bomb = NUM_BOMB
        self.bomb_switch = False

    def on_off_or_bump(self, mouse):
        if self.on_off:
            self.on_off = False
            self.begin = True
        if self.bomb > 0:
            self.bomb_switch = True
            if mouse.y < self.paddle.y and self.window.get_object_at(mouse.x, mouse.y) is not None:
                bomb = GImage("Bomb.png")
                self.window.add(bomb, x=mouse.x-bomb.width/2, y=mouse.y-bomb.height/2)
                pause(FRAME_RATE)
                for i in range(0, self.window.width):
                    self.window.remove(self.window.get_object_at(i, mouse.y))
                self.window.remove(GImage("Bomb.png"))
                self.bomb -= 1
        else:
            self.bomb_switch = False

    def paddle_move(self, mouse):
        self.paddle.y = self.window.height - PADDLE_OFFSET
        self.paddle.x = mouse.x - self.paddle.width / 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def get_remaining_x(self):
        return self.__dx

    def get_remaining_y(self):
        return self.__dy





