class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3.5

        # 子弹设置
        self.bullet_speed = 50
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = (255, 192, 203)
        self.bullet_color_red = (255, 0, 0)
        self.bullet_color_green = (0, 255, 0)
        self.bullet_color_blue = (0, 0, 255)
        self.bullet_color_orange = (255, 165, 0)
        self.bullet_color_yellow = (255, 255, 0)
        self.bullet_color_purple = (160, 32, 240)

        self.bullet_color_array = [self.bullet_color, self.bullet_color_red, self.bullet_color_green,
                                   self.bullet_color_blue, self.bullet_color_orange, self.bullet_color_yellow,
                                   self.bullet_color_purple]

        self.bullets_allowed = 300

        #
        self.alien_speed = 15
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # 飞船设置
        self.ship_limit = 2

    def to_string(self):
        print("screen_width=" + str(self.screen_width))
        print("screen_height=" + str(self.screen_height))
