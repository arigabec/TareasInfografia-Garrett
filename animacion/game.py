import arcade
import random
from players import Tank

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Tank"

SPEED = 10

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.rot_speed = 0.5
        self.speed = 10
        self.tank1 = Tank(400, 400, arcade.color.RED)
        self.tank2 = Tank(400, 400, arcade.color.BLUE)
    
    def on_key_press(self, symbol: int, modifiers: int):
        # TANK 1
        if symbol == arcade.key.W:
            self.tank1.speed = SPEED
        if symbol == arcade.key.S:
            self.tank1.speed = -SPEED
        if symbol == arcade.key.A:
            self.tank1.angular_speed = 1.5
        if symbol == arcade.key.D:
            self.tank1.angular_speed = -1.5
        if symbol == arcade.key.SPACE:
            self.tank1.shoot(20)

        # TANK 2
        if symbol == arcade.key.UP:
            self.tank2.speed = SPEED
        if symbol == arcade.key.DOWN:
            self.tank2.speed = -SPEED
        if symbol == arcade.key.LEFT:
            self.tank2.angular_speed = 1.5
        if symbol == arcade.key.RIGHT:
            self.tank2.angular_speed = -1.5
        if symbol == arcade.key.ENTER:
            self.tank2.shoot(20)
            
    def on_key_release(self, symbol: int, modifiers: int):
        # TANK 1
        if symbol in (arcade.key.W, arcade.key.S):
            self.tank1.speed = 0
        if symbol in (arcade.key.A, arcade.key.D):
            self.tank1.angular_speed = 0

        # TANK 2
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.tank2.speed = 0
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.tank2.angular_speed = 0

    def on_update(self, delta_time: float):
        self.tank1.update(delta_time)
        self.tank2.update(delta_time)
        self.tank1.detect_collision(self.tank2)
        self.tank2.detect_collision(self.tank1)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"Player 1: {self.tank1.life}", 20, 760, arcade.color.RED, 20)
        arcade.draw_text(f"Player 2: {self.tank2.life}", 620, 760, arcade.color.BLUE, 20)
        self.tank1.draw()
        self.tank2.draw()
        
if __name__ == "__main__":
    app = App()
    arcade.run()