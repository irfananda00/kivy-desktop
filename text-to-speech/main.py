import kivy
kivy.require("1.7.1")

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

class TextToSpeech(BoxLayout):
    saywhat_text = ObjectProperty(None)

    def say_something(self, text):
        subprocess.call(["espeak", text])

    def clear(self):
        self.saywhat_text.text = ""
        self.saywhat_text.focus = True

class TextToSpeechApp(App):
    def build(self):
        return TextToSpeech()

if __name__ == "__main__":
    TextToSpeechApp().run()
