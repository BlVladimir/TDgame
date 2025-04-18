from scripts.configs.buttons_group import *
from math import ceil
from scripts.classes_objects.button_class import *

def change_using_additional_parameter(additionalParameters):
    if additionalParameters:
        additionalParameters = False
    else:
        additionalParameters = True
    return additionalParameters

def draw_sprite_group(sprite_group, context):
    sprite_group.draw(context.config_parameter_scene.get_screen())


class ButtonGroupController:
    def __init__(self, width, height):
        if height / 2.5 > width / 4:
            button_level_scale = ceil(width / 4)
        else:
            button_level_scale = ceil(height / 2.5)
        buttons_levels_array = (Button(width / 2 - button_level_scale * 1.5 - height / 20, height / 2 - button_level_scale - height / 40, "images/UI/lvl/lvl1.png", button_level_scale, button_level_scale, action_scene, 'lvl1'),
                                     Button(width / 2 - button_level_scale / 2, height / 2 - button_level_scale - height / 40, "images/UI/lvl/lvl2.png", button_level_scale, button_level_scale, action_scene, 'lvl2'),
                                     Button(width / 2 + button_level_scale / 2 + height / 20, height / 2 - button_level_scale - height / 40, "images/UI/lvl/lvl3.png", button_level_scale, button_level_scale, action_scene, 'lvl3'),
                                     Button(width / 2 - button_level_scale * 1.5 - height / 20, height / 2 + height / 40, "images/UI/lvl/lvl4.png", button_level_scale, button_level_scale, action_scene, 'lvl4'),
                                     Button(width / 2 - button_level_scale / 2, height / 2 + height / 40, "images/UI/lvl/lvl5.png", button_level_scale, button_level_scale, action_scene, 'lvl5'),
                                     Button(width / 2 + button_level_scale / 2 + height / 20, height / 2 + height / 40, "images/UI/lvl/lvl6.png", button_level_scale, button_level_scale, action_scene, 'lvl6'))

        self.__main_menu_group = ButtonsGroup()
        self.__settings_group = ButtonsGroup()
        self.__shop_group = ButtonsGroup()
        self.__general_group = GeneralButtonGroup(width, height)
        for i in buttons_levels_array:
            self.__main_menu_group.append_sprite(i)

    @property
    def main_menu_group(self):
        return self.__main_menu_group

    @property
    def settings_group(self):
        return self.__settings_group

    @property
    def shop_group(self):
        return self.__shop_group

    @property
    def general_group(self):
        return self.__general_group