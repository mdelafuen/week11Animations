import arcade
import Comp151Window
import types
import random

def update(window, delta_time):
    if window.up_pressed and not window.down_pressed:
        window.playerDy = 3
    elif window.down_pressed and not window.up_pressed:
        window.playerDy = -3
    else:
        window.playerDy = 0
    if window.left_pressed and not window.right_pressed:
        window.playerDx = -3
    elif window.right_pressed and not window.left_pressed:
        window.playerDx = 3
    else:
        window.playerDx = 0
    window.player.center_x = window.player.center_x + window.playerDx
    window.player.center_y = window.player.center_y + window.playerDy
    gold_to_remove = 0
    for gold_pile in window.goldList:
        if gold_pile.collides_with_sprite(window.player):
            window.score += 10
            print(f"Your score is {window.score}")
            gold_to_remove = gold_pile
            break
    if gold_to_remove:
        window.goldList.remove(gold_to_remove)


def draw(window_being_updated):
    #update(window_being_updated)
    arcade.start_render()
    window_being_updated.player.draw()
    for gold_pile in window_being_updated.goldList:
        gold_pile.draw()

def setup_window(graphicsWindow):
    width, height = graphicsWindow.get_size()
    gold_list = []
    for gold_count in range(6):
        gold_pot = arcade.Sprite("gold-coins-large.png")
        xPos = random.randint(0, width)
        yPos = random.randint(0, height)
        gold_pot.set_position(xPos, yPos)
        gold_list.append(gold_pot)
    player = arcade.Sprite("galleon.png")
    player.set_position(200, 400)
    graphicsWindow.player = player
    arcade.set_background_color(arcade.color.EGYPTIAN_BLUE)
    graphicsWindow.playerDx = 0
    graphicsWindow.playerDy = 0
    graphicsWindow.goldList = gold_list
    graphicsWindow.up_pressed = False
    graphicsWindow.down_pressed = False
    graphicsWindow.left_pressed = False
    graphicsWindow.right_pressed = False
    graphicsWindow.score = 0

def key_pressed(game_window, key, modifiers):
    if key == arcade.key.LEFT:
        game_window.left_pressed = True
    if key == arcade.key.RIGHT:
        game_window.right_pressed = True
    if key == arcade.key.UP:
        game_window.up_pressed = True
    if key == arcade.key.DOWN:
        game_window.down_pressed = True


def key_released(game_window, key, modifiers):
    if key == arcade.key.LEFT:
        game_window.left_pressed = False
    if key == arcade.key.RIGHT:
        game_window.right_pressed = False
    if key == arcade.key.UP:
        game_window.up_pressed = False
    if key == arcade.key.DOWN:
        game_window.down_pressed = False


def main():
    graphicsWindow = Comp151Window.Comp151Window(1000, 800, "Ship Demo")
    setup_window(graphicsWindow)
    graphicsWindow.on_draw = types.MethodType(draw, graphicsWindow)
    graphicsWindow.on_update = types.MethodType(update, graphicsWindow)
    graphicsWindow.on_key_press = types.MethodType(key_pressed, graphicsWindow)
    graphicsWindow.on_key_release = types.MethodType(key_released, graphicsWindow)
    arcade.run()


main()