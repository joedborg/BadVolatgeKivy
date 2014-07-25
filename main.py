from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class BadVoltageApp(App):
    def __init__(self):
        self.sound = SoundLoader.load('http://audio.lugradio.org/badvoltage/Bad%20Voltage%201x21.ogg')

    def build(self):
        return Button(text='Hello QPython')


BadVoltageApp().run()