from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

from wallet_screen import address_field



class WalletApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Teal"     #['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        button = MDRectangleFlatButton(text="QR", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       on_release= self.get_qrcode)
        self.address = Builder.load_string(address_field)
        screen.add_widget(self.address)
        screen.add_widget(button)
        return screen

    def get_qrcode(self, obj):
        print(self.address.text)

if __name__ == '__main__':
    WalletApp().run()