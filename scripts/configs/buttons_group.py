from pygame.sprite import Group
from scripts.classes_objects.button_class import Button
from scripts.classes_objects.tower_class import Tower

def upgrade_tower(context):  # улучшение башни по номеру
    if context.towers_controller.get_current_tower().get_level() != 3:
        cost =  context.towers_controller.get_current_tower().get_improve_cost_array()[context.towers_controller.get_current_tower().get_level() - 1]
        is_free = context.config_modifier.get_is_free()
        price_up = context.config_modifier.get_price_up()
        if is_free:
            context.towers_controller.get_current_tower().upgrade(1, 60)
            context.towers_controller.get_current_tower().set_level()
            context.towers_controller.get_current_button_update().change_image('images/upgrade/2lvl.png') if context.towers_controller.get_current_tower().get_level() == 2 \
                else  context.towers_controller.get_current_button_update().change_image('images/upgrade/3lvl.png')
            context.config_modifier.get_new_value_is_free(False)
            context.config_modifier.get_new_value_price_up(False)
            context.towers_controller.append_upgrade(context)
        elif price_up and context.config_gameplay.get_money() >= cost * 2:
            context.towers_controller.get_current_tower().upgrade(1, 60)
            context.towers_controller.get_current_tower().set_level()
            context.towers_controller.get_current_button_update().change_image('images/upgrade/2lvl.png') if context.towers_controller.get_current_tower().get_level() == 2 \
                else context.towers_controller.get_current_button_update().change_image('images/upgrade/3lvl.png')
            context.config_gameplay.set_money(-cost * 2)
            context.config_modifier.get_new_value_price_up(False)
            context.towers_controller.append_upgrade(context)
        elif not price_up and context.config_gameplay.get_money() >= cost:
            context.towers_controller.get_current_tower().upgrade(1, 60)
            context.towers_controller.get_current_tower().set_level()
            context.towers_controller.get_current_button_update().change_image('images/upgrade/2lvl.png') if context.towers_controller.get_current_tower().get_level() == 2 \
                else  context.towers_controller.get_current_button_update().change_image('images/upgrade/3lvl.png')
            context.config_gameplay.set_money(-cost)
            context.towers_controller.append_upgrade(context)

def buy_tower(**kwargs):
    height = kwargs['height']
    if 'additional_image' in kwargs.keys():
        kwargs['context'].towers_controller.append_tower_object(
            Tower(kwargs['image'], kwargs['context'].maps_controller.get_tile_scale(), kwargs['damage'],
                              kwargs['context'].maps_controller.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['coordinate'],
                              kwargs['context'].config_gameplay.get_current_tile(),
                              kwargs['improve_array'], kwargs['armor_piercing'], kwargs['poison'], image_gun=kwargs['additional_image'],
                              radius=kwargs['radius']),
            kwargs['context'].ButtonGroupController.upgrade_group.append_sprite(Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower, '1')))
    else:
        kwargs['context'].towers_controller.append_tower_object(
            Tower(kwargs['image'], kwargs['context'].maps_controller.get_tile_scale(), kwargs['damage'],
                              kwargs['context'].maps_controller.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['coordinate'],
                              kwargs['context'].config_gameplay.get_current_tile(),
                              kwargs['improve_array'], kwargs['armor_piercing'], kwargs['poison'], radius=kwargs['radius']),
            Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower, '1'))

class ButtonsGroup:
    def __init__(self, sprites = None):
        self.__button_group = Group()
        if sprites:
            for i in sprites:
                self.__button_group.add(i)
        self.__active = True

    def draw(self, context):
        if self.__active:
            self.__button_group.draw(context.config_parameter_scene.get_screen())
            self.__button_group.update({'context':context})

    def action(self, event):
        if self.__active:
            for i in self.__button_group.sprites():
                if i.is_pressed(event):
                    return i.is_pressed(event)
        return False

    def update(self, context):
        self.__button_group.update(context = context)

    @property
    def active(self):
        raise PermissionError('privet attribute')

    @active.setter
    def active(self, value):
        self.__active = bool(value)

class ExpansionsButtonGroup(ButtonsGroup):
    def __init__(self, spites = None):
        super().__init__(spites)

    def append_sprite(self, sprite):
        self.__button_group.add(sprite)

    def clear_buttons(self):
        self.__button_group.empty()

class TextButtonsGroup(ButtonsGroup):
    def __init__(self, sprites = None):
        super().__init__(sprites)

    def change_text(self, **kwargs):
        sprites = self.__button_group.sprites()
        for i in range(len(sprites)):
            if sprites[i].name in kwargs.keys():
                self.__button_group.sprites()[i].text = kwargs[sprites[i].name]

class GeneralButtonsGroup:
    def __init__(self, sprites = None):
        self.__button_group = Group()
        self.__general_buttons_array = sprites  # объекты кнопок, встречающихся везде
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

    def action(self, event, scene='0'):
        for i in self.__get_sprites(scene):
            if i.is_pressed(event):
                return i.is_pressed(event)