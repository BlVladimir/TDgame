def draw_buttons(context):
    buttons_level = context.get_config_constant_object().get_button_level_array()
    for i in buttons_level:
        i.draw(context)

def handle_event(event, context):
    buttons_level = context.get_config_constant_object().get_button_level_array()
    for i in range(len(buttons_level)):
        if buttons_level[i].is_pressed(event):
            context.get_config_gameplay().set_is_started(True)
            buttons_level[i].handle_event_parameter({'context':context,'lvl':str(i+1)})