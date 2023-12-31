
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock, mainthread
from os import *
from time import sleep
import shutil
from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    folderpath_en = StringProperty('')

    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
        
    def render(self, _):
        pass