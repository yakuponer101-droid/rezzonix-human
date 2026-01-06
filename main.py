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
