import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_rain():
    arcade.draw_lrtb_rectangle_filled(550, 552, 480, 440, arcade.csscolor.DARK_BLUE)

    arcade.draw_lrtb_rectangle_filled(450, 452, 480, 440, arcade.csscolor.DARK_BLUE)

    arcade.draw_lrtb_rectangle_filled(350, 352, 480, 440, arcade.csscolor.DARK_BLUE)

    arcade.draw_lrtb_rectangle_filled(250, 252, 480, 440, arcade.csscolor.DARK_BLUE)

    arcade.draw_lrtb_rectangle_filled(150, 152, 480, 440, arcade.csscolor.DARK_BLUE)

    arcade.draw_lrtb_rectangle_filled(50, 52, 480, 440, arcade.csscolor.DARK_BLUE)

    arcade.draw_lrtb_rectangle_filled(500, 502, 560, 520, arcade.csscolor.DARK_BLUE)

    arcade.draw_lrtb_rectangle_filled(400, 402, 560, 520, arcade.csscolor.DARK_BLUE)

    arcade.draw_lrtb_rectangle_filled(300, 302, 560, 520, arcade.csscolor.DARK_BLUE)

    arcade.draw_lrtb_rectangle_filled(200, 202, 560, 520, arcade.csscolor.DARK_BLUE)

    arcade.draw_lrtb_rectangle_filled(100, 102, 560, 520, arcade.csscolor.DARK_BLUE)

def draw_tree():

    arcade.draw_rectangle_filled(100, 320, 30, 275, arcade.csscolor.SIENNA)

    arcade.draw_circle_filled(100, 500, 55, arcade.csscolor.DARK_GREEN)

def draw_terrain():
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 250, arcade.csscolor.GREY)

def draw_car(x):
    arcade.draw_rectangle_filled(460 + x, 330, 210, 30, arcade.csscolor.BLACK)

    arcade.draw_rectangle_filled(460 + x, 350, 95, 20, arcade.csscolor.BLACK)

    arcade.draw_circle_filled(400 + x, 305, 30, arcade.csscolor.BLACK)

    arcade.draw_circle_filled(520 + x, 305, 30, arcade.csscolor.BLACK)

def on_draw(delta_time):
    arcade.start_render()

    draw_rain()

    draw_tree()

    draw_terrain()

    draw_car(on_draw.car_x,)

    on_draw.car_x +=-1

on_draw.car_x = 0



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")

    arcade.set_background_color(arcade.csscolor.AZURE)





    arcade.schedule(on_draw, 1 / 60)



    arcade.run()

main()