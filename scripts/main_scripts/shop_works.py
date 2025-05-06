# def shop_works(context):
#     if context.config_gameplay.get_current_tile()is None:
#         context.config_gameplay.set_shop_type(0)
#     elif context.maps_controller.get_build_array[context.config_gameplay.get_current_tile]['is_filled']:
#         context.config_gameplay.set_shop_type(2)
#     else:
#         context.config_gameplay.set_shop_type(1)
#     if context.towers_controller.get_current_tower():
#         if context.towers_controller.get_current_tower().get_image_gun() is not None:
#             context.towers_controller.get_current_tower().rotate_gun()
#             context.towers_controller.get_current_tower().draw_radius(context)
#     context.config_gameplay.set_amount_of_money('x' + str(context.config_gameplay.get_money))  # рисует количество денег