from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.clock import Clock
from kivymd.uix.progressbar import MDProgressBar


class RezzonixHumanApp(MDApp):
    def build(self):
        self.title = "Rezzonix Human Analyzer"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"

        screen = MDScreen()

        layout = MDBoxLayout(
            orientation="vertical",
            padding=40,
            spacing=30
        )

        self.label = MDLabel(
            text="REZZONIX HUMAN\nAnaliz Sistemi Hazır",
            halign="center",
            font_style="H5"
        )

        self.progress = MDProgressBar(
            value=0,
            max=100
        )

        self.button = MDRaisedButton(
            text="EL SENSÖRÜNÜ TUT & ANALİZİ BAŞLAT",
            pos_hint={"center_x": 0.5},
