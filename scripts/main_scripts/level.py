from scripts.main_scripts import shop_works
import pygame

def button_works(event, context):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not context.config_gameplay.get_is_fail():  # если кнопка была нажата
        context.animation_controller.start_move(context)  # переменная isMove нужна, чтобы определять, закончено движение или нет
    if pygame.key.get_pressed()[pygame.K_TAB]:  # была нажата кнопка таб
        context.config_gameplay.set_use_additional_parameters(True)
    else:
        context.config_gameplay.set_use_additional_parameters(False)


def level(event, context):
    context.towers_controller.define_current_tower(context)
    context.enemies_controller.define_current_enemy()
    context.maps_controller.definition_current_tile(event, context)  # определяет текущий тайл
    context.enemies_controller.kill_enemies(context)

    if event.type == pygame.MOUSEBUTTONDOWN:  # если кнопка мыши нажата
        if context.enemies_controller.get_current_enemy():  # если выделенный враг существует и существует хотя бы одна башня
            context.towers_controller.fire(context)
    button_works(event, context)
    shop_works.shop_works(event, context)
