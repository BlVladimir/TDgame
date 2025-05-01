from scripts.classes_objects.button_class import Button
from scripts.classes_objects import tower_class
def buy_tower(**kwargs):
    height = kwargs['height']
    if 'additional_image' in kwargs.keys():
        kwargs['context'].towers_controller.append_tower_object(
            tower_class.Tower(kwargs['image'], kwargs['context'].maps_controller.get_tile_scale(), kwargs['damage'],
                              kwargs['context'].maps_controller.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['coordinate'],
                              kwargs['context'].config_gameplay.get_current_tile(),
                              kwargs['improve_array'], kwargs['armor_piercing'], kwargs['poison'], image_gun=kwargs['additional_image'],
                              radius=kwargs['radius']),
            Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower, '1'))
    else:
        kwargs['context'].towers_controller.append_tower_object(
            tower_class.Tower(kwargs['image'], kwargs['context'].maps_controller.get_tile_scale(), kwargs['damage'],
                              kwargs['context'].maps_controller.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['coordinate'],
                              kwargs['context'].config_gameplay.get_current_tile(),
                              kwargs['improve_array'], kwargs['armor_piercing'], kwargs['poison'], radius=kwargs['radius']),
            Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower, '1'))

def buy_tower1(kwargs):  # добавляет в массив башен новую
    height = kwargs['height']
    if 'additional_image' in kwargs.keys():
        kwargs['context'].towers_controller.append_tower_object(
            tower_class.Tower(kwargs['image'], kwargs['context'].maps_controller.get_tile_scale(), kwargs['damage'],
                              kwargs['context'].maps_controller.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['coordinate'], kwargs['context'].config_gameplay.get_current_tile(),
                              kwargs['improve_array'], kwargs['armor_piercing'], kwargs['poison'], image_gun=kwargs['additional_image'], radius=kwargs['radius']),
            Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
    else:
        kwargs['context'].towers_controller.append_tower_object(
            tower_class.Tower(kwargs['image'], kwargs['context'].maps_controller.get_tile_scale(), kwargs['damage'],
                              kwargs['context'].maps_controller.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['coordinate'], kwargs['context'].config_gameplay.get_current_tile(),
                              kwargs['improve_array'], kwargs['armor_piercing'], kwargs['poison'], radius=kwargs['radius']),
            Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))

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


class Product:  # класс продуктов
    def __init__(self, image, cost, scale, coordinate, damage, radius, improve_cost_array, armor_piercing, poison, additional_image = None):
        self.__image = image
        self.__cost = cost
        self.__armor_piercing = armor_piercing
        self.__poison = poison
        self.__damage_tower = damage
        self.__radius_tower = radius
        self.__improve_cost_array = improve_cost_array
        self.__coordinate = coordinate
        self.__scale = scale
        self.__additional_money = 0
        if additional_image is not None:  # нужно, так как не у всех башен есть вращающаяся пушка
            self.__additional_image = additional_image
            self.__button_product = Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower, additional_image)
        else:
            self.__additional_image = None
            self.__button_product = Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower)

    def draw(self, context):  # рисует продукт
        self.__button_product.draw(context)

    def __reset_characteristic(self, context):  # сбрасывает дополнительные характеристики до изначальных
        match context.maps_controller.get_build_array()[context.config_gameplay.get_current_tile()]['type']:
            case 2:
                self.__damage_tower -= 1
            case 3:
                self.__radius_tower = self.__radius_tower / 1.2
            case 4:
                self.__armor_piercing = False
            case 5:
                self.__poison -= 1
            case 6:
                self.__additional_money -= 2


    def __create_tower(self, price_coefficient, height, context):  # создает башню с характеристиками, зависящими от текущего тайла
        match context.maps_controller.get_build_array()[context.config_gameplay.get_current_tile()]['type']:
            case 1:
                self.__button_product.handle_event_parameter(
                {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower, 'improve_array': self.__improve_cost_array, 'armor_piercing': self.__armor_piercing,
                'poison': self.__poison, 'additional_money': self.__additional_money, 'radius': self.__radius_tower, 'height': height, 'context': context})
            case 2:
                self.__button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower + 1, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': self.__armor_piercing, 'poison': self.__poison, 'additional_money': self.__additional_money, 'radius': self.__radius_tower, 'height': height, 'context': context})
            case 3:
                self.__button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': self.__armor_piercing, 'poison': self.__poison, 'additional_money': self.__additional_money, 'radius': self.__radius_tower * 1.2, 'height': height, 'context': context})
            case 4:
                self.__button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': True, 'poison': self.__poison, 'additional_money': self.__additional_money, 'radius': self.__radius_tower, 'height': height, 'context': context})
            case 5:
                self.__button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': self.__armor_piercing, 'poison': self.__poison + 1, 'additional_money': self.__additional_money, 'radius': self.__radius_tower, 'height': height, 'context': context})
            case 6:
                self.__button_product.handle_event_parameter(
                {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower, 'improve_array': self.__improve_cost_array, 'armor_piercing': self.__armor_piercing,
                'poison': self.__poison, 'additional_money': self.__additional_money + 2, 'radius': self.__radius_tower, 'height': height, 'context': context})
        context.config_gameplay.set_money(-self.__cost * price_coefficient)


    def buy(self, event,  context):  # покупка башни(возможность покупки и покупка, если возможно)
        is_free = context.config_modifier.get_is_free()
        price_up = context.config_modifier.get_price_up()
        is_filled = False
        if not price_up and not is_free and self.__button_product.is_pressed(event) and context.config_gameplay.get_money() >= self.__cost:
            self.__create_tower(1, context.config_parameter_scene.get_height(), context)
            is_filled = True
        elif price_up and not is_free and self.__button_product.is_pressed(event) and context.config_gameplay.get_money() >= self.__cost * 2:
            self.__create_tower(2, context.config_parameter_scene.get_height(), context)
            context.config_modifier.get_new_value_price_up(False)
            is_filled = True
        elif is_free and self.__button_product.is_pressed(event):
            self.__create_tower(0, context.config_parameter_scene.get_height(), context)
            context.config_modifier.get_new_value_price_up(False)
            context.config_modifier.get_new_value_is_free(False)
            is_filled = True
        return is_filled

    def get_coordinate(self):  # гетеры и сетеры
        return self.__coordinate

    def get_scale(self):
        return self.__scale

    def get_cost(self):
        return self.__cost

    def get_product_coordinate(self):
        return self.__coordinate