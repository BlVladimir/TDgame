from pygame.sprite import Group
from scripts.classes_objects.button_class import Button
from sys import exit

def action_scene(**kwargs):  # функция, меняющая переменную сцены
    kwargs['context'].config_parameter_scene.set_scene(kwargs['lvl'])
    if kwargs['lvl'].isdigit():
        kwargs['context'].maps_controller.change_level(kwargs['lvl'])

def action_exit():  # функция, закрывающая окно
    exit()

class ButtonsGroup:
    def __init__(self):
        self.__button_group = Group()
        self.__active = True

    def append_sprite(self, sprite):
        self.__button_group.add(sprite)

    def draw(self, context):
        if self.__active:
            self.__button_group.draw(context.config_parameter_scene.get_screen())
            self.__button_group.update({'context':context})

    def action(self, event, **kwargs):
        for i in self.__button_group.sprites():
            if i.is_pressed(event):
                i.handle_event_parameter(kwargs)
                break

    def clear_buttons(self):
        self.__button_group.empty()

    @property
    def active(self):
        raise PermissionError('privet attribute')

    @active.setter
    def active(self, value):
        self.__active = bool(value)

class GeneralButtonGroup:
    def __init__(self, width, height):
        self.__button_group = Group()
        self.__general_buttons_array = (Button(width - 170 - height * 0.4, 20, "images/UI/exit.png", 150, 75, action_exit, 'exit'),
        Button(150, 20, "images/UI/exit_in_main_menu.png", 100, 100, action_scene, 'go_to_main_menu'),
        (20, 20, "images/UI/settings.png", 100, 100, action_scene, 'go_to_settings'))  # объекты кнопок, встречающихся везде
        for i in self.__general_buttons_array:
            self.__button_group.add(i)

    def __get_sprites(self, scene='0'):  # 1-для главного меню, 2-для настроек
        if scene == 'mainMenu':
            return self.__button_group.remove(self.__general_buttons_array[1])
        elif scene == 'setting':
            return self.__button_group.remove(self.__general_buttons_array[2])
        else:
            return self.__button_group

    def draw(self, context, scene='0'):
        self.__get_sprites(scene).draw(context.config_parameter_scene.get_screen())
        self.__get_sprites(scene).update(context)

    def action(self, event, context, scene='0'):
        sprites = self.__get_sprites(scene)
        for i in sprites:
            if i.is_pressed(event):
                match i.name:
                    case 'go_to_main_menu':
                        i.handle_event_parameter({'context':context, 'lvl':'mainMenu'})
                    case 'go_to_settings':
                        i.handle_event_parameter({'context':context, 'lvl':'setting'})
                    case 'exit':
                        i.handle_event_parameter()
                break