from scripts.main_scripts import button_works, shop_works
import pygame

def level(event, highlighting, context):
    button_works.is_started(context, highlighting)
    context.towers_controller.define_current_tower(context)
    context.enemies_controller.define_current_enemy()
    context.maps_controller.definition_current_tile(event, context)  # определяет текущий тайл
    context.enemies_controller.kill_enemies(context)

    if event.type == pygame.MOUSEBUTTONDOWN:  # если кнопка мыши нажата
        if context.enemies_controller.get_current_enemy():  # если выделенный враг существует и существует хотя бы одна башня
            context.towers_controller.fire(context)
    button_works.button_works(event, context)
    shop_works.shop_works(event, context)
    context.config_constant_object.get_button_exit().handle_event(event)
