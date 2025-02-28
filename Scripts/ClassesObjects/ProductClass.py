from Scripts.ClassesObjects.ButtonClass import Button
from Scripts.ClassesObjects import TowerClass


def buy_tower(parameter_dict):  # добавляет в массив башен новую
    height = parameter_dict['height']
    if 'additional_image' in parameter_dict.keys():
        parameter_dict['context'].get_towers_controller().append_tower_object(
            TowerClass.Tower(parameter_dict['image'], parameter_dict['context'].get_maps_controller().get_tile_scale(), parameter_dict['damage'],
                             parameter_dict['context'].get_maps_controller().get_build_array()[parameter_dict['context'].get_config_gameplay().get_current_tile()]['coordinate'], parameter_dict['context'].get_config_gameplay().get_current_tile(),
                             parameter_dict['improve_array'], parameter_dict['armor_piercing'], parameter_dict['poison'], image_gun=parameter_dict['additional_image'], radius=parameter_dict['radius']),
            Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
    else:
        parameter_dict['context'].get_towers_controller().append_tower_object(
            TowerClass.Tower(parameter_dict['image'], parameter_dict['context'].get_maps_controller().get_tile_scale(), parameter_dict['damage'],
                             parameter_dict['context'].get_maps_controller().get_build_array()[parameter_dict['context'].get_config_gameplay().get_current_tile()]['coordinate'], parameter_dict['context'].get_config_gameplay().get_current_tile(),
                             parameter_dict['improve_array'], parameter_dict['armor_piercing'], parameter_dict['poison'], radius=parameter_dict['radius']),
            Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))

def upgrade_tower(context):  # улучшение башни по номеру
    if context.get_towers_controller().get_current_tower().level != 3:
        cost =  context.get_towers_controller().get_current_tower().improve_cost_array[context.get_towers_controller().get_current_tower().level - 1]
        is_free = context.get_config_modifier().get_is_free()
        price_up = context.get_config_modifier().get_price_up()
        if is_free:
            context.get_towers_controller().get_current_tower().upgrade(1, 60)
            context.get_towers_controller().get_current_tower().level += 1
            context.get_towers_controller().get_current_button_update().change_image('images/upgrade/2lvl.png') if context.get_towers_controller().get_current_tower().level == 2 \
                else  context.get_towers_controller().get_current_button_update().change_image('images/upgrade/3lvl.png')
            context.get_config_modifier().get_new_value_is_free(False)
            context.get_config_modifier().get_new_value_price_up(False)
            context.get_towers_controller().append_upgrade(context)
        elif price_up and context.get_config_gameplay().get_money() >= cost * 2:
            context.get_towers_controller().get_current_tower().upgrade(1, 60)
            context.get_towers_controller().get_current_tower().level += 1
            context.get_towers_controller().get_current_button_update().change_image('images/upgrade/2lvl.png') if context.get_towers_controller().get_current_tower().level == 2 \
                else context.get_towers_controller().get_current_button_update().change_image('images/upgrade/3lvl.png')
            context.get_config_gameplay().set_money(-cost * 2)
            context.get_config_modifier().get_new_value_price_up(False)
            context.get_towers_controller().append_upgrade(context)
        elif not price_up and context.get_config_gameplay().get_money() >= cost:
            context.get_towers_controller().get_current_tower().upgrade(1, 60)
            context.get_towers_controller().get_current_tower().level += 1
            context.get_towers_controller().get_current_button_update().change_image('images/upgrade/2lvl.png') if context.get_towers_controller().get_current_tower().level == 2 \
                else  context.get_towers_controller().get_current_button_update().change_image('images/upgrade/3lvl.png')
            context.get_config_gameplay().set_money(-cost)
            context.get_towers_controller().append_upgrade(context)


class Product:  # класс продуктов
    def __init__(self, image, cost, scale, coordinate, damage, radius, improve_cost_array, armor_piercing, poison, additional_image = None):
        self.__image = image
        self.cost = cost
        self.__armor_piercing = armor_piercing
        self.__poison = poison
        self.__damage_tower = damage
        self.__radius_tower = radius
        self.__improve_cost_array = improve_cost_array
        self.coordinate = coordinate
        self.scale = scale
        self.__additional_money = 0
        if additional_image is not None:  # нужно, так как не у всех башен есть вращающаяся пушка
            self.__additional_image = additional_image
            self.button_product = Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower, additional_image)

        else:
            self.__additional_image = None
            self.button_product = Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower)

    def draw(self, context):  # рисует продукт
        self.button_product.draw(context)

    def __reset_characteristic(self, context):
        match context.get_maps_controller().get_build_array()[context.get_config_gameplay().get_current_tile()]['type']:
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
        match context.get_maps_controller().get_build_array()[context.get_config_gameplay().get_current_tile()]['type']:
            case 1:
                self.button_product.handle_event_parameter(
                {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower, 'improve_array': self.__improve_cost_array, 'armor_piercing': self.__armor_piercing,
                'poison': self.__poison, 'additional_money': self.__additional_money, 'radius': self.__radius_tower, 'height': height, 'context': context})
            case 2:
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower + 1, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': self.__armor_piercing, 'poison': self.__poison, 'additional_money': self.__additional_money, 'radius': self.__radius_tower, 'height': height, 'context': context})
            case 3:
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': self.__armor_piercing, 'poison': self.__poison, 'additional_money': self.__additional_money, 'radius': self.__radius_tower * 1.2, 'height': height, 'context': context})
            case 4:
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': True, 'poison': self.__poison, 'additional_money': self.__additional_money, 'radius': self.__radius_tower, 'height': height, 'context': context})
            case 5:
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': self.__armor_piercing, 'poison': self.__poison + 1, 'additional_money': self.__additional_money, 'radius': self.__radius_tower, 'height': height, 'context': context})
            case 6:
                self.button_product.handle_event_parameter(
                {'additional_image': self.__additional_image, 'image': self.__image, 'damage': self.__damage_tower, 'improve_array': self.__improve_cost_array, 'armor_piercing': self.__armor_piercing,
                'poison': self.__poison, 'additional_money': self.__additional_money + 2, 'radius': self.__radius_tower, 'height': height, 'context': context})
        context.get_config_gameplay().set_money(-self.cost * price_coefficient)


    def buy(self, event,  context):  # покупка башни
        is_free = context.get_config_modifier().get_is_free()
        price_up = context.get_config_modifier().get_price_up()
        is_filled = False
        if not price_up and not is_free and self.button_product.is_pressed(event) and context.get_config_gameplay().get_money() >= self.cost:
            self.__create_tower(1, context.get_config_parameter_scene().get_height(), context)
            is_filled = True
        elif price_up and not is_free and self.button_product.is_pressed(event) and context.get_config_gameplay().get_money() >= self.cost * 2:
            self.__create_tower(2, context.get_config_parameter_scene().get_height(), context)
            context.get_config_modifier().get_new_value_price_up(False)
            is_filled = True
        elif is_free and self.button_product.is_pressed(event) and context.get_config_gameplay().get_money() >= self.cost * 2:
            self.__create_tower(0, context.get_config_parameter_scene().get_height(), context)
            context.get_config_modifier().get_new_value_price_up(False)
            context.get_config_modifier().get_new_value_is_free(False)
            is_filled = True
        return is_filled