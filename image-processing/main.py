import kivy
kivy.require("1.7.1")

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel

class ImageProcessing():
    def crop(self, h, w):
        pass

class RootWidget(BoxLayout):
    pass

class TableLayout(TabbedPanel):
    pass

class ImageProcessingApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    ImageProcessingApp().run()
