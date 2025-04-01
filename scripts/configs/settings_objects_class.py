from scripts.classes_objects.button_class import Button

class SettingsObjects:
    def __init__(self, width, height, change_using_additional_parameter, sound_controller):
        self.__button_additional_parameter = Button(width // 2 - height // 10, height // 2 - height//10, 'images/UI/setting_button.png', height//5, height//5, change_using_additional_parameter)
        self.__button_sound_setting = Button(width // 2 - 1.5 * height // 5 - height // 7, height // 2 - height//10, 'images/UI/setting_button.png', height//5, height//5, sound_controller.sound_setting)
        self.__button_music_setting = Button(width // 2 + height // 10 + height // 7, height // 2 - height//10,'images/UI/setting_button.png', height//5, height//5, sound_controller.music_setting)

    def draw_buttons(self, context):
        self.__button_additional_parameter.draw_button_with_text('Additional parameter:' + str(context.get_config_gameplay(). get_always_use_additional_parameters()), context)
        self.__button_sound_setting.draw_button_with_text('Play sound:' + str(context.get_sound_controller().get_play_sound()), context)
        self.__button_music_setting.draw_button_with_text('Play music:' + str(context.get_sound_controller().get_play_music()), context)

    def action_settings(self, event, context):
        if self.__button_additional_parameter.is_pressed(event):
            context.get_file_save_controller().change_true_false('always use additional parameter')
            context.get_config_gameplay().set_always_use_additional_parameters(context.get_file_save_controller().get_parameter('always use additional parameter'))
        if self.__button_sound_setting.is_pressed(event):
            self.__button_sound_setting.handle_event_parameter(context)
        if self.__button_music_setting.is_pressed(event):
            self.__button_music_setting.handle_event_parameter(context)