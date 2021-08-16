import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label


Builder.load_string("""
<TextInput>:
    size_hint: (.1,None)
    height: 50
    text: "Enter File to Be Search"

""")



class file(App):
    def build(self):
        self.window = GridLayout()
        # Add coloumns
        self.window.cols = 1
        # Resize margin padding or size pos
        self.window.size_hint = (0.5, 0.5)
        self.window.pos_hint = {'center_x': 0.5, "center_y": 0.7}
        # Add Image
        self.window.add_widget(Image(source="one.png"))

        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)
        # Add button
        self.button = Button(text="Search", size_hint=(.1,.2), bold=True, background_color="#3339FF")
        self.window.add_widget(self.button)

        # Add button
        self.button = Button(text="Merge .txt files from search results", size_hint=(.1, .1), bold=True, background_color="#64FF33")
        self.window.add_widget(self.button)



        return self.window

if __name__ == "__main__":
    file().run()