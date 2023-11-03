
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock, mainthread
import datetime as t
import math 

from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty
Builder.load_file('views/temporary/temporary.kv')
class Temporary(BoxLayout):
    misec= NumericProperty(0)
    misec_str=StringProperty('00')
    sec= NumericProperty(0)
    sec_str=StringProperty('00')
    min= NumericProperty(0)
    min_str=StringProperty('00')
    hur= NumericProperty(0)
    hur_str=StringProperty('00')
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
    
        
    def render(self, _):
        pass
    def e(self):
        Clock.schedule_interval(self.repeat, .01)
    def pu(self):
        Clock.unschedule(self.repeat)
    def re(self):
        Clock.unschedule(self.repeat)
        self.sec=0
        self.min=0
        self.hur=0
        self.misec=0
        self.misec_str=str(self.misec)
        self.min_str=str(self.min)
        self.hur_str=str(self.hur)
        self.sec_str =str(self.sec)
    def repeat(self,*args):
        if self.misec>=99:
            self.misec=0
            self.sec+=1
        else:
            self.misec+=1
        if self.sec==60:
            self.min+=1
            self.sec=0
        if self.min==60:
            self.hur+=1
            self.min=0
        self.min_str=str(self.min)
        self.hur_str=str(self.hur)
        self.sec_str =str(self.sec)
        self.misec_str=str(round(self.misec,3))