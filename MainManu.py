def draw_buttons(context):
    buttons_level = context.get_config_constant_object().get_button_level_array()
    for i in buttons_level:
        i.draw(context)

def handle_event(event, context):
    buttons_level = context.get_config_constant_object().get_button_level_array()
    context.get_config_gameplay().new_value_is_started(buttons_level[0].is_pressed(event))
    for i in range(len(buttons_level)):
        if buttons_level[i].is_pressed(event):
            buttons_level[i].handle_event_parameter({'context':context,'lvl':'lvl'+str(i+1)})