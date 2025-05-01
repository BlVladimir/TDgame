from sys import exit

class EventController:
    def update(self, context):
        button_event = context.buttons_groups_controller.action
        match button_event.name:
            case 'exit':
                exit()
            case 'change_scene':
                context.config_parameter_scene.set_scene(button_event.parameter['scene'])
                if button_event.parameter['scene'].isdigit():
                    context.maps_controller.change_level(button_event.parameter['scene'])
                    context.config_constant_object.get_information_table().reset_modifier()
                    context.config_modifier.reset_price_modifier()
                    context.towers_controller.update_scale_animation(context)
                    context.config_parameter_scene.highlighting.update_scale(context)
                    context.maps_controller.update_trajectory_array()
                    context.maps_controller.create_waves(100, context)  # создает волны
                    context.config_gameplay.set_current_wave(1 - context.config_gameplay.get_current_wave())  # текущая волна
                    context.enemies_controller.create_enemy(context)  # создает врагов на 1 клетке
                    context.config_gameplay.set_is_started(False)  # переменная отвечает за то, началась ли игра или нет
                    context.config_gameplay.set_money(-context.config_gameplay.get_money() + 4)
                    for i in range(len(context.maps_controller.get_build_array())):  # обнуляет все тайлы
                        context.maps_controller.get_build_array()[i]['is_filled'] = False
                    context.config_constant_object.clear_sprites()
            case 'using_additional_parameter_setting':
                context.file_save_controller.change_true_false('always use additional parameter')
                context.config_gameplay.set_always_use_additional_parameters(context.file_save_controller.get_parameter('always use additional parameter'))