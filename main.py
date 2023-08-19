from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image


class LoginPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        # Create the background image widget
        self.background = Image(source='123.jpg',allow_stretch=True, keep_ratio=False, size_hint=(1, 1))

        self.register_input = TextInput(hint_text='Register Number')
        self.roll_input = TextInput(hint_text='Roll Number')
        self.signin_button = Button(text='Sign In',background_color='blue',bold=True)

        self.signin_button.bind(on_press=self.sign_in)
        self.roll_input.pos_hint = {"center_x": .5, "center_y": .5}
        self.register_input.size_hint = (0.4, 0.2)
        self.roll_input.size_hint = (0.4, 0.2)
        self.register_input.pos_hint = {"center_x": .5, "center_y": .5}
        self.signin_button.size_hint = (0.4, 0.2)
        self.signin_button.pos_hint = {"center_x": .5, "center_y": .5}
        self.empty_space = Label(size_hint_y=None, height=10)

        layout = BoxLayout(orientation='vertical',spacing=10)
        layout.add_widget(self.background)

        layout.add_widget(self.register_input)
        layout.add_widget(self.roll_input)
        layout.add_widget(self.signin_button)
        layout.add_widget(self.empty_space)

        self.add_widget(layout)

    def sign_in(self, instance):
        register_number = self.register_input.text
        roll_number = self.roll_input.text
        if register_number and roll_number:
            sm.current = 'main'


class MainPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        buttons = ['DOM', 'DME', 'THERMAL-I', 'COMP LAB']
        for text in buttons:
            button = Button(text=text)
            button.bind(on_press=self.show_questions)
            layout.add_widget(button)

        self.add_widget(layout)

    def show_questions(self, instance):
        sm.current = 'questions'


class QuestionsPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        for i in range(1, 11):
            button = Button(text=f'Question {i}')
            layout.add_widget(button)

        self.add_widget(layout)

sm = ScreenManager()
sm.add_widget(LoginPage(name='login'))
sm.add_widget(MainPage(name='main'))
sm.add_widget(QuestionsPage(name='questions'))


class PECApp(App):
    def build(self):



        return sm


if __name__ == '__main__':
    PECApp().run()
