import arcade
import Comp151Window
import types

def update(window):
    window.player.center_x += window.player.Dx
    window_size = window.get_size()
    if window.player._get_right() > window_size[0] or window.player._get_left() <0:
        window.player.Dx = -window.player.Dx


def draw(window_being_updated):
    update(window_being_updated)
    arcade.start_render()
    window_being_updated.player.draw()

def setup_window(graphicsWindow):
    player = arcade.Sprite("galleon.png")

    player.set_position(200, 400)
    graphicsWindow.player = player
    arcade.set_background_color(arcade.color.EGYPTIAN_BLUE)
    graphicsWindow.player.Dx = 3


def main():
    graphicsWindow = Comp151Window.Comp151Window(800, 800, "Ship Demo")
    setup_window(graphicsWindow)
    graphicsWindow.on_draw = types.MethodType(draw, graphicsWindow)
    arcade.run()


main()