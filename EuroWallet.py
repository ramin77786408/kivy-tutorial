
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.widget import Widget
from kivymd.uix.button import MDRectangleFlatButton

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


from kivy.app import App

class MainWidget(BoxLayout):
    def mask(self):
        print("MASK")

    def on_pressed_qr(self):
        print("Qr Pressed")

    def on_pressed_paste(self):
        print("Paste pressed")

    def on_pressed_max(self):
        print("MAX pressed")

    def on_pressed_unit(self):
        print("Unit pressed")

class EuroWalletApp(MDApp):
    pass

if __name__ == '__main__':
    EuroWalletApp().run()