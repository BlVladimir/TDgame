from Scripts.MainScripts import ButtonWorks, ShopWorks, LVL
import pygame

def level(shop, event, context):
    ButtonWorks.is_started(context)
    context.get_towers_controller().define_current_tower(context)
    context.get_enemies_controller().define_current_enemy()
    context.get_maps_controller().definition_current_tile(event, context)  # определяет текущий тайл
    if event.type == pygame.MOUSEBUTTONDOWN:  # если кнопка мыши нажата
        if context.get_enemies_controller().get_current_enemy():  # если выделенный враг существует и существует хотя бы одна башня
            if context.get_towers_controller().get_current_tower() and context.get_towers_controller().get_current_tower().is_in_radius(context):  # если индекс башни равен текущему тайлу и текущий враг в радиусе башни
                context.get_enemies_controller().get_current_enemy().remove_health(context)  # отнимает у врага здоровье, равное урону башни
                context.get_towers_controller().get_current_tower().is_used = True  # переменная отвечает за то, что башня была использована
                context.get_enemies_controller().get_current_enemy().reset_to_zero_additional_tower_price()
                context.get_enemies_controller().get_current_enemy().new_value_additional_tower_price(context)
                context.get_enemies_controller().kill_enemies(context)
    ButtonWorks.button_works(event, context)
    ShopWorks.shop_works(shop, event, context)
    context.get_config_constant_object().get_button_exit().handle_event(event)
