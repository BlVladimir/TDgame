from pygame import MOUSEBUTTONDOWN, mixer

class SoundController:

    def __init__(self):
        self.__sound_directory_dict = {'shot':mixer.Sound('Sound/Shot.mp3'),
                                       'poison_shot':mixer.Sound('Sound/PoisonShot.mp3'), 'electric_shot':mixer.Sound('Sound/ElectricShot.mp3'), 'click':mixer.Sound('Sound/Click.mp3'),
                                       'death':mixer.Sound('Sound/DeathEnemy.mp3'), 'walk':mixer.Sound('Sound/MovementEnemy.mp3')}
        mixer.Sound.set_volume(self.__sound_directory_dict['shot'], 0.03)
        mixer.Sound.set_volume(self.__sound_directory_dict['electric_shot'], 0.03)
        mixer.Sound.set_volume(self.__sound_directory_dict['poison_shot'], 0.1)
        mixer.Sound.set_volume(self.__sound_directory_dict['death'], 0.1)
        self.__play_music = True
        self.__play_sound = True
        if self.__play_music:
            mixer.music.load('Sound/MusicGame.mp3')
            mixer.music.set_volume(0.01)
            mixer.music.play()

    def click_sound(self, event):
        if self.__play_sound and event.type == MOUSEBUTTONDOWN:
            self.__sound_directory_dict['click'].play()

    def play_sound(self, name_sound):
        if self.__play_sound:
            self.__sound_directory_dict[name_sound].play()

    def stop_sound(self, name_sound):
        if self.__play_sound:
            self.__sound_directory_dict[name_sound].stop()

    def sound_setting(self):
        if self.__play_sound:
            self.__play_sound = False
        else:
            self.__play_sound = True

    def music_setting(self):
        if self.__play_music:
            self.__play_music = False
            mixer.music.stop()
        else:
            self.__play_music = True
            mixer.music.play()