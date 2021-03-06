from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

class ButtonGrid(GridLayout):
	def do_click(self, number):
		filename = "Sounds/audio" + number + ".mp3"
		sound = SoundLoader.load(filename)
		sound.play()

class MagicPiano(App):
	def build(self):
		return ButtonGrid()

if __name__ == "__main__":
	MagicPiano().run()