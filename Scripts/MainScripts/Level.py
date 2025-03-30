from Scripts.MainScripts import ButtonWorks, ShopWorks, LVL
import pygame

def level(shop, event, highlighting, context):
    ButtonWorks.is_started(context, highlighting)
    context.get_towers_controller().define_current_tower(context)
    context.get_enemies_controller().define_current_enemy()
    context.get_maps_controller().definition_current_tile(event, context)  # определяет текущий тайл
    context.get_enemies_controller().kill_enemies(context)

    if event.type == pygame.MOUSEBUTTONDOWN:  # если кнопка мыши нажата
        if context.get_enemies_controller().get_current_enemy():  # если выделенный враг существует и существует хотя бы одна башня
            context.get_towers_controller().fire(context)
    ButtonWorks.button_works(event, context)
    ShopWorks.shop_works(shop, event, context)
    context.get_config_constant_object().get_button_exit().handle_event(event)
