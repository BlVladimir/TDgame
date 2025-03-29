from pygame import MOUSEBUTTONDOWN, mixer

class SoundController:

    def __init__(self):
        self.__sound_volume = 1
        self.__music_volume = 1
        self.__sound_directory_dict = {'music_menu':'Sound/MusicMenu.mp3', 'music_game':'Sound/MusicGame.mp3', 'shot':mixer.Sound('Sound/Shot.mp3'),
                                       'poison_shot':mixer.Sound('Sound/PoisonShot.mp3'), 'electric_shot':mixer.Sound('Sound/ElectricShot.mp3'), 'click':mixer.Sound('Sound/Click.mp3')}
        mixer.Sound.set_volume(self.__sound_directory_dict['shot'], 0.03)
        mixer.Sound.set_volume(self.__sound_directory_dict['electric_shot'], 0.03)
        mixer.Sound.set_volume(self.__sound_directory_dict['poison_shot'], 0.1)

    def click_sound(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.__sound_directory_dict['click'].play()

    def play_sound(self, name_sound):
        self.__sound_directory_dict[name_sound].play()