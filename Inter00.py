#!/usr/bin/env python

import random
import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics.context_instructions import Color
from kivy.uix.scrollview import ScrollView

class InterScreenWidget(BoxLayout):
    
    def BtnHit(self, **args):
        self.ids['CONTENT'].text += ' hit'

class StatBlockWidget(BoxLayout):
    pass

class ContentBlockWidget(ScrollView):
    text = StringProperty('')

class ButtonBlockWidget(BoxLayout):
    pass

class ActionButton(Button):
    pass

class Inter00(App):
    def build(self):
        return InterScreenWidget()

if __name__ == "__main__":
	Inter00().run()
