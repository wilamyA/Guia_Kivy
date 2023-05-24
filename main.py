from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MyScreen, self).__init__(**kwargs)
        self.cols = 2

        # Label e campo para a data
        self.add_widget(Label(text='Data:'))
        self.date_input = TextInput()
        self.add_widget(self.date_input)

        # Label e campo para o horário
        self.add_widget(Label(text='Horário:'))
        self.time_input = TextInput()
        self.add_widget(self.time_input)

        # Label e campo para a lista
        self.add_widget(Label(text='Lista:'))
        self.list_input = TextInput()
        self.add_widget(self.list_input)

        # Botão Confirmar
        self.confirm_button = Button(text='Confirmar')
        self.add_widget(self.confirm_button)

        # Botão Cancelar
        self.cancel_button = Button(text='Cancelar')
        self.add_widget(self.cancel_button)


class MyApp(App):
    def build(self):
        # Título da tela
        title_label = Label(text='Minha Tela')

        # GridLayout principal com título e componentes
        root = GridLayout(cols=1)
        root.add_widget(title_label)
        root.add_widget(MyScreen())

        return root


if __name__ == '__main__':
    MyApp().run()
