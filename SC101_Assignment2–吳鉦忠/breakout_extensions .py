"""
File: breakout_extensions.py
Name: Andy Wu
------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Add " the Bomb " to bomb the row of the bricks by mouse clicked.
Extra add the loser broad.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

# Constants
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    vx = graphics.get_remaining_x()
    vy = graphics.get_remaining_y()
    # Add animation loop here!
    life = NUM_LIVES
    graphics.life_label.text = "Life: " + str(life)
    bomb_label = GLabel("Bomb: "+str(graphics.bomb))
    bomb_label.font = '-20'
    graphics.window.add(bomb_label, graphics.window.width-bomb_label.width, bomb_label.height)
    graphics.life_label.text = "Life: " + str(life)
    while True:
        if life > 0:
            if graphics.begin:
                graphics.ball.move(vx, vy)
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    vx = - vx
                if graphics.ball.y <= 0:
                    vy = - vy
                if graphics.ball.y + graphics.ball.height < graphics.paddle.y:
                    # Remove the bricks.
                    if graphics.ball.y > graphics.life_label.y and graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) is not None:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x, graphics.ball.y))
                        vy = - vy
                        graphics.score += 1
                        graphics.score_speed += 1
                        graphics.score_label.text = 'Score: ' + str(graphics.score)
                    if graphics.ball.y > graphics.life_label.y and graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y) is not None:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y))
                        vy = - vy
                        graphics.score += 1
                        graphics.score_speed += 1
                        graphics.score_label.text = 'Score: ' + str(graphics.score)
                    if graphics.ball.y > graphics.life_label.y and graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height) is not None:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height))
                        vy = - vy
                        graphics.score += 1
                        graphics.score_speed += 1
                        graphics.score_label.text = 'Score: ' + str(graphics.score)
                    if graphics.ball.y > graphics.life_label.y and graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height) is not None:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height))
                        vy = - vy
                        graphics.score += 1
                        graphics.score_speed += 1
                        graphics.score_label.text = 'Score: ' + str(graphics.score)
                # To bounce back after hitting the paddle.
                elif graphics.ball.y + graphics.ball.height <= graphics.paddle.y + graphics.paddle.height and graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height) is not None:
                    vy = - vy
                elif graphics.ball.y + graphics.ball.height <= graphics.paddle.y + graphics.paddle.height and graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height) is not None:
                    vy = - vy
                # The ball under the paddle.
                elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.window.remove(graphics.ball)
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2, y=(graphics.window.height - graphics.ball.height * 2) / 2)
                    life -= 1
                    graphics.on_off = True
                    graphics.begin = False
                    graphics.life_label.text = "Life: " + str(life)
            pause(FRAME_RATE)
            if graphics.score_speed >= 5:
                vx *= 1.2
                graphics.score_speed = 0
            bomb_label.text = "Bomb: "+str(graphics.bomb)
        else:
            graphics.window.clear()
            game_over = GLabel('Game Over !')
            game_over1 = GLabel('Game Over !')
            game_over2 = GLabel('Game Over !')
            game_over3 = GLabel('Game Over !')
            game_over4 = GLabel('Game Over !')
            game_over5 = GLabel('You are loser !')
            game_over6 = GLabel('You are loser !')
            game_over7 = GLabel('You are loser !')
            game_over8 = GLabel('You are loser !')
            game_over9 = GLabel('You are loser !')
            game_over10 = GLabel('You are loser !')
            game_over11 = GLabel('You are loser !')
            font = 10
            for i in range(1, 100):
                font += 5
                graphics.window.remove(game_over)
                game_over.font = str(-font)
                graphics.window.add(game_over, x=(graphics.window.width-game_over.width)/2, y=graphics.window.height/2)
                pause(5)
                game_over1.font = str(-font)
                graphics.window.add(game_over1, x=(graphics.window.width - game_over.width) / 2,
                                    y=graphics.window.height / 2)
                pause(10)
                game_over2.font = str(-font)
                graphics.window.add(game_over2, x=(graphics.window.width - game_over.width) / 2,
                                    y=graphics.window.height / 2)
                pause(15)
                game_over3.font = str(-font)
                graphics.window.add(game_over3, x=(graphics.window.width - game_over.width) / 2,
                                    y=graphics.window.height / 2)
                pause(20)
                game_over4.font = str(-font)
                graphics.window.add(game_over4, x=(graphics.window.width - game_over.width) / 2,
                                    y=graphics.window.height / 2)
                pause(25)

                game_over9.font = str(-font)
                game_over9.color = 'tomato'
                graphics.window.add(game_over9, x=(graphics.window.width - game_over.width) / 2,
                                    y=graphics.window.height / 5)
                pause(5)
                game_over5.font = str(-font)
                game_over5.color = 'tomato'
                graphics.window.add(game_over5, x=((graphics.window.width - game_over.width)*3) / 4,
                                    y=(graphics.window.height*3) / 9)
                pause(10)
                game_over6.font = str(-font)
                game_over6.color = 'tomato'
                graphics.window.add(game_over6, x=(graphics.window.width - game_over.width) / 4,
                                    y=(graphics.window.height*3) / 5)
                pause(15)
                game_over7.font = str(-font)
                game_over7.color = 'tomato'
                graphics.window.add(game_over7, x=((graphics.window.width - game_over.width)*3) / 15,
                                    y=graphics.window.height / 4)
                pause(20)
                game_over8.font = str(-font)
                game_over8.color = 'tomato'
                graphics.window.add(game_over8, x=(graphics.window.width - game_over.width) / 2,
                                    y=graphics.window.height*3 / 4)
                pause(25)
                game_over10.font = str(-font)
                game_over10.color = 'tomato'
                graphics.window.add(game_over10, x=(graphics.window.width - game_over.width)*3 / 4,
                                    y=graphics.window.height * 4 / 5)
                pause(25)
                game_over11.font = str(-font)
                game_over11.color = 'tomato'
                graphics.window.add(game_over11, x=(graphics.window.width - game_over.width) * 2.5 / 4,
                                    y=graphics.window.height * 4.8 / 5)
                pause(25)
            break


if __name__ == '__main__':
    main()
