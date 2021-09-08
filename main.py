from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

import sqlite3

db = sqlite3.connect('server.base') # создаем таблицу
sql = db.cursor() # Он позволяет делать SQL-запросы к базе


#подкл. к табл. и создаем 2 столбца - login и password
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT
) """)
db.commit()


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
        user_login = self.text_login.text
        user_password = self.text_password.text


        sql.execute(f"SELECT Login FROM users WHERE login = '{user_login}' ")
        if sql.fetchone() is None:
            print('Такого пользователя нет! Зарегистрируйтесь! Укажите почту и пароль, и нажмите "Зарегестрироваться"')
            #for value in sql.execute(" SELECT * FROM users "):  # вывод таблицы
            #    print(value)  # вывод таблицы

        else:
            sql.execute(f"SELECT Password FROM users WHERE Password = '{user_password}' ")
            if sql.fetchone() is None:
                print('Неверный пароль! Попробуйте ещё раз!')

            else:
                print('Успешно!')






    # При клике на "Зарег."
    def password_press(self, instance):
        user_login = self.text_login.text
        user_password = self.text_password.text


        sql.execute(f"SELECT Login FROM users WHERE login = '{user_login}' ")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?, ?)", (user_login, user_password))
            db.commit()
            print('Вы успешно зарегистрировались! Введите свои данные и нажмите "Войти"')
        else:
            print('Такой пользователь уже есть! Попробуйте войти')


if __name__ == "__main__":
    BoxApp().run()