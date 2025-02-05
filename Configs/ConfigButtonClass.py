from ButtonClass import Button

class ConfigButton:

    def __init__(self, width, height, function_button_level):
        self.button_level_array = (Button(width / 2 - 600, height / 2 - 300, "images/UI/lvl/lvl1.png", 300, 300, function_button_level),
        Button(width / 2 - 200, height / 2 - 300, "images/UI/lvl/lvl2.png", 300, 300, function_button_level),
        Button(width / 2 + 200, height / 2 - 300, "images/UI/lvl/lvl3.png", 300, 300, function_button_level),
        Button(width / 2 - 600, height / 2 + 100, "images/UI/lvl/lvl4.png", 300, 300, function_button_level),
        Button(width / 2 - 200, height / 2 + 100, "images/UI/lvl/lvl5.png", 300, 300, function_button_level),
        Button(width / 2 + 200, height / 2 + 100, "images/UI/lvl/lvl6.png", 300, 300, function_button_level))

    def get_button_level_array(self):
        return self.button_level_array

