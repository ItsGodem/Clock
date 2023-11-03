
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from kivy.clock import Clock, mainthread
import datetime as t
from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty
Builder.load_file('views/auth/auth.kv')
class Auth(BoxLayout):
    sec= NumericProperty(0)
    sec_str=StringProperty('00')
    min= NumericProperty(0)
    min_str=StringProperty('00')
    hor= NumericProperty(0)
    hur_str=StringProperty('00')
    snd=NumericProperty(0)
    mun=NumericProperty(0)
    hur=NumericProperty(0)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

        Clock.schedule_interval(self.repeat, 1*(10**-100))
        
    def render(self, _):
        pass
    
    def repeat(self,*args):
        no=t.datetime.now()
        self.snd='%02d.%06d' %(no.second,no.microsecond)
        self.mun='%02d' %(no.minute)
        self.hor='%02d' %(no.hour)
        self.sec=float(self.snd)*6
        self.min=int(self.mun)*6
        self.hur=int(self.hor)*15
        if int(self.sec/6)<10:
            self.sec_str = '0'+str(int(self.sec/6))
        else:
            self.sec_str = str(int(self.sec/6))
        if int(self.min/6)<10:
            self.min_str = '0'+str(int(self.min/6))
        else:
            self.min_str = str(int(self.min/6))
        if int(self.hur/15)<10:
            self.hur_str = '0'+str(int(self.hur/15))
        else:
            self.hur_str = str(int(self.hur/15))

            