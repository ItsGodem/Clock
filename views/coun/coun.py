
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.uix.modalview import ModalView
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock, mainthread
import datetime as t
import playsound as p
from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty, ObjectProperty,BooleanProperty
Builder.load_file('views/coun/coun.kv')
class Coun(BoxLayout):
    sec=0
    min=0
    hur=0
    sec_str=StringProperty('0')
    min_str=StringProperty('0')
    hur_str=StringProperty('0')
    secs=NumericProperty(0.0)
    mins=NumericProperty(0.0)
    hurs=NumericProperty(0.0)
    stbutton=BooleanProperty(False)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render,.1)
        
        Clock.schedule_interval(self.repeat, 1*(10**-100))


    
    def render(self, _):
        pass
    def up(self,h):
        if h=='sec':
            if self.sec<59:
                self.sec+=1
            else:
                self.sec=0
        if h=='min':
            if self.min<59:
                self.min+=1
            else:
                self.min=0
        if h=='hur':
            if self.hur<24:
                self.hur+=1
            else:
                self.hur=0
    def down(self,h):
        if h=='sec':
            if self.sec>0:
                self.sec-=1
            else:
                self.sec=59
        if h=='min':
            if self.min>0:
                self.min-=1
            else:
                self.min=59
        if h=='hur':
            if self.hur>0:
                self.hur-=1
            else:
                self.hur=23
    def play(self):
        if self.sec>0 or self.min>0 or self.hur>0:
            Clock.schedule_interval(self.co_down, .1)
    def pu(self):
        Clock.unschedule(self.co_down)
    def re(self):
        Clock.unschedule(self.co_down)
        self.sec=0
        self.hur=0
        self.min=0
        Clock.unschedule(self.cheak, .1)

        self.stbutton =False
    def co_down(self,_):
        if self.sec>0:
            self.sec-=.1
        else:
            if self.min>0:
                self.min-=1
                self.sec=60
            else:
                if self.hur>0:
                    self.hur-=1
                    self.min=60
            
        Clock.schedule_once(self.cheak,.1)
        self.stbutton =True
    def cheak(self,_):
        if self.sec<=0 and self.min<=0 and self.hur<=0:
            
            p.playsound('/home/kareem/Desktop/New Folder/python/ri.mp3')
            self.stbutton =False

            Clock.unschedule(self.co_down)
    def repeat(self,_):
        self.sec_str=str(self.sec)
        self.min_str=str(self.min)
        self.hur_str=str(self.hur)
        self.secs=float(self.sec_str)*6
        self.mins=float(self.min_str)*6
        self.hurs=float(self.hur_str)*15