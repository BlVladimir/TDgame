from pygame import MOUSEBUTTONDOWN, mixer

class SoundController:

    def __init__(self, file_save_controller):
        self.__sound_directory_dict = {'shot':mixer.Sound('sound/shot.mp3'),
                                       'poison_shot':mixer.Sound('sound/poison_shot.mp3'), 'electric_shot':mixer.Sound('sound/electric_shot.mp3'), 'click':mixer.Sound('sound/click.mp3'),
                                       'death':mixer.Sound('sound/death_enemy.mp3'), 'walk':mixer.Sound('sound/movement_enemy.mp3')}
        mixer.Sound.set_volume(self.__sound_directory_dict['shot'], 0.03)
        mixer.Sound.set_volume(self.__sound_directory_dict['electric_shot'], 0.03)
        mixer.Sound.set_volume(self.__sound_directory_dict['poison_shot'], 0.1)
        mixer.Sound.set_volume(self.__sound_directory_dict['death'], 0.1)
        self.__play_music = file_save_controller.get_parameter('play_music')
        self.__play_sound = file_save_controller.get_parameter('play_sound')
        mixer.music.load('sound/music_game.mp3')
        mixer.music.set_volume(0.01)
        if self.__play_music:
            mixer.music.play(loops=-1)

    def click_sound(self, event):
        if self.__play_sound and event.type == MOUSEBUTTONDOWN:
            self.__sound_directory_dict['click'].play()

    def play_sound(self, name_sound):
        if self.__play_sound:
            self.__sound_directory_dict[name_sound].play()

    def stop_sound(self, name_sound):
        if self.__play_sound:
            self.__sound_directory_dict[name_sound].stop()

    def sound_setting(self, context):
        if self.__play_sound:
            self.__play_sound = False
            context.file_save_controller.set_parameter('play_sound', False)
        else:
            self.__play_sound = True
            context.file_save_controller.set_parameter('play_sound', True)

    def music_setting(self, context):
        if self.__play_music:
            self.__play_music = False
            mixer.music.stop()
            context.file_save_controller.set_parameter('play_music', False)
        else:
            self.__play_music = True
            mixer.music.play(loops=-1)
            context.file_save_controller.set_parameter('play_music', True)

    def get_play_sound(self):
        return self.__play_sound

    def get_play_music(self):
        return self.__play_music