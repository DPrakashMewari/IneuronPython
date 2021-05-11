import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Helloapp(GridLayout):
    def __init__(self):
        super(Helloapp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Student Name"))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Student Marks:"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender:"))
        self.s_gen = TextInput()
        self.add_widget(self.s_gen)

        self.press = Button(text="Click me")
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("you have entered your details successfully")
        print("Name of student" + self.s_name.text)
        print("Student Marks is" + self.s_marks.text)
        print("Marks of student" + self.s_gen.text)



class Hello(App):
    def build(self):
        return Helloapp()


if __name__ == "__main__":
    Hello().run()
