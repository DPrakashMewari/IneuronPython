import kivy
from kivy.app import App
from kivy.uix.label import Label

class Helloapp(App):
    def build(self):
        return Label(text="Hi!This is Prakays")

if __name__ == "__main__":
    Helloapp().run()