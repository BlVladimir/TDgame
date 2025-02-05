def draw_buttons(screen, context):
    buttons_level = context.get_config_button().get_button_level_array()
    for i in buttons_level:
        i.draw(screen)

def handle_event(event, context):
    buttons_level = context.get_config_button().get_button_level_array()
    isStarted = buttons_level[0].is_pressed(event)
    for i in range(len(buttons_level)):
        if buttons_level[i].is_pressed(event):
            buttons_level[i].handle_event_parameter('lvl'+str(i+1))
    return isStarted