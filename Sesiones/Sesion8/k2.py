
from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label  import Label
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):

    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Hola Clase 2',
            font_size=150)
        f.add_widget(s)
        s.add_widget(l)
        return f

TestApp().run()
