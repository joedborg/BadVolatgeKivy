from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class BadVoltageApp(App):
    def __init__(self):
        super(BadVoltageApp, self).__init__()
        self.sound = SoundLoader.load('/sdcard/Download/bv121.ogg')
        self.seek_memory = 0
        self.play_button = Button(text='Play')
        self.play_button.bind(on_press=self.play_callback)

    def play_callback(self, instance):
        if self.sound.status == 'stop':
            self.sound.seek(self.seek_memory)
            self.sound.play()
            self.play_button.text = 'Pause'
        elif self.sound.status == 'play':
            self.seek_memory = self.sound.get_pos()
            self.sound.stop()
            self.play_button.text = 'Play'

    def build(self):
        return self.play_button


BadVoltageApp().run()