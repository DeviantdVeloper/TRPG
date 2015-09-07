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

class ScatterTextWidget(BoxLayout):
    pass

class Inter00(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
	Inter00().run()
