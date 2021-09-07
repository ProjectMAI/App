from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)    # установка цвета фона окна

class BoxApp(App):
    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation = 'vertical', size_hint = [.5, .5])

        self.text_login = TextInput()
        self.text_password = TextInput()

        bl.add_widget(self.text_login)  # позиция Логин
        bl.add_widget(self.text_password) # позиция Пароль

        # Настройка кнопки  Войти
        bl.add_widget(Button(
            text= "Войти",

            font_size = 13,  # font_size рaзмер шрифта
            on_press=self.login_press,  # on_press нажата
            background_color=[1, 0, 0, 1],  # background_color цвет RGBA в %
            background_normal="",  # background_normal  делает цвет ярче
                     ))

        # Настройка кнопки  Зарегестрироваться
        bl.add_widget(Button(
            text = "Зарегестрироваться",
            font_size=13,  # font_size рaзмер шрифта
            on_press=self.password_press,  # on_press нажата
            background_color=[.5, .19, .88, 1],  # background_color цвет RGBA в %
            background_normal="",  # background_normal  делает цвет ярче
                    ))


        al.add_widget(bl)
        return al

    def on_text(self,instance,value):
        self.on_text.text = print(self.on_text)



 # Вывод пароля и логина в консоль

    # При клике на "Войти"
    def login_press(self, instance):
        print(self.text_login.text)
        print(self.text_password.text)

    # При клике на "Зарег."
    def password_press(self, instance):
        print(self.text_login.text)
        print(self.text_password.text)

if __name__ == "__main__":
    BoxApp().run()